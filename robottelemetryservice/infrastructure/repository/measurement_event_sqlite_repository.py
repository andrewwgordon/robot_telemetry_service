import logging
import sqlite3
from typing import List
from robottelemetryservice.domain.measurement_event import MeasurementEvent,IMeasurementEventRepository

log=logging.getLogger(__name__)

class MeasurementEventSQLiteRepository(IMeasurementEventRepository):
    
    SQL='''insert into measurement_event(site_name,date_time,data_value,measurement_location_id) values(?,?,?,?)    '''

    def __init__(self,app_config):
        self.__app_config=app_config
    
    def add(self,measurements: List[MeasurementEvent]):
        measurements_t=[]
        for measurement in measurements:
            measurements_t.append(tuple(measurement))
        try:
            conn=sqlite3.connect(self.__app_config['Database']['database.uri'])
            cur=conn.cursor()
            cur.executemany(self.SQL,measurements_t)
            conn.commit()
            conn.close()
        except Exception as ex:
            log.error(ex)
