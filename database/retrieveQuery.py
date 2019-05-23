# from database.connection import connection
from database.connection import mydb

import datetime


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
  #limit RTC to length of 19 to avoid corrupt RTCs
  sqlStatement = "select id, RTC_T from " +table+ " where stationID = " +str(stationID)+ " and char_length(RTC_T)=19 ORDER BY id  DESC limit 1"
  cursor.execute(sqlStatement)
  result = cursor.fetchall()
  return result


def retrieveRTCforTrend(stationID, table, biggestId):
  cursor = mydb.cursor()
  sqlStatement = "select RTC_T from " +table+ " where stationID = " +str(stationID)+ " and id != " +str(biggestId)+ " and char_length(RTC_T)=19 ORDER BY id  DESC limit 1000"
  cursor.execute(sqlStatement)
  result = cursor.fetchall()
  return result


def retrieveStatus(id,problem):
  cursor = mydb.cursor()
  sqlStatement = " select status, id from DetectedAnalyzerProblems where stationID = " +str(id)+ " and Problem = '" + problem + "' and status != 'fixed'"
  cursor.execute(sqlStatement)
  result = cursor.fetchall()
  return result


#######
#SORRY THE FILE IS CALLED RETRIEVE QUERY BUT WE SHALL DO INSERET QUERIES IN HERE AS WELL
#######

def insertProblem(stationID, problem, status):
  cursor = mydb.cursor()
  sql = "INSERT INTO DetectedAnalyzerProblems (stationID, Problem, when_reported,status) VALUES (%s, %s, %s, %s)"
  time = datetime.datetime.now()
  val = (str(stationID), problem, str(time), status)
  cursor.execute(sql, val)

  mydb.commit()


  ######
  # UPDATE QUERY
  #####

def updateProblem(status, entryID):
  mycursor = mydb.cursor()
  sql = "UPDATE DetectedAnalyzerProblems SET status =" +status+  "WHERE id = " + str(entryID)

  mycursor.execute(sql)

  mydb.commit()



