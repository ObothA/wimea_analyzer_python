
def analyseSeconds(gap,list_of_times, sID, table):
  #for @ station, @ node ------
  def sortFunc(object):
    # function to sort dictionaries based on seconds
    return object['time_in_seconds']

  #sort to avoid negatives during subtraction
  list_of_times.sort(reverse=True, key=sortFunc)

  clusters = [[61,1]]
  counter = 0
  while counter < len(list_of_times) - 1:
    difference = list_of_times[counter]['time_in_seconds'] - list_of_times[counter + 1]['time_in_seconds']
    difference = round(difference)
    #print(difference, list_of_times[counter]['rtc'], list_of_times[counter + 1]['rtc'])

    append = True
    for cluster in clusters:
      if difference == cluster[0]:
        cluster[1]  = cluster[1]+ 1
        append = False
    if append:
        clusters.append([difference,1])
    counter = counter + 1
  print(clusters)
  print()
