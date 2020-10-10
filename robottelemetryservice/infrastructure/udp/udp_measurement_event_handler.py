import socketserver
import threading
from robottelemetryservice.infrastructure.serialisation import serializer
from robottelemetryservice.infrastructure.configuration import application

measurement_repository=application.get_measurement_repository()

class UDPMeasurementEventHandler(socketserver.DatagramRequestHandler):
    def handle(self):
        udp_payload=self.request[0].strip().decode()
        measurements=serializer.udp_msg_to_measurements(udp_payload)
        measurement_repository.add(measurements)
