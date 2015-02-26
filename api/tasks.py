import os
import urlparse
import redis
import json
import time
from celery import shared_task
from models import CalculatedPosition, Receiver

from triangulation.intersector import find_common_center

url = urlparse.urlparse(os.environ.get('REDISCLOUD_URL'))
r = redis.Redis(host=url.hostname, port=url.port, password=url.password)

cache_key = 'wiloc_cached_recordings'
cache_timestamp_key = 'wiloc_cached_recordings_last_update'

#Perform a triangulation whenever either of these conditions are met
max_recordings = 20
max_time = 5

def get_receiver_data(receiver_pks):
	data = []
	for receiver in receiver_pk:
		receiver_obj = Receiver.objects.get(pk=receiver)
		data.append({
			receiver: receiver,
			x: receiver_obj.x,
			y: receiver_obj.y,
			z: receiver_obj.z
		})

	return data

@shared_task
def new_recording(transmitter_pk, receiver_pk, rssi, timestamp):
	cached_recordings = r.get(cache_key)
	last_updated = r.get(cache_timestamp_key)

	#Parse the cached recordings and last updated, or use sane defaults for both
	if cached_recordings is None:
		cached_recordings = {}
	else:
		cached_recordings = json.loads(cached_recordings)

	if last_updated is None:
		last_updated = time.time()
	else:
		last_updated = json.loads(last_updated)

	if not transmitter_pk in cached_recordings:
		cached_recordings[transmitter_pk] = []
	
	cached_recordings[transmitter_pk].append({
		receiver: receiver_pk,
		transmitter: transmitter_pk,
		rssi: rssi,
		timestamp: timestamp
	})

	#Check if conditions are met
	if (time.time()-last_updated)>max_time or len(cached_recordings[transmitter_pk])>max_recordings:
		#Get set of receiver pks
		receiver_list = set([recording['receiver'] for recording in cached_recordings[transmitter_pk]])
		
		#Use the cached recordings plus the receiver pks to triangulate the position
		center,uncertainty = find_common_center(cached_recordings[transmitter_pk],get_receiver_data(receiver_list))
		#Create db entry for this
		print ("MADE CALCULATED RECORDING. DATA: "+str((center,uncertainty)))
		cached_recordings[transmitter_pk] = []

	r.set(cache_key,json.dumps(cached_recordings))
	r.set(cache_timestamp_key,time.time())
