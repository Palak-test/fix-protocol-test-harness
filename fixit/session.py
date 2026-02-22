
"""
Session management for Fixit Protocol Test Harness.
"""
class FixSessionManager:
                def __init__(self):
                    self.sessions = {}
                    self.features = {}
                def enable_feature(self, feature_name):
                    self.features[feature_name] = True

                def disable_feature(self, feature_name):
                    self.features[feature_name] = False

                def is_feature_enabled(self, feature_name):
                    return self.features.get(feature_name, False)
            def reload_config(self, session_id, new_config):
                """Reload configuration for a session without restart."""
                session = self.get_session(session_id)
                if not session:
                    raise ValueError('Session not found')
                session.config = new_config
                session.validate_config()
        def replay_messages(self, session_id, messages):
            """Simulate replaying a list of messages to a session."""
            session = self.get_session(session_id)
            if not session:
                raise ValueError('Session not found')
            for msg in messages:
                session.send_message(msg)
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
                                        def set_protocol_version(self, version="FIX.4.2"):
                                            """Set the FIX protocol version for the session."""
                                            self.protocol_version = version
                                    def handle_admin_message(self, message):
                                        """Handle admin-level FIX messages (e.g., logon, logout, heartbeat)."""
                                        msg_type = None
                                        if isinstance(message, dict):
                                            msg_type = message.get('35')
                                        if msg_type in ['A', '5', '0']:
                                            # Logon (A), Logout (5), Heartbeat (0)
                                            return f"Handled admin message type: {msg_type}"
                                        return "Not an admin message"
                                def send_heartbeat(self):
                                    """Simulate sending a FIX heartbeat message."""
                                    if self.state != 'connected':
                                        raise RuntimeError('Session not connected')
                                    heartbeat_msg = "8=FIX.4.2|9=5|35=0|49=CLIENT|56=SERVER|10=000|"
                                    self.send_message(heartbeat_msg)
                                    return heartbeat_msg
                            def enable_encryption(self, enabled=True):
                                """Enable or disable encryption for the session (placeholder)."""
                                self.encryption_enabled = enabled
                        def log_message(self, message, log_file="fixit_messages.log"):
                            """Log a FIX message to a file."""
                            with open(log_file, "a") as f:
                                f.write(message + "\n")
                    def receive_message(self, raw_message):
                        """Simulate receiving a FIX message."""
                        if self.state != 'connected':
                            raise RuntimeError('Session not connected')
                        # Placeholder for receiving logic
                        return raw_message
                def send_message(self, message):
                    """Simulate sending a FIX message."""
                    self._ensure_connected()
                    # Placeholder for sending logic
                    return True

                def _ensure_connected(self):
                    if self.state != 'connected':
                        raise RuntimeError('Session not connected')
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
    def __init__(self, session_id, config=None):
        self.session_id = session_id
        self.state = 'disconnected'
        self.config = config or {}
        self.validate_config()
        self.in_seq_num = 1
        self.out_seq_num = 1
    def next_out_seq(self):
        self.out_seq_num += 1
        return self.out_seq_num

    def next_in_seq(self):
        self.in_seq_num += 1
        return self.in_seq_num

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
