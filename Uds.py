# useful for unit testing for UDS, Simulating ECU,HIL test automation,(paired with python- can , cantools, etc
'''
switching sessions - 0x10
reading data by identifier - 22
writing data by identifier - 2E
reseting ECU - 0x11
clearing DTC - 0X14
Running diagnostics routines - 0x31

1. simulate an ECU using udsoncan.server.server
2. send & valid UDS requests  to ECU using client
3. use pytest to write automated UDS tests
4. Highlevel functoin to read DID'S, reset ECU, switch sessions

'''
from matplotlib.backends.backend_nbagg import connection_info

#Client
#used to initate and manage diagnostics requests
'''
from udsoncan.client import Client
with Client(connection, request_timeout = 2) as client:
    client.change_session(0x03)
'''
#Connection
#Wraps transport layer (usually ISO-TP over CAN)
'''
from udsoncan.connections import PythonIsoTpCconnection
conn = pythonIsoTpConnection(isotp.CanStack(bus=bus, address=tp_addr))
'''
#Transport layer(ISO-TP +CAN)
#Uds uses IsoTP(ISO 15765) to send UDS message over CAN
# here in the 2nd line you need to define can_bus and isotp_addr
'''
import isotp
stack = isotp.CanStack(bus = can_bus, address = isotp_addr()
'''
#Config:
'''#Used to customize how client/Server behaves

from udsoncan import configs
configs.default_client_config'''

#if you want to seethe raw bytes then use
'''import logging
logging.basicConfig(level=logging.DEBUG)
'''
#now lets write all the commands to send the message uds on can and get the responses
#import all libraries
# now lets write all the commands to send the message uds on can and get the responses
# import all libraries

import threading, time
import can, isotp
from udsoncan import configs,services
from udsoncan import didcodec as did
from udsoncan.server import Server
from udsoncan.connections import PythonIsoTpConnection
from udsoncan.client import Client

# ---------- CONFIG ----------
BITRATE = 500000
TXID_TESTER = 0x7E0      # tester -> ECU
RXID_ECU    = 0x7E8      # ECU -> tester
VIN_STR = "TESTVIN123456789"

# ---------- SERVER (fake ECU) ----------
def start_fake_ecu():
    bus = can.Bus(interface="virtual", channel="vcan0", bitrate=BITRATE)
    # ECU perspective: it transmits on RXID_ECU and receives on TXID_TESTER
    addr_srv = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=RXID_ECU, rxid=TXID_TESTER)
    stack_srv = isotp.CanStack(bus=bus, address=addr_srv)
    conn_srv = PythonIsoTpConnection(stack_srv)

    class App:
        def __init__(self): self.vin = VIN_STR
        def get_data_identifier(self, did_value, coding=None):
            if did_value == 0xF190:
                return self.vin

    cfg = configs.default_server_config.copy()
    cfg["data_identifiers"] = {0xF190: did.AsciiCodec(17)}

    server = Server(app=App(), connection=conn_srv, config=cfg)
    server.start()
    return server

# ---------- CLIENT (tester) ----------
def run_client():
    bus = can.Bus(interface="virtual", channel="vcan0", bitrate=BITRATE)
    addr_cli = isotp.Address(isotp.AddressingMode.Normal_11bits, txid=TXID_TESTER, rxid=RXID_ECU)
    stack_cli = isotp.CanStack(bus=bus, address=addr_cli)
    conn_cli = PythonIsoTpConnection(stack_cli)
    with Client(conn_cli, request_timeout=2, config=configs.default_client_config) as client:
        client.change_session(services.DiagnosticSessionControl.Session.extendedDiagnosticSession)
        resp = client.read_data_by_identifier(0xF190)
        print("VIN (decoded):", resp.service_data.values[0xF190])
        print("Raw UDS response:", resp.original_payload.hex().upper())

if __name__ == "__main__":
    srv = start_fake_ecu()
    time.sleep(0.2)          # give the server a moment to boot
    try:
        run_client()
    finally:
        srv.stop()
