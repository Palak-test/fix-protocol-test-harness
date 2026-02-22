
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

def export_stats_to_csv(stats, filename):
    """Export statistics dictionary to a CSV file."""
    import csv
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Type', 'Count'])
        for msg_type, count in stats.get('types', {}).items():
            writer.writerow([msg_type, count])
        writer.writerow(['Total', stats.get('total', 0)])
