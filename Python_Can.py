



#sending a single messgae
'''
Environment variables:
can_interface
can_channel
can_bitrate
can_config
Interface names:
as we are doing with out hardware , can choose:
"virtual" - virtual

3.1 BUS
Transmitting
Receiving
Filtering
Bus API
Thread safe bus

3.2Message

3.3
Notitifier
Listners
BufferedReader
RedirectReader

3.4 File IO
reading and writing file
printer
CSV Writer
SqliteWriter
ASC(.asc Logging format)
Log
BLF
MF4
TRC
Rotating Logger
Replaying Files

3.5 Asyncio support

3.6 Broadcast Manager
Message senging tasks

3.7 Error Handling
3.8 Bit Timing Configuration






main objects -
1.Bus
vector_bus = can.Bus(interface= "virtual"
2. Message
3. Channel
4. Bitrate
5. Config
bus = can.interface.Bus(channel = "can0", interface = "virtual", can_filters = filters)
 Bus API:
 parametes
 1. channel : None/ vcan0
2. Interface : virtual/None
3. config_context :
4. ignore_config: None
5. kwargs -  any interface specific keyword arguments

block waiting for a message from the bus

parameters
timeout(float/None)- seconds to wait for a message or None to wait
Returns
None on timeout/ message object
Raises
canoperationerror- if an error occured while reading
------------------------------------------------------
#abstractmethod send(msg, timeout =None)
transmit a message to CAN bus
Override this method to  enable transmit path

1. Parameters
msg
timeout

2, Raises
canoperationerror- if an error occured while reading

3. Return type
None on timeout/ message object

-----------------------------------------------------

send_periodic(msgs, period, duration=None, store_task =True, autostart = True, modifier_callback = None)

Start sending messages at a given period on this bus
the task with be active until one of the following conditions are met:
the duration expires
the BUS instance goes out of scope
the BUS instance is shutdown
stop_all_periodic_task() is called
the task stop() method is called

#Parameters:
1. msgs - Message to transmit
2. period - period in seonds between each message
3. duration - Approximate duration in seconds to continue sending messagee.If no duration is provided, task will continue
4. store_task -
5. autostart - sending task will imediately start after creation
6. modifier_callback - function which should be used to modify each message's data before sending.

#:returns
a started task instance.Note the task can be stopped by calling the task's stop() method

returns type
cyclicsendtaskABC
-----------------------------------
#setfilters(filters = None)
apply filtering to all message received by this Bus

Parameters
#filters(sequence[CanFilter]/None)-
iterable of dictionaries each containing a "can_id", "can_mask" and optionsl "extended" :key
[{"can_id" : 0x11, "can_mask": 0x21, "extended": False}]]

#Return type
None
#shutdown()
#stop_all_periodic_tasks
stop sending any messages that were started using send_period()
-----------------------------------------------------

#Thread safe bus
this thread safe versoin of BusABC class can be used by multiple threads at once.
Sending and Receiving is locked separately to aviod unneccssary delay.
conflicting calls are executed by blocking untill bus is accessible.

my_bus = can.ThreadSafeBus(interface = "virtual", channel = "vcan0")
my_bus.send()
my_bus.recv()

#Syntax
class can.ThreadSafeBus(channel = None, interface =  None, config_context = None, ignore_config = False, *kwargs)


Contains a thread safe can.BusABC implementatoin that wraps around an exisiting interface instance.
All public methods of that base class are now safe to be called from multiple threads.



#Parameters
channel
interface
config_context
ignore_config
kwargs
-------------------------------------

Message
class can.Message(timestamp = 0.0, arbitration_id = 0, is_extended_id = True, is_remote_frame = False, is_error_frame = False,
channel =None, dtc = None, data = None, is_fd = False, is_rx = True
, bitrate_switch = False, error_state_indicator = False, check = False)

The message object is ued to represent CAN message for sending , receving and other purpose converting different logging formats
messages can use extended identifiers, be remote/error frames, contian data and amy be associated to a channel.
messages are always compared by identify and never by value, becaues that may introduce unexpected behaviour.
messages do not support "dynamic" attributes, meaning others than documented ones, since it uses __slots__

to create a message object

#Parameters
check
timestamp
arbitration_id
is_extended_id
is_remote_frame
is_error_frame
channel
dlc
data
is_fd
is_rx
bitrate_switch
error_State_indicator

#:raises
Value Error - If and only if check is set to True and one/ more arguments were invalid


#equals(other, timestamp_delta =1e-06, check_channel = True, check_direction = True)

2. Notifiers and Listerners
Notifier:
Notifier object is used as a message distributor for a bus.
the Notifier uses an event loop/ creates a thread to read messages from the bus and distributes them to listerners

#
class can.Notifier(bus, listerners, timeout = 1.0, loop = None)

Manages the distribution of Message instances to listernses
supports multiple buses listerners

Parameters:
---------------------------
bus(BusABC / list[ABC]) - A Bus/ list of buses to consume message from

listerners (iterable[Listener/ Callable[Message], Awaitable[None]-
an iterable of Listeners or collables that receive a Message and return Nothing.


timeout- An optional max no of seconds to wait for any Message


loop - An asyncio event loop to schedule the listeners

Raises
-----------
ValueError - If a passed in bus is already assigned to an active Notifier

3. add_bus(bus)
add a bus notificatoin
Parameters
bus(BusABC)- CAN bus instance

:raises
ValueError - If a bus is already assigned to an active Notifier

Return type
None

4. add_listner(listener)
add new listner to notification list.
if it is already present ,it will be called two times each time a message arrives

---
Parameters
listener - listener to be added to the list to be notified

Return type
None
----
property bus: BusABC| tuple[BusABC]- return the associated bus/tuple





'''


#Transmitting:

import can

def send_one():
    """Sends a single CAN message on a virtual bus (Windows)."""
    msg = can.Message(
        arbitration_id=0x0123,
        data=[0, 25, 0, 2, 3, 4, 5, 1],
        is_extended_id=True
    )
    with can.Bus(interface="virtual", channel="vcan0", bitrate=500000) as bus:
        try:
            bus.send(msg)
            print(f"Message sent on {bus.channel_info}")
        except can.CanError:
            print("Message not sent")

if __name__ == "__main__":
    send_one()


