## Usage Examples

Run the CLI:

	python -m fixit.main --config config.yaml

Parse a FIX message:

	from fixit.core import FixMessageParser
	parser = FixMessageParser()
	msg = parser.parse("8=FIX.4.2|9=12|35=A|49=CLIENT|56=SERVER|10=123|")
	print(msg)
# Fixit Protocol Test Harness

A custom-built tool for testing and simulating FIX protocol sessions.

## Features
- Modular design
- Easy configuration
- Extensible for custom FIX scenarios

---

*Project initialized*