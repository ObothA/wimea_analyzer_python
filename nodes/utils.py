
def analyseSeconds(gap,list_of_times, sID, table):
  #for @ station, @ node ------
  counter = 0
  while counter < len(list_of_times) - 1:
    difference = print(list_of_times[counter + 1]['time_in_seconds']) - print(list_of_times[counter]['time_in_seconds'])
    difference = round(difference)
    print(difference)
    counter = counter + 1
