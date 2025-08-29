import cantools
def test_engine_speed():
    db = cantools.database.load_file("vehicle_sample.dbc")
    msg =db.get_message_by_name("ENGINE_STATUS")

#Encoding signal values
    encoded = msg.encode({"EngineSpeed": 800,"EngineTemp": 40})
# Decoding back
    decoded = msg.decode(encoded)

#asserttions
    assert decoded["EngineSpeed"] == 800
    assert decoded["EngineTemp"] == 40