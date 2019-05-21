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
      latest_secondsEpoch = IDresult[0][1]
      if len('2019-02-21,17:53:16') == 19:
        latest_secondsEpoch = datetime.datetime.strptime(latest_secondsEpoch, '%Y-%m-%d,%H:%M:%S')
      else:
        latest_secondsEpoch = 0
      print(sID[0], table, IDresult, latest_secondsEpoch)
