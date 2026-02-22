# session.py for Fixit

class FixSession:
    """Basic FIX session handler."""
    def __init__(self, session_id):
        self.session_id = session_id
        self.state = 'disconnected'

    def connect(self):
        self.state = 'connected'

    def disconnect(self):
        self.state = 'disconnected'
