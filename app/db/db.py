import configparser
import mysql.connector as db
from typing import Any


def get_env(key: str, default: str) -> str:
    _parser = configparser.ConfigParser()
    _parser.read("./config.ini")
    val = _parser[key]
    return str(val) if val else default


def get_mysql_connection():
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
    conn = get_mysql_connection()
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
