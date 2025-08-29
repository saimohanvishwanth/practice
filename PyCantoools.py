# load dbc file
import cantools
db = cantools.database.load_file("vehicle_sample.dbc")
#Inspect messages and signals, Look for the correct message that contains "EngineStatus" as a signal or message.
for message in db.messages:
    print(f"message: {message.name}")
    for signal in message.signals:
        print(f" signal:{signal.name}")

# Encoding "ENGINE_STATUS" signal in to CAN Frame
# here inside message ENGINE_STATUS ,signals :EngineSpeed,EngineTemp
#get the message object
msg = db.get_message_by_name("ENGINE_STATUS")
#Encode the signal value (ex: EngineStatus = 1)
data =msg.encode({"EngineSpeed": 800,"EngineTemp" :40})
print(f"encoded data :{data}") #O/P: encoded data :b'\x00\x19P\x00\x00\x00\x00\x00'

# decoding the CAN fram back to signal values
#you can decode that same byte data back:

decoded = msg.decode(data)
print(f"Decoded Signals: {decoded}")

assert decoded["EngineSpeed"] == 800
'''
# decode a can frame in to signals
msg = db.get_message_by_name("ENGINE_STATUS")
decoded = msg.decode([0x0A, 0X0B, 0X00,0X00, 0X00])
print(decoded)'''

