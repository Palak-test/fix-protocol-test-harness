def pretty_print_message(message_dict):
	"""Return a human-readable string for a FIX message dict."""
	if not isinstance(message_dict, dict):
		return str(message_dict)
	return '\n'.join(f"{k}: {v}" for k, v in message_dict.items())
def pretty_print_message(message_dict):
	"""Return a human-readable string for a FIX message dict."""
	if not isinstance(message_dict, dict):
		return str(message_dict)
	return '\n'.join(f"{k}: {v}" for k, v in message_dict.items())
def filter_messages(messages, msg_type):
	"""Return only messages of a given type (tag 35)."""
	filtered = []
	for msg in messages:
		if isinstance(msg, dict) and msg.get('35') == msg_type:
			filtered.append(msg)
	return filtered
# Fixit: Utilities

import yaml
import json

def load_config(path):
	"""Load configuration from YAML or JSON file."""
	if path.endswith('.yaml') or path.endswith('.yml'):
		with open(path, 'r') as f:
			return yaml.safe_load(f)
	elif path.endswith('.json'):
		with open(path, 'r') as f:
			return json.load(f)
	else:
		raise ValueError('Unsupported config file format')
