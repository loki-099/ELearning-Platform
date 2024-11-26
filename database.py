import pyodbc

class Database:
    """Database class to handle connections and queries."""

    def __init__(self, server, database, driver="ODBC Driver 17 for SQL Server"):
        self.server = server
        self.database = database
        self.driver = driver
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = pyodbc.connect(
                f"DRIVER={{{self.driver}}};"
                f"SERVER={self.server};"
                f"DATABASE={self.database};"
                f"Trusted_Connection=yes;"
            )
            return self.connection
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    def execute_query(self, query, params=None, fetch_all=True):
        """
        Execute a SQL query.

        :param query: SQL query string.
        :param params: Parameters for the query.
        :param fetch_all: Fetch all rows if True, fetch one if False.
        :return: Query results or affected row count.
        """
        if not self.connection:
            self.connect()
        
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if query.strip().lower().startswith("select"):
                return cursor.fetchall() if fetch_all else cursor.fetchone()
            else:
                self.connection.commit()
                return cursor.rowcount  # Rows affected
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None
