import sqlite3
import logging
from pathlib import Path
from contextlib import contextmanager
from config import DATABASE_PATH
from .schema import create_schema

logger = logging.getLogger(__name__)


class DatabaseConnection:
    _instance = None
    _connection = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._connection is None:
            self._connect()

    def _connect(self):
        try:
            DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
            self._connection = sqlite3.connect(
                str(DATABASE_PATH),
                check_same_thread=False,
                timeout=30
            )
            self._connection.row_factory = sqlite3.Row
            self._connection.execute("PRAGMA foreign_keys = ON")
            logger.info(f"Database connection established at {DATABASE_PATH}")
        except sqlite3.Error as e:
            logger.error(f"Database connection failed: {str(e)}")
            raise

    @contextmanager
    def get_cursor(self):
        try:
            cursor = self._connection.cursor()
            yield cursor
            self._connection.commit()
        except sqlite3.Error as e:
            self._connection.rollback()
            logger.error(f"Database error: {str(e)}")
            raise
        finally:
            cursor.close()

    def execute(self, query, params=None):
        with self.get_cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor

    def fetchone(self, query, params=None):
        with self.get_cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()

    def fetchall(self, query, params=None):
        with self.get_cursor() as cursor:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchall()

    def close(self):
        if self._connection:
            self._connection.close()
            logger.info("Database connection closed")


def get_db_connection():
    return DatabaseConnection()


def init_database():
    try:
        db = get_db_connection()
        create_schema(db)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {str(e)}")
        raise