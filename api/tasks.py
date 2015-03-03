import os
import urlparse
import logging
import traceback
logger = logging.getLogger('api')

import json
import time
from pymongo import MongoClient
from celery import shared_task
from models import CalculatedPosition, Receiver, Transmitter

from triangulation.intersector import find_common_center

mongouri = os.getenv('MONGOLAB_URI')
parsed = urlparse.urlsplit(mongouri)
db_name = parsed.path[1:]

db = MongoClient(mongouri)[db_name]

cfg_collection = db.config

cache_key = 'cached_recordings'
cache_timestamp_key = 'cached_recordings_last_update'

#Perform a triangulation whenever either of these conditions are met
max_recordings = 50
max_time = 500

def get_receiver_data(receiver_pks):
	data = {}
	for receiver in receiver_pks:
		receiver_obj = Receiver.objects.get(pk=receiver)
		data[receiver] = {
			'receiver': receiver,
			'x': receiver_obj.x,
			'y': receiver_obj.y,
			'z': receiver_obj.z
		}

	return data

@shared_task
def new_recording(transmitter_pk, receiver_pk, rssi, timestamp):
	#This is nessecary so that the transmitter pk can be a key in a mongo collection, because apparently only strings can be keys.
	transmitter_pk = str(transmitter_pk)
	
	cfg = cfg_collection.find_one()

	insert = False
	if cfg is None:
		insert = True
		cfg = {
			cache_key: {},
			cache_timestamp_key: time.time()
		}

	cached_recordings = cfg[cache_key]
	last_updated = cfg[cache_timestamp_key]

	if not transmitter_pk in cached_recordings:
		cached_recordings[transmitter_pk] = []
	
	cached_recordings[transmitter_pk].append({
		'receiver': receiver_pk,
		'transmitter': transmitter_pk,
		'rssi': rssi
	})

	#Check if conditions are met
	if len(cached_recordings[transmitter_pk])>max_recordings:
		tx = Transmitter.objects.get(pk=transmitter_pk)
		logger.info("Recording cache full. Performing position calculation.", extra = {
				'transmitter': str(tx)
			})
		#Get set of receiver pks
		receiver_list = set([recording['receiver'] for recording in cached_recordings[transmitter_pk]])
		
		try:
			#Use the cached recordings plus the receiver pks to triangulate the position
			center,uncertainty = find_common_center(cached_recordings[transmitter_pk],get_receiver_data(receiver_list))
		except:
			logger.error('Unexpected error raised: '+(traceback.format_exc()))
		#Create db entry for this
		if center and uncertainty:
			calcpos = CalculatedPosition(time=timestamp,transmitter=tx,x=center.x,y=center.y,z=0,uncertainty=uncertainty)
			calcpos.save()
			logger.info("Calculated position!", extra = {
				'transmitter': str(tx),
				'position': str(calcpos)
			})
		cached_recordings[transmitter_pk] = []

	cfg[cache_key] = cached_recordings

	if insert:
		cfg_collection.insert(cfg)
	else:
		cfg_collection.save(cfg)
