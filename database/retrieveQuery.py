# from database.connection import connection
from database.connection import mydb


def retrieveQuery(sql):
  cursor = mydb.cursor()
  # Read records
  cursor.execute(sql)
  result = cursor.fetchall()
  #result = cursor.fetchone()
  # finally:
  # connection.close()
  return [result]