from domain.models.completion_codes import CompletionCodes
from domain.models.users import User
from domain.user import UserParam, UserSimple
from repository.orm.user import UserRepositoryImpl

from icecream import ic


class UserUsecase:
    def __init__(self, repository: UserRepositoryImpl) -> None:
        self.repository = repository

    def create_user(self, param: UserParam) -> UserSimple:
        nu = User(external_id=param.external_id)
        user = self.repository.create_user(nu)
        # [TODO] Allocate condition(s)
        # [TODO] Allocate task(s)
        return UserSimple.parse_obj(
            {
                "id": user.id,
                "external_id": user.external_id,
                "condition": 5,
                "tasks": [1, 2],
            }
        )

    def get_user(self, user_id: int) -> UserSimple:
        user = self.repository.get_user(user_id)
        ic(user)
        return UserSimple.parse_obj(
            {
                "id": user.id,
                "external_id": user.external_id,
                "condition": 5,
                "tasks": [1, 2],
            }
        )

    def set_completion_code(self, user_id: int, code: int) -> str:
        nc = CompletionCodes(user_id=user_id, completion_code=code)
        code = self.repository.set_completion_code(nc)
        return code

    def get_completion_code(self, user_id: int) -> int:
        code = self.repository.get_completion_code(user_id)
        return code
