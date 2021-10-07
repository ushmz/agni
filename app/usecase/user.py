from domain.user import UserParam, UserSimple
from domain.repository.user import UserRepository


class UserUsecase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, param: UserParam) -> UserSimple:
        user = self.repository.create_user(param)
        return user

    def get_user(self, user_id: int) -> str:
        user = self.repository.get_user(user_id)
        return user

    def get_completion_code(self, user_id: int) -> str:
        code = self.repository.get_completion_code(user_id)
        return code
