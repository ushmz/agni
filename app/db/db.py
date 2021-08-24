import configparser
import mysql.connector as db
from typing import Any, List

from models.task import Serp, TaskInfo
from models.log import BehaviorLog


def get_connection():
    _parser = configparser.ConfigParser()
    _parser.read("./config.ini")

    return db.connect(
        host=_parser["mysql"]["host"],
        port=_parser["mysql"]["port"],
        user=_parser["mysql"]["user"],
        password=_parser["mysql"]["password"],
        database=_parser["mysql"]["database"],
    )


@DeprecationWarning
def exec_query(query: str, **params) -> Any:
    """
    This is multi-purpose function to execute query and get result.
    Using this method, it is difficult to
        - judge which is better `fetchone` or `fetchall`
        - handle custom error
    Thus, this method is NOT recommended.

    args:
        query(str) : Query string, which can contein format char '?'
        params     : Parameters, which is used in format
    returns:
        result     : Query result
    """
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    try:
        cur.execute(query, params)
        result = cur.fetchall()
        return result
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        cur.close()
        conn.close()


def get_completion_code(user_id: int) -> str:
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
    except Exception as e:
        print(f"[ERROR] {e}")
        return ""
    finally:
        cur.close()
        connection.close()


def get_task_info(task_id: int) -> TaskInfo:
    """
    Get task information, like title, descriptions, etc...

    args:
        task_id(int) : Task id that you'd like to fetch
    returns:
        info(TaskInfo) : Information object
    """
    raise NotImplementedError(f"params: task_id={task_id}")


def get_serp(task_id: int) -> List[Serp]:
    """
    Get search result pages by given task INIT_DB

    args:
        task_id(int) : Task ID
    returns:
        serps(List[Serp]) : Listed result page objects
    """
    raise NotImplementedError(f"params: task_id={task_id}")


def create_log(behavior: BehaviorLog) -> None:
    """
    Create behavior log object and insert it to DB

    args:
        behavior(BehaviorLog) : Behavior log parameters
    returns:
        None
    """
    raise NotImplementedError(f"params: behavior={behavior}")


def create_answer(answer: str) -> None:
    """
    Insert user's answer to DB

    args:
        answer(str) : User's task answer
    returns:
        None
    """
    raise NotImplementedError(f"params: answer={answer}")
