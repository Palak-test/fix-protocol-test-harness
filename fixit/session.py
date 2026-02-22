class FixSessionManager:
    """Manages multiple FIX sessions."""
    def __init__(self):
        self.sessions = {}

    def add_session(self, session_id, config=None):
        session = FixSession(session_id, config)
        self.sessions[session_id] = session
        return session

    def get_session(self, session_id):
        return self.sessions.get(session_id)
# session.py for Fixit

class FixSession:
                def send_message(self, message):
                    """Simulate sending a FIX message."""
                    if self.state != 'connected':
                        raise RuntimeError('Session not connected')
                    # Placeholder for sending logic
                    return True
            def shutdown(self):
                """Gracefully shutdown the session."""
                if self.state == 'connected':
                    self.disconnect()
                # Additional cleanup logic can be added here
        def get_state(self):
            """Return the current session state."""
            return self.state
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

    def connect(self, retries=3):
        attempt = 0
        while attempt < retries:
            try:
                # Simulate connection logic
                self.state = 'connected'
                return True
            except Exception:
                attempt += 1
        self.state = 'disconnected'
        return False

    def disconnect(self):
        self.state = 'disconnected'
