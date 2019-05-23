#########
# Generic function to report problems
########

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
    if status is 'reported':
      updateProblem('re-reported', entry_id)
