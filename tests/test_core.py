# test_core.py for Fixit
import pytest
from fixit.core import FixMessageParser

def test_parser_returns_dict():
    parser = FixMessageParser()
    result = parser.parse("8=FIX.4.2|9=12|35=A|49=CLIENT|56=SERVER|10=123|")
    assert isinstance(result, dict)
