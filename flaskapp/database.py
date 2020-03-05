import sqlalchemy as db


class Database():
    engine = db.create_engine(
        'postgresql:///flask')

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")

    def fetchByQyery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM customer")

        for data in fetchQuery.fetchall():
            print(data)
