'''
in can bus tools:

1. dbc,kcd, sym , arxml cdd file parsing
2. CAN message encoding and decoding
3. Diagnostic DID encoding and decoding
4. Node tester
5. C source code generator
6. CAN bus monitor
7. Graphical plots of signals

3.1 Scripting
3.2 Command line tool
the decode subcommmand
the plot sub command
the dump sub command
the list sub command
the generate C sub command
the monitor subcommand

3.3
3.4
3.5
3.6
3.7
'''
# parsing small dbc file
# 01_parse_db_like.py
# 03_encode_decode_can.py
"""import cantools

db = cantools.database.load_file("V:/Learning/DBC_practise/sample.dbc")   # adjust path if needed

# --- Example A: STEER_STATUS ---
steer = db.get_message_by_name("STEER_STATUS")

payload = steer.encode({
    "STEER_TORQUE_SENSOR": 120,     # physical units per DBC (factor -1.0 means raw will be negated)
    "STEER_ANGLE_RATE": 5.0,        # deg/s (factor -0.1 internally)
    "STEER_STATUS": 0,              # 0..15 (4 bits)
    "STEER_CONTROL_ACTIVE": 1,      # boolean bit
    "STEER_CONFIG_INDEX": 2,        # 0..15 (4 bits)
    "COUNTER": 1,                   # 0..3 (2 bits)
    "CHECKSUM": 0                   # stand-in; compute real checksum if your ECU needs it
})
print("STEER_STATUS encoded:", payload)
print("STEER_STATUS decoded:", steer.decode(payload))

# --- Example B: WHEEL_SPEEDS ---
ws = db.get_message_by_name("WHEEL_SPEEDS")
ws_payload = ws.encode({
    "WHEEL_SPEED_FL": 47.5,   # kph
    "WHEEL_SPEED_FR": 47.3,
    "WHEEL_SPEED_RL": 46.9,
    "WHEEL_SPEED_RR": 47.1,
    "CHECKSUM": 0
})
print("WHEEL_SPEEDS encoded:", ws_payload)
print("WHEEL_SPEEDS decoded:", ws.decode(ws_payload))"""

#send on CAN (node-tester style) — WHEEL_SPEEDS burst
# 05_node_tester_ping.py
"""import time, can, cantools

# choose your interface:
# Linux vcan: channel="vcan0", bustype="socketcan"
# PEAK:       channel="PCAN_USBBUS1", bustype="pcan"

bus = can.interface.Bus(channel="vcan0", interface="virtual")

db = cantools.database.load_file("V:/Learning/DBC_practise/sample.dbc")
ws = db.get_message_by_name("WHEEL_SPEEDS")

for i in range(20):
    base = 30 + i * 0.5
    data = ws.encode({
        "WHEEL_SPEED_FL": base + 0.2,
        "WHEEL_SPEED_FR": base + 0.0,
        "WHEEL_SPEED_RL": base - 0.3,
        "WHEEL_SPEED_RR": base - 0.1,
        "CHECKSUM": 0
    })
    msg = can.Message(arbitration_id=ws.frame_id, data=data, is_extended_id=False)
    bus.send(msg)
    print("TX:", msg)
    time.sleep(0.05)"""

#live monitor + decode (all three messages)
# 06_monitor_decode.py
"""import can, cantools

db = cantools.database.load_file("V:/Learning/DBC_practise/sample.dbc")
bus = can.interface.Bus(channel="vcan0", interface="virtual")

print("Monitoring… Ctrl+C to stop.")
try:
    while True:
        rx = bus.recv(timeout=1.0)
        if not rx:
            continue
        try:
            m = db.get_message_by_frame_id(rx.arbitration_id)
            print(f"0x{rx.arbitration_id:X}", m.decode(rx.data))
        except KeyError:
            print(f"0x{rx.arbitration_id:X} [unknown] data={rx.data.hex()}")
except KeyboardInterrupt:
    pass
"""
#quick plotting (wheel speeds over time)

# 07_plot_signals.py
"""import pandas as pd, matplotlib.pyplot as plt, cantools, can, time

db = cantools.database.load_file("V:/Learning/DBC_practise/sample.dbc")
ws = db.get_message_by_name("WHEEL_SPEEDS")
bus = can.interface.Bus(channel="vcan0", interface="virtual")

rows = []
print("Collecting 5s of data…")
t0 = time.time()
while time.time() - t0 < 5:
    rx = bus.recv(0.5)
    if not rx or rx.arbitration_id != ws.frame_id:
        continue
    sig = ws.decode(rx.data)
    rows.append({"t": rx.timestamp - t0, **sig})

df = pd.DataFrame(rows)
if not df.empty:
    df.plot(x="t", y=["WHEEL_SPEED_FL","WHEEL_SPEED_FR","WHEEL_SPEED_RL","WHEEL_SPEED_RR"])
    plt.title("Wheel Speeds (kph)")
    plt.xlabel("Time (s)"); plt.ylabel("kph")
    plt.show()
else:
    print("No WHEEL_SPEEDS frames captured. Make sure something is transmitting.")"""






