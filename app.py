import sys
import logging
import configparser
import socketserver
import threading
from robottelemetryservice.infrastructure.configuration import application
from robottelemetryservice.infrastructure.udp.udp_measurement_event_handler import UDPMeasurementEventHandler

log=logging.getLogger(__name__)

def run():
    log.info('Robot Telemetry Service...')
    app_config=application.get_app_config()
    try:
        server_address=('0.0.0.0',int(app_config['Host']['host.port']))
        udpServer=socketserver.ThreadingUDPServer(server_address,UDPMeasurementEventHandler)
        udpServer.serve_forever()
    except Exception as ex:
        log.error(ex)
        sys.exit(1)

if __name__=='__main__':
    run()
