from robottelemetryservice.infrastructure.configuration import application
from robottelemetryservice.domain.measurement_event import MeasurementEvent
from robottelemetryservice.infrastructure.repository.measurement_event_sqlite_repository import MeasurementEventSQLiteRepository

app_config=application.get_app_config()

def test_measurement_event_repository():
    measurements=[]
    measurment_1=MeasurementEvent('rohot',1602336381,54321.1,2)
    measurment_2=MeasurementEvent('rohot',1602336382,14321.1,3)
    measurements.append(measurment_1)
    measurements.append(measurment_2)
    measurement_events_repository=MeasurementEventSQLiteRepository(app_config)
    measurement_events_repository.add(measurements)