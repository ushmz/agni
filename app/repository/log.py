from domain.log import ClickLog, TimeLog
from domain.repository.log import LogRepository


class LogRepositoryImple(LogRepository):
    def post_click_log(self, log: ClickLog) -> None:
        """
        Update click log in DB

        args:
            log(ClickLog) : Click log parameters
        returns:
            None
        """
        raise NotImplementedError(f"params: log={log}")

    def post_time_log(self, log: TimeLog) -> None:
        """
        Update task time log in DB

        args:
            log(TimeLog) : Task time log parameters
        returns:
            None
        """
        raise NotImplementedError(f"params: log={log}")
