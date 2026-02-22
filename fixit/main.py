# main.py for Fixit

from fixit.core import FixMessageParser
import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

if __name__ == "__main__":
    setup_logging()
    logging.info("Welcome to Fixit Protocol Test Harness!")
