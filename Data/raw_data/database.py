from sqlalchemy import create_engine
import pandas as pd


class Database:

    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)


    def read_query(self, query):

        df = pd.read_sql(
            query,
            self.engine
        )

        return df