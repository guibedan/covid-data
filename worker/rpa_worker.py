import schedule
from time import sleep
from data.loadData import load, update

load()


def rpa_worker():
    print("[INFO] RPA Process", flush=True)
    # schedule.every(1).week.do(update)
    schedule.every(5).minute.do(update)

    while True:
        try:
            schedule.run_pending()
            sleep(1)
        except KeyboardInterrupt:
            print("[REPROCESS] Process interrupt for keyboard", flush=True)
            break
