from infra.mysql import get_connection
from domain.repository.user import UserRepository
from domain.user import UserParam, UserSimple


class UserRepositoryImpl(UserRepository):
    def create_user(self, params: UserParam) -> UserSimple:
        """
        Create user.

        args:
            params(UserParam) : User parameter for creation
        returns:
            user(UserSimple) : Simple user information
        """
        connection = get_connection()
        cur = connection.cursor(dictionary=True)

        try:
            cur.execute(
                """
                INSERT INTO
                    user
                VALUES(
                    ?
                )
                """,
                params.external_id,
            )

            res = cur.fetchall()

            return res[-1]
        except Exception:
            raise
        finally:
            cur.close()
            connection.close()

    def get_user(self, user_id: int) -> UserSimple:
        """
        Get user's completion code from DB.

        args:
            user_id(int) : User ID that you'd like to get
        returns:
            user(UserSimple) : User information
        """
        connection = get_connection()
        cur = connection.cursor(dictionary=True)

        try:
            cur.execute(
                """
                SELECT
                    completion_code
                FROM
                    completion_codes
                RIGHT JOIN
                    users
                ON
                    users.id = completion_codes.uid
                WHERE
                    users.id = ?
                """,
                user_id,
            )

            res = cur.fetchall()

            if len(res) != 1:
                print("[WARNING] User Id duplication is detected!!")

            return res[-1]["completion_code"]
        except Exception:
            raise
        finally:
            cur.close()
            connection.close()

    def get_completion_code(self, user_id: int) -> str:
        """
        Get user's completion code from DB.

        args:
            user_id(int) : User ID that you'd like to get
        returns:
            completion_code(str) : Completion code
        """
        connection = get_connection()
        cur = connection.cursor(dictionary=True)

        try:
            cur.execute(
                """
                SELECT
                    completion_code
                FROM
                    completion_codes
                RIGHT JOIN
                    users
                ON
                    users.id = completion_codes.uid
                WHERE
                    users.id = ?
                """,
                user_id,
            )

            res = cur.fetchall()

            if len(res) != 1:
                print("[WARNING] User Id duplication is detected!!")

            return res[-1]["completion_code"]
        except Exception:
            raise
        finally:
            cur.close()
            connection.close()
