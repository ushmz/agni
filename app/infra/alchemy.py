import configparser
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_env(key: str, default: str) -> str:
    """
    Get environment variable from `.ini` file.
    Filename is specified (./config.ini).
    If given key does not have valid value, return default.

    args:
        key(str) : Key of environment value that you want.
        default(str) : In case of given key doesn't have valid value.
    return:
        value(str) : Environment variable or default value.
    """
    _parser = configparser.ConfigParser()
    _parser.read("./config.ini")
    val = _parser["DEFAULT"][key]
    return str(val) if val else default


__ENGINE = get_env("engine", "mysql")
__USER = get_env("user", "agni")
__PASSWORD = get_env("password", "agni")
__HOST = get_env("host", "0.0.0.0")
__PORT = get_env("port", "3306")
__DB_NAME = get_env("database", "agni")

__DATABASE = "%s+mysqlconnector://%s:%s@%s:%s/%s?charset=utf8" % (
    __ENGINE,
    __USER,
    __PASSWORD,
    __HOST,
    __PORT,
    __DB_NAME,
)


Base = declarative_base()


@contextmanager
def session_scope():
    """
    Get SQLAlchemy session object
    """
    engine = create_engine(__DATABASE, encoding="utf-8", echo=True)
    Session = sessionmaker(
        bind=engine,
        autocommit=False,
        # autoflush=False,
        expire_on_commit=False,
    )
    session = Session()

    try:
        yield session
        session.commit()
    except Exception as exc:
        session.rollback()
        raise exc
    finally:
        session.close()
