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

def retrieveBiggestIdFromTable(stationID,table):
  ############################################
  cursor = mydb.cursor()
  sqlStatement = "select id, RTC_T from " +table+ " where stationID = " +stationID+ " "
  cursor.execute(sqlStatement)
  result = cursor.fetchall()
  return result

