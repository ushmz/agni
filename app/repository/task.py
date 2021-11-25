from infra.mysql import get_connection
from domain.task import Answer, Task
from domain.repository.task import TaskRepository


class TaskRepositoryImpl(TaskRepository):
    def get_task_description(self, task_id: int) -> Task:
        """
        Get task information (title, descriptions, etc...)

        args:
            task_id(int) : Task id that you'd like to fetch
        returns:
            info(TaskInfo) : Information object
        """
        conn = get_connection()
        cur = conn.cursor(dictionary=True)

        try:
            cur.execute(
                "SELECT query, title, description, search_url"
                + " FROM tasks WHERE id = %s" % (task_id,)
            )
            rs = cur.fetchone()
            return rs
        except Exception as e:
            print(f"[ERROR] {e}")
            return Task()
        finally:
            cur.close()
            conn.close()

    def create_answer(self, answer: Answer) -> None:
        """
        Insert user's answer to DB

        args:
            answer(Answer) : User's task answer and reason
        returns:
            None
        """
        conn = get_connection()
        cur = conn.cursor()

        try:
            cur.execute(
                "INSERT INTO"
                + " answers(user_id, task_id, condition_id, answer, reason)"
                + " VALUES('%s', '%s', '%s', '%s', '%s')"
                % (
                    answer.user_id,
                    answer.task_id,
                    answer.condition_id,
                    answer.answer,
                    answer.reason,
                )
            )
        except Exception as e:
            print(f"[ERROR] {e}")
        else:
            conn.commit()
        finally:
            cur.close()
            conn.close()
