
def analyseSeconds(gap,list_of_times, sID, table):
  #for @ station, @ node ------
  counter = 0
  while counter < len(list_of_times) - 1:
    difference = list_of_times[counter + 1]['time_in_seconds'] - list_of_times[counter]['time_in_seconds']
    difference = round(difference)
    print(difference, list_of_times[counter + 1]['rtc'], list_of_times[counter]['rtc'])
    counter = counter + 1
