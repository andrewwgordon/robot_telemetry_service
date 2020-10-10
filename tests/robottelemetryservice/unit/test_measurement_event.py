from robottelemetryservice.domain.measurement_event import MeasurementEvent

def test_measurement_event():
    measurement_event=MeasurementEvent('robot',1602334484,1234.5678,1)
    print(measurement_event.__dict__)
    assert measurement_event.siteName=='robot'
    assert measurement_event.dateTimeUTC==1602334484
    assert measurement_event.measurementLocationId==1
    assert measurement_event.dataValue==1234.5678