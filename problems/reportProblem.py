#########
# Generic function to report problems
########

import datetime

from database.retrieveQuery import retrieveStatus
from database.retrieveQuery import insertProblem
from database.retrieveQuery import updateProblem

def reportProblemMethod(stationID, problem):
  result = retrieveStatus(stationID, problem)
  if len(result) is 0:
    print('no entry')
    insertProblem(stationID, problem, 'reported')
  else :
    status = result[0][0]
    entry_id = result[0][1]
    time_reported = result[0][2]
    # get time since epoch, [0;19] slices upto 19th index of string to fit strp requirements
    time_reported = datetime.datetime.strptime(str(time_reported)[0:19], '%Y-%m-%d %H:%M:%S').timestamp()

    if status == 'reported':
      updateProblem('re-reported', entry_id)

    if status == 're-reported':
      current_time = datetime.datetime.now().timestamp()
      gap = (current_time - time_reported)/ 3600
      print(gap)
      if(gap > 0.01):
        updateProblem('persistent', entry_id)


      
      
