import can
import PyCantoools


# Fake CAN message simulation
class MockBus:
    def send(self, msg):
        print(f"[MOCK SEND] Sent message to ID {msg.arbitration_id}: {msg.data}")

    def recv(self, timeout=1):
        # Simulated incoming CAN message
        return can.Message(arbitration_id=0x123, data=[0x01, 0x02, 0x03, 0x04], is_extended_id=False)


# Load a dummy or real DBC file (if you have one)
# db = cantools.database.load_file("your_file.dbc")

def test_can_message_decode():
    bus = MockBus()

    msg = can.Message(arbitration_id=0x123, data=[0x0A, 0x1B, 0x00, 0x00], is_extended_id=False)
    bus.send(msg)

    response = bus.recv()
    print(f"[MOCK RECV] Received: ID={response.arbitration_id}, Data={response.data}")

    # If using DBC decoding:
    # decoded = db.decode_message(response.arbitration_id, response.data)
    # print(decoded)

    assert response.arbitration_id == 0x123
    assert len(response.data) == 4
