#########
# Generic function to report problems
########

from database.retrieveQuery import retrieveStatus

def reportProblemMethod(stationID, problem):
  result = retrieveStatus(stationID, problem)
  if len(result) is 0:
    print('no entry')
    #insert record
  else :
    print('entry found')
    status = result[0][0]
