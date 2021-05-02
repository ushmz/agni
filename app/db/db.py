import configparser
from pymysql import connect


def conn():
    _parser = configparser.ConfigParser()
    _parser.read("./config.ini")

    return connect(
        host=_parser["mysql"]["host"],
        port=_parser["mysql"]["port"],
        user=_parser["mysql"]["user"],
        password=_parser["mysql"]["password"],
        database=_parser["mysql"]["database"],
    )
