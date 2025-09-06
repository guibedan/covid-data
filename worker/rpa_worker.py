import schedule
from time import sleep
from services.update import UpdateService


def rpa_worker():
    print("[INFO] RPA Process", flush=True)
    service = UpdateService()
    service.update()

    schedule.every(1).week.do(service.update)

    while True:
        try:
            schedule.run_pending()
            sleep(1)
        except KeyboardInterrupt:
            print("[REPROCESS] Process interrupt for keyboard", flush=True)
            break
