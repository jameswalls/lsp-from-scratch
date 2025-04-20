import logging
import os
import sys

LOG_DIR = os.path.expanduser("~/projects/lsp_from_scratch/logs")

def get_logger(filename: str) -> logging.Logger:
    # Create logs directory if it doesn't exist
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Configure logging to write to a file
    logging.basicConfig(
        filename=os.path.join(LOG_DIR, filename),
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(filename)

    return logger


def handle_message(logger: logging.Logger, msg: str):
    # Implementation of message handling will go here
    logger.info(f"Received message: {msg}")
    pass


def main():
    print("Hello, World!")

    logger = get_logger("lsp.log")
    logger.info("Hey I started!")

    for line in sys.stdin:
        msg = line.strip()
        handle_message(logger, msg)

if __name__ == "__main__":
    main()
