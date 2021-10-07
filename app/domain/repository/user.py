from abc import ABCMeta, abstractmethod
from domain.user import UserParam, UserSimple


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self, user: UserParam) -> UserSimple:
        """
        Create user.

        args:
            user_id(int) : User ID that you'd like to get
        returns:
            user(UserSimple) : Simple user information
        """
        raise NotImplementedError(f"params: user={user}")

    @abstractmethod
    def get_user(self, user_id: int) -> str:
        """
        Get user's completion code from DB.

        args:
            user_id(int) : User ID that you'd like to get
        returns:
            completion_code(str) : Completion code
        """
        raise NotImplementedError(f"params: user_id={user_id}")

    @abstractmethod
    def get_completion_code(self, user_id: int) -> str:
        """
        Get user's completion code from DB.

        args:
            user_id(int) : User ID that you'd like to get
        returns:
            completion_code(str) : Completion code
        """
        raise NotImplementedError(f"params: user_id={user_id}")
