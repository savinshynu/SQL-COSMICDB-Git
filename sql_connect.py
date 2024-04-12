"""
- Connecting to cosmic database with pymysql
- read data from COSMIC SQL database using python
"""

import pymysql 
  
def mysqlconnect(): 
    # To connect MySQL database 
    conn = pymysql.connect( 
        host='', 
        user='',  
        password = '', 
        db='', 
        ) 
      
    cur = conn.cursor() 
    #cur.execute("select @@version") 
    #cur.execute("SELECT * FROM ObservationStamp WHERE source_name LIKE '3C%' LIMIT 10")
    #sql = "SHOW tables"
    comm = "SELECT * FROM cosmic_observation_stamp LIMIT 10"
    cur.execute(comm)
    output = cur.fetchall() 
    for x in output:
        print(x)
      
    # To close the connection 
    conn.close() 
  
# Driver Code 
if __name__ == "__main__" : 
    mysqlconnect()
