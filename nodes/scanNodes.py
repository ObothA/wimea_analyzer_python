#
#
#

from database.retrieveQuery import retrieveBiggestIdFromTable

def scanNodes(stationsIDs):
    list_of_tables = ['GroundNode', 'SinkNode', 'TenMeterNode', 'TwoMeterNode']
    for sID in stationsIDs:
        # sID[0]
        for table in list_of_tables:
            IDresult  = retrieveBiggestIdFromTable(sID[0],table)
            print(sID, table, IDresult)

