import logging
import socketserver
import threading
from robottelemetryservice.infrastructure.serialisation import serializer
from robottelemetryservice.infrastructure.configuration import application

log=logging.getLogger(__name__)
measurement_repository=application.get_measurement_repository()

class UDPMeasurementEventHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        udp_payload=self.request[0].strip().decode()
        ip_address=self.client_address[0]
        log.info(ip_address+":"+udp_payload)
        # measurements=serializer.udp_msg_to_measurements(udp_payload)
        # measurement_repository.add(measurements)
