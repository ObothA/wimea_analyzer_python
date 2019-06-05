import datetime
import copy

from problems.reportProblem import reportProblemMethod
from database.retrieveQuery import insertIntoChangeTracker
from database.retrieveQuery import ReportIntervalClusters
from problems.reportProblem import check_if_problem_existed
 

def analyseSeconds(gap,list_of_times, sID, table):
  #for @ station, @ node ------
  def sortFunc(object):
    # function to sort dictionaries based on seconds
    return object['time_in_seconds']

  #sort to avoid negatives during subtraction
  list_of_times.sort(reverse=True, key=sortFunc)

  #clusters = [[61,1]]
  clusters = []
  counter = 0
  previous_difference = 0
  while counter < len(list_of_times) - 1:
    difference = list_of_times[counter]['time_in_seconds'] - list_of_times[counter + 1]['time_in_seconds']
    difference = difference / 60
    difference = round(difference)
    
    #change tracker
    if previous_difference is not 0 and difference >= 1:
      if difference > previous_difference:
        time_of_running_analyzer = datetime.datetime.now()
        change = ' from ' + str(previous_difference) + ' to '+ str(difference)
        time_range = 'between' + list_of_times[counter + 1]['rtc'] +' and '+list_of_times[counter]['rtc']
        # print(sID[0], table, list_of_times[counter + 1]['rtc'] +' => '+list_of_times[counter]['rtc'] + ' from ' + str(previous_difference) + ' to '+ str(difference))   
        insertIntoChangeTracker(sID[0], time_of_running_analyzer, table, change, time_range)
        previous_difference = difference
      elif previous_difference < difference:
        previous_difference = difference
    elif previous_difference is 0 and difference >= 1:
      previous_difference = difference

    if difference >= 1:
      append = True
      for cluster in clusters:
        if difference == cluster[0]:
          cluster[1]  = cluster[1] + 1
          append = False
      if append:
          clusters.append([difference,1])
    counter = counter + 1
  
  # sort the clusters
  def sortClusters(cluster):
    # function to sort clusters based on frequencies in the clusters
    return cluster[1]

  #sort to avoid negatives during subtraction
  clusters.sort(reverse=True, key=sortClusters)

  most_occuring_difference = clusters[0][0]
  magnitude = most_occuring_difference * 10000
  if type(gap) is int or type(gap) is float:
    gap = round(gap)
    if gap > magnitude:
      node_status = 'off'
      reportProblemMethod(sID[0], table + '_' + node_status)
    elif gap < magnitude:
      node_status = 'on'
      check_if_problem_existed(sID[0], table + '_' + node_status)
  else :
    node_status = 'not calculated, latest rtc is corrupt'
  
  #print(sID[0],table,node_status, gap, magnitude)
  #print(sID[0],table,node_status)
  #entering db
  #print(sID[0], datetime.datetime.now(), str(clusters))
  ReportIntervalClusters(sID[0], table, str(clusters))
  print()
  print()
  print(sID[0], table, str(clusters))


