"""
An example script to connect to the COSMIC VLA database
make SQL queries 
"""
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine("mysql+pymysql://user:password@Host:port/database-name", echo = True)

# Test the connection
connection = engine.connect()
#connection.execute("select @@version")
#print(connection.table_names)

comm = "SELECT * FROM cosmic_observation_stamp LIMIT 10"
result = connection.execute(comm)

for row in result:
    print(row)
