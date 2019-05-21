#
#
#
import datetime
from database.retrieveQuery import retrieveQuery
from nodes.scanNodes import scanNodes 

def stations():
  #scan stations for on/off status

  sql = "SELECT `station_id` FROM `stations` WHERE `station_id` = 54" #49
  stations_id_result = retrieveQuery(sql)
  result = stations_id_result[0]

  list_of_tables = ['GroundNode', 'SinkNode', 'TenMeterNode', 'TwoMeterNode']
  list_of_gaps = []
  list_of_largest = []

  for stationID in result:
    #print(stationID[0])
    list_of_latest_hours = []
    for table in list_of_tables:
      #print(stationID[0],table)
      sql = "select hoursSinceEpoch from " +table+ " where `stationID` = " +str(stationID[0])+ " ORDER BY id  DESC limit 1"
      hours_result = retrieveQuery(sql)
      if not hours_result[0]:
        resultH = 0
      else:
        resultH = hours_result[0][0][0]
      list_of_latest_hours.append(resultH)
    
    largest = 0
    for time in list_of_latest_hours:
      if time > largest:
        largest = time
    #get gap
    gap = datetime.datetime.now().timestamp() / 3600 - largest
    list_of_largest.append((stationID[0],largest))
    list_of_gaps.append((stationID[0],gap))

  #print(list_of_largest)
  #print()
  #print(list_of_gaps)

  #last time each station received data
  print('--=====####################################======----')
  print('                   STATIONS REPORT                    ')
  for station_tuple in list_of_gaps:
    print('station ' + str(station_tuple[0]) + ' last received data ' +str(station_tuple[1]) + ' hours back')
  print('--=====####################################======----')
  print()

  #######################
  #call next method to scan nodes 
  scanNodes(result)