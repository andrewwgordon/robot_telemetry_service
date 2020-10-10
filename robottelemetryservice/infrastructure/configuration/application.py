import sys
import logging
import logging.config
import configparser
from datetime import datetime
from robottelemetryservice.infrastructure.repository.measurement_event_sqlite_repository import MeasurementEventSQLiteRepository

try:
    logging.config.fileConfig('./robottelemetryservice/resources/logging.conf',disable_existing_loggers=False)
except Exception as ex:
    sys.stderr.write(str(datetime.now())+' - __main__ - FATAL - Error loading logging.conf...\n')
    raise ex

log=logging.getLogger(__name__)

app_config=configparser.RawConfigParser()
app_config.read('./robottelemetryservice/resources/robottelemetryservice.properties')

measurement_sqlite_repository=MeasurementEventSQLiteRepository(app_config)

def get_app_config():
    return app_config

def get_measurement_repository():
    return measurement_sqlite_repository