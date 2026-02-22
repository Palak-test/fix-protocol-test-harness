
"""
Statistics and reporting for Fixit Protocol Test Harness.
"""
# stats.py for Fixit

def calculate_message_stats(messages):
    """Calculate statistics for a list of FIX messages (dicts)."""
    total = len(messages)
    types = {}
    for msg in messages:
        msg_type = msg.get('35') if isinstance(msg, dict) else None
        if msg_type:
            types[msg_type] = types.get(msg_type, 0) + 1
    return {'total': total, 'types': types}
