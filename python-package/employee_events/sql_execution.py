from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
#### YOUR CODE HERE

# OPTION 1: MIXIN
# Define a class called `QueryMixin`
class QueryMixin:
    def __int__(self):
        self.db_path = Path(__file__).resolve().parent / "employee_events.db"
        
    # Define a method named `pandas_query`
    # that receives an sql query as a string
    # and returns the query's result
    # as a pandas dataframe
    #### YOUR CODE HERE
    def pandas_query(self, sql_query):
        connection = connect(self.db_path)
        return pd.read_sql_query(sql_query, connection)

    # Define a method named `query`
    # that receives an sql_query as a string
    # and returns the query's result as
    # a list of tuples. (You will need
    # to use an sqlite3 cursor)
    #### YOUR CODE HERE
    def query(self, sql_query):
        connection = connect(self.db_path)
        cursor = connection.cursor()    
        return cursor.execute(sql_query).fetchall()   
        
 # Leave this code unchanged
def query(func):
    """
    Decorator that runs a standard sql execution
    and returns a list of tuples
    """

    @wraps(func)
    def run_query(*args, **kwargs):
        query_string = func(*args, **kwargs)
        connection = connect(self.db_path)
        cursor = connection.cursor()
        result = cursor.execute(query_string).fetchall()
        connection.close()
        return result
    
    return run_query
