from abc import ABCMeta, abstractmethod
from domain.log import ClickLog, TimeLog


class LogRepository(metaclass=ABCMeta):
    @abstractmethod
    def post_click_log(self, log: ClickLog) -> None:
        """
        Update click log in DB

        args:
            log(ClickLog) : Click log parameters
        returns:
            None
        """
        raise NotImplementedError(f"params: log={log}")

    @abstractmethod
    def post_time_log(self, log: TimeLog) -> None:
        """
        Update task time log in DB

        args:
            log(TimeLog) : Task time log parameters
        returns:
            None
        """
        raise NotImplementedError(f"params: log={log}")
