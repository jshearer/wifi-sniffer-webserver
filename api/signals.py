import logging
logger = logging.getLogger('api')

from django.db.models.signals import post_save
from django.dispatch import receiver

from models import Recording
from tasks import new_recording

@receiver(post_save, sender=Recording)
def my_handler(sender, **kwargs):
	rec = kwargs['instance']
	new_recording.delay(rec.transmitter.pk, rec.receiver.pk, rec.rssi, rec.time)
	logger.info("Received new record!",extra=
		{
			'rssi': rec.rssi,
			'transmitter': str(rec.transmitter),
			'receiver': str(rec.receiver),
		})
	rec.delete()
