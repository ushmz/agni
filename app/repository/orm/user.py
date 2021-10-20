from domain.models.completion_codes import CompletionCodes
from infra.alchemy import session_scope
from domain.models.users import User
from domain.repository.user import UserRepository


class UserRepositoryImpl(UserRepository):
    def create_user(self, user: User) -> User:
        with session_scope() as session:
            session.add(user)
        return user

    def get_user(self, user_id: int) -> User:
        with session_scope() as session:
            user: User = session.query(User).filter(User.id == user_id).first()
        return user

    def set_completion_code(self, code: CompletionCodes) -> CompletionCodes:
        with session_scope() as session:
            session.add(code)
        return code

    def get_completion_code(self, user_id: int) -> int:
        with session_scope() as session:
            code: CompletionCodes = (
                session.query(CompletionCodes)
                .filter(CompletionCodes.user_id == user_id)
                .first()
            )
        return code.completion_code
