import psycopg2
import os


class PostgresDatabase:
    def __init__(self):
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT", "5432")

    def get_connection(self):
        return psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def execute(self, query, data=None):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, data)
            conn.commit()
            cursor.close()
            conn.close()
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()

    def get(self, query, data=None):
        conn = self.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query, data)
                result = cursor.fetchall()
                return result
        except psycopg2.Error as e:
            print(f"Error executing query: {e}")
        finally:
            conn.close()
