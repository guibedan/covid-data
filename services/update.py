from services.brazil import BrazilService


class UpdateService:
    def __init__(self):
        self.brazil_service = BrazilService()

    def update(self):
        print("[INFO] Update data", flush=True)
        self.brazil_service.save_states_and_regions()
        self.brazil_service.add_cities()
        print("[INFO] Update finished", flush=True)
