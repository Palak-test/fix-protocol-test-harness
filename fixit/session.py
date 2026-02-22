# session.py for Fixit

class FixSession:
    """Basic FIX session handler."""
    def __init__(self, session_id, config=None):
        self.session_id = session_id
        self.state = 'disconnected'
        self.config = config or {}
        self.validate_config()

    def validate_config(self):
        # Example: require 'host' and 'port' in config
        required = ['host', 'port']
        for key in required:
            if key not in self.config:
                raise ValueError(f"Missing required config: {key}")

    def connect(self):
        self.state = 'connected'

    def disconnect(self):
        self.state = 'disconnected'
