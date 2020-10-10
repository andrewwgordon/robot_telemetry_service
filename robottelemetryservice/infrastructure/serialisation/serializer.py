from typing import List
from robottelemetryservice.domain.measurement_event import MeasurementEvent

def udp_msg_to_measurements(udp_msg: str) -> List[MeasurementEvent]:
    measurements=[]
    udp_items=udp_msg.split(',')
    for i in range(2,len(udp_items),2):
        measurements.append(
            MeasurementEvent(
                udp_items[0],
                int(udp_items[1]),
                float(udp_items[i]),
                float(udp_items[i+1])
            )
        )
    return measurements
