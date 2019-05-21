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
  sqlStatement = "select id, RTC_T from " +table+ " where stationID = " +str(stationID)+ " ORDER BY id  DESC limit 1"
  cursor.execute(sqlStatement)
  result = cursor.fetchall()
  return result


def retrieveRTCforTrend(stationID, table, biggestId):
  cursor = mydb.cursor()
  sqlStatement = "select RTC_T from " +table+ " where stationID = " +str(stationID)+ " and id != " +str(biggestId)+ " ORDER BY id  DESC limit 500"
  cursor.execute(sqlStatement)
  result = cursor.fetchall()
  return result


