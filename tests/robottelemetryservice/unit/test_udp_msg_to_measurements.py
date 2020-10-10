from robottelemetryservice.infrastructure.serialisation import serializer

def test_udp_msg_to_measurements():
    udp_msg='''robot,1602336384,9999.99,1,1234.554,2,100.99,3'''
    measurements=serializer.udp_msg_to_measurements(udp_msg)
    assert measurements[0].dataValue==9999.99
    assert measurements[1].measurementLocationId==2
    assert measurements[2].dateTimeUTC==1602336384
    assert measurements[2].siteName=='robot'