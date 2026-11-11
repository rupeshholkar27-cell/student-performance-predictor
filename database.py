import sqlite3
import pandas as pd
from logger_config import get_logger

logger = get_logger("database")


class Database:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        conn = self._connect()
        try:
            with conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        study_hours REAL,
                        attendance REAL,
                        internal1 REAL,
                        internal2 REAL,
                        assignment REAL,
                        semester_score REAL
                    )
                """)
        finally:
            conn.close()

    def add_student(self, student):
        conn = self._connect()
        try:
            with conn:
                conn.execute(
                    "INSERT INTO students (name, study_hours, attendance, "
                    "internal1, internal2, assignment, semester_score) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    student.to_tuple()
                )
            logger.info(f"Added student: {student.name}")
        except sqlite3.Error as e:
            logger.error(f"Database error while adding student: {e}")
            raise
        finally:
            conn.close()

    def load_csv(self, path):
        df = pd.read_csv(path)
        conn = self._connect()
        try:
            df.to_sql("students", conn, if_exists="append", index=False)
        finally:
            conn.close()
        logger.info(f"Loaded {len(df)} rows from {path}")

    def get_all(self):
        conn = self._connect()
        try:
            return pd.read_sql("SELECT * FROM students", conn)
        finally:
            conn.close()