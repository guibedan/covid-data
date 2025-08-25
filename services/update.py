from services.brazil import BrazilService


class UpdateService:
    def __init__(self):
        self.brazil_service = BrazilService()

    def update(self):
        self.brazil_service.save_states_and_regions()