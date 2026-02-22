# main.py for Fixit

from fixit.core import FixMessageParser

import logging
import argparse

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def parse_args():
    parser = argparse.ArgumentParser(description="Fixit Protocol Test Harness")
    parser.add_argument('--config', type=str, help='Path to config file')
    return parser.parse_args()

if __name__ == "__main__":
    setup_logging()
    args = parse_args()
    logging.info("Welcome to Fixit Protocol Test Harness!")
    if args.config:
        logging.info(f"Using config file: {args.config}")
