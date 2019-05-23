#########
# Generic function to report problems
########

from database.retrieveQuery import retrieveStatus
from database.retrieveQuery import insertProblem

def reportProblemMethod(stationID, problem):
  result = retrieveStatus(stationID, problem)
  if len(result) is 0:
    print('no entry')
    insertProblem(stationID,problem)
  else :
    print('entry found')
    status = result[0][0]
    print(status)
