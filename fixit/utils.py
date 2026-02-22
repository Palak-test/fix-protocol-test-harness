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
