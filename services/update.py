from repository.update import UpdateRepository


class UpdateService:
    def __init__(self):
        self.repository = UpdateRepository()

    def update(self):
        self.repository.update()