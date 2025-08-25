import os
import logging
from dotenv import load_dotenv
from worker.rpa_worker import rpa_worker
from worker.api_worker import api_worker


def main():
    load_dotenv()
    if os.getenv('WORKER') == 'API':
        rpa_worker()
    elif os.getenv('WORKER') == 'RPA':
        api_worker()
    else:
        logging.error('Invalid WORKER')
        exit(1)


if __name__ == "__main__":
    main()
