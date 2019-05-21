#
#
#

from database.retrieveQuery import retrieveBiggestIdFromTable
import datetime


def scanNodes(stationsIDs):
  list_of_tables = ['GroundNode', 'SinkNode', 'TenMeterNode', 'TwoMeterNode']
  for sID in stationsIDs:
    # sID[0]
    for table in list_of_tables:
      IDresult = retrieveBiggestIdFromTable(sID[0], table)
      print(IDresult)
      latest_secondsEpoch = IDresult[0][1]
      second_latest_secondsEpoch = IDresult[1][1]
      if len(latest_secondsEpoch) == 19 and len(second_latest_secondsEpoch) == 19:
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
      
      print(gap)
      #print(sID[0], table, IDresult, latest_secondsEpoch)
