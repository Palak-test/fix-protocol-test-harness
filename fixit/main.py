try:
    from colorama import Fore, Style, init as colorama_init
    colorama_init()
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
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
    if COLORAMA_AVAILABLE:
        print(Fore.GREEN + "Welcome to Fixit Protocol Test Harness!" + Style.RESET_ALL)
    else:
        print("Welcome to Fixit Protocol Test Harness!")
    if args.config:
        logging.info(f"Using config file: {args.config}")
