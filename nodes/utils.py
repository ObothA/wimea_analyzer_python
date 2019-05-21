
def analyseSeconds(gap,list_of_times, sID, table):
  #for @ station, @ node ------
  var counter = 0
  while counter < len(list_of_times) - 1:
    print(list_of_times[counter]['time_in_seconds'])
    counter = counter + 1
