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
      print(IDresult)
      latest_secondsEpoch = IDresult[0][1]
      second_latest_secondsEpoch = IDresult[1][1]
      if latest_secondsEpoch is not None and len(latest_secondsEpoch) == 19  and second_latest_secondsEpoch is not None and len(second_latest_secondsEpoch) == 19:
        latest_secondsEpoch = datetime.datetime.strptime(latest_secondsEpoch, '%Y-%m-%d,%H:%M:%S')
        second_latest_secondsEpoch = datetime.datetime.strptime(second_latest_secondsEpoch, '%Y-%m-%d,%H:%M:%S')
        latest_secondsEpoch = latest_secondsEpoch.timestamp()
        second_latest_secondsEpoch = second_latest_secondsEpoch.timestamp()
        gap = latest_secondsEpoch - latest_secondsEpoch
      else:
        # corrupt data detected, no problem will be reported
        latest_secondsEpoch = 0
        second_latest_secondsEpoch = 0
        gap = 'not calculated, corrupt data'

      result_for_trend = retrieveRTCforTrend(sID[0], table, IDresult[0][0])
      #print(result_for_trend)
      list_of_times = []
      for rtc in result_for_trend:
        if rtc[0] is not None and len(rtc[0]) == 19:
          time = datetime.datetime.strptime(rtc[0], '%Y-%m-%d,%H:%M:%S')
          list_of_times.append(time.timestamp())
      
      mean_of_times = statistics.mean(list_of_times)
      magnitude = mean_of_times * 10
      if type(gap) is str:
        report = 'corrupt rtc somewhere, not calculated'
      elif gap >  magnitude:
        report = '***OFF'
      elif gap < magnitude :
        report = 'ON'

      print('station ' +str(sID[0])+ ', ' + table + '   ' + report)
