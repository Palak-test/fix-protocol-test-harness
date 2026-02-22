# test_session.py for Fixit
from fixit.session import FixSession

def test_session_connect_disconnect():
    session = FixSession("SESSION-1")
    assert session.state == 'disconnected'
    session.connect()
    assert session.state == 'connected'
    session.disconnect()
    assert session.state == 'disconnected'
