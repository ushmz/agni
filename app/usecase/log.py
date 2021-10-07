from repository.log import LogRepositoryImple
from domain.log import ClickLog, TimeLog
from domain.repository.log import LogRepository


class LogUsecase:
    def __init__(self, repository: LogRepository = LogRepositoryImple()) -> None:
        self.repository = repository

    def post_click_log(self, log: ClickLog):
        self.post_click_log(log)
        return

    def post_time_log(self, log: TimeLog):
        self.post_time_log(log)
        return
