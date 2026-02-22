def test_send_and_receive_message():
    session = FixSession("SESSION-2", config={"host": "localhost", "port": 1234})
    session.connect()
    assert session.send_message("8=FIX.4.2|9=12|35=A|49=CLIENT|56=SERVER|10=123|")
    received = session.receive_message("8=FIX.4.2|9=12|35=A|49=CLIENT|56=SERVER|10=123|")
    assert received == "8=FIX.4.2|9=12|35=A|49=CLIENT|56=SERVER|10=123|"
# test_session.py for Fixit
from fixit.session import FixSession

def test_session_connect_disconnect():
    session = FixSession("SESSION-1")
    assert session.state == 'disconnected'
    session.connect()
    assert session.state == 'connected'
    session.disconnect()
    assert session.state == 'disconnected'
