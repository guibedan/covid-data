import os
import logging
from dotenv import load_dotenv
from worker.rpa_worker import rpa_worker
from worker.api_worker import api_worker


def main():
    load_dotenv()

    worker = os.getenv('WORKER')

    if worker == 'API':
        api_worker()
    elif worker == 'RPA':
        rpa_worker()
    else:
        logging.error('Invalid WORKER')
        exit(1)


if __name__ == "__main__":
    main()
