'''import can
#to create a CAN bus
bus = can.Bus(interface ="virtual",channel = "vcan0",bitrate =50000)
# to create sender bus
sender =can.Bus(interface = "virtual", channel = "vcan0", bitrate = 500000)
#create the message
msg = can.Message(arbitration_id=0x123,data=[0x01,0x01,0x03,0x04],is_extended_id = False)
#send message to sender
sender.send(msg)
# shutdown
bus.shutdown()
sender.shutdown()

-----------------------------------------------------
# receive a CAN message:
received = bus.recv(timeout=1.0)
print(received.arbitration_id, received.data)
# or
------
import can
#you can use this way to receive a CAN message:
#create the CAN bus
receiver= can.Bus(interface = "virtual", channel = "vcan0", bitrate = 500000)
# wait for receive a CAN message
print("waiting to receive a CAN message")
received_msg = receiver.recv(timeout = 5.0) # wait for 5 sec
if received_msg:
    print("message received")
    print(f"arbitration_id:{hex(received_msg.arbitration_id)}")
    print(f"data: {list(received_msg.data)})")
#Shutdown receiver
receiver.shutdown()
---------------------------------
'''
# if you want to send and receive message at same Bus then you can use this code
'''
import can

sender = can.Bus(interface="virtual", channel="vcan0", bitrate=500000)
receiver = can.Bus(interface="virtual", channel="vcan0", bitrate=500000)

msg = can.Message(arbitration_id=0x123,
                  data=[0x01, 0x02, 0x03, 0x04],
                  is_extended_id=True)
sender.send(msg)

received = receiver.recv(timeout=5.0)
if received:
    print(received.arbitration_id, received.data)

sender.shutdown()
receiver.shutdown()

'''
# if you want to use send and receive in separate node or more than one node
'''
import can
import time
# create a receiver node(1st CAN bus)
receiver = can.Bus(interface = "virtual", chaneel = "van0", bitrate = 500000)
# create a sender node(2nd CAN Bus)
sender = can.Bus(interface = "virtual", channel = "vcan0", bitrate = 500000)
# prepare a CAN message to send
msg = can.Message(arbitration_id=0x124, data=[0x01, 0x03,0x04,0x05], is_extended_id =False)
#Send messgae from sender
sender.send(msg)
#allow a moment for transmission(but safer side)
time.sleep(0.1)
# try to receive the message on receiver side

received = receiver.recv(timeout=3.0)
if received:
    print("your message has been received")
    print(f"ID:{hex(received.arbitration_id)}")
else:
    print("your message has not been received")

# shutdown
sender.shutdown()
receiver.shutdown()
'''