#
#
#

from database.retrieveQuery import retrieveBiggestIdFromTable
from database.retrieveQuery import retrieveRTCforTrend
import datetime
import statistics



def scanNodes(stationsIDs):
  list_of_tables = ['GroundNode', 'SinkNode', 'TenMeterNode', 'TwoMeterNode']
  for sID in stationsIDs:
    # sID[0]
    for table in list_of_tables:
      IDresult = retrieveBiggestIdFromTable(sID[0], table)
      #print(IDresult)
      if len(IDresult) is not 0: 
        latest_RTC = IDresult[0][1]
        if latest_RTC is not None and len(latest_RTC) == 19:
          latest_RTC = datetime.datetime.strptime(latest_RTC, '%Y-%m-%d,%H:%M:%S')
          latest_RTC = latest_RTC.timestamp()
          now = datetime.datetime.now().timestamp()
          gap = now - latest_RTC
        else:
          # corrupt data detected, no problem will be reported
          latest_RTC = 0
          gap = 'not calculated, corrupt data'

        #print(sID[0],gap)
        result_for_trend = retrieveRTCforTrend(sID[0], table, IDresult[0][0])
        #print(result_for_trend)
        list_of_times = []
        for rtc in result_for_trend:
          if rtc[0] is not None and len(rtc[0]) == 19:
            time = datetime.datetime.strptime(rtc[0], '%Y-%m-%d,%H:%M:%S')
            list_of_times.append(time.timestamp())
        print(sID,table,list_of_times)
