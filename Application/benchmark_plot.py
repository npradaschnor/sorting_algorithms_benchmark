#GMIT 2020
#Computational Thinking with Algorithms module
#Computer Science - Data Analytics course
#Noa P Prada Schnor   G00364074

#Application used to benchmark 5 sorting algorithms: insertion sort, merge sort, counting sort, quicksort and timsort. Application's files:
#sorting_algorithms.py - contains the 5 sorting functions
#randomArrays.py - contains the functions that creates random arrays, and an array of arrays of different sizes
#benchmark_plot.py - run this to get the results: table and plot

#########################################################################################################

from sorting_algorithms import insertionSort, mergeSort,countingSort, quickSort, timSort
from randomArrays import list_arr, arr20, arr50, arr100, arr250, arr500, arr750, arr1000, arr1250, arr2500, arr3750, arr5000, arr6250, arr7500, arr8750, arr10000, size_n
import time
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import copy

##################################################################################################################

#Benchmark

def timerRun(function, array):  # function to get the avg run time. The arg array is a list of 10 different arrays with same number of elements

  arr = copy.deepcopy(array) #to avoid the original array of been sorted

  results = []  # will store the running time of the 10 times

  i = 0 #set i to zero. It will be used in the while loop.

  while i < 10: #will run 10 times     
    start_time = time.time() #log the start time in seconds
    function(arr[i])  # each time the function is called a different array is used as an argument
    end_time = time.time() #log the end time in seconds
    results.append(end_time-start_time) #add into the results array the time in seconds that the function run
    i += 1 #increase by 1 d

  r = sum(results)  # sum the results of 10 runs
  l = len(results)  # get the number of times that it run

  # final result is the total running time divided by number of times it rum and multiplied by 1000 to get the result in milliseconds
  avg_run = (r/l)*1000

  # return the average run time with 3 decimal places
  return (round(avg_run, 3))



##################################################

#get the average running time of sorting algorithms to sort random array of different sizes

def sortRun(sort_function): 

  avg_time = [] #empty list to be populated with avg running time of the sorting function with different array sizes

  global list_arr #list that contains 14 lists with different size and each list contains 10 nested arrays with same number of elements

  new_list = copy.deepcopy(list_arr) #independent copy of list_arr. So, each time sortRun is called, the list_arr remains the same and an independent copy is made

  index = 0 #index starts at 0 and will be increased to 14, until the while loop stops. 

  while index < 15: #there are 15 different input sizes (check randomArrays.py for more info)
      avg_run_test = timerRun(sort_function, new_list[index]) #get the avg run time of 10 times the function run with a specific input size
      avg_time.append(avg_run_test) #populate the avg_time array with the results
      index += 1 #increase index by 1

  return avg_time #return the results after all the tests were done

##################################################

#Create the list with running time for each sorting algorithm
insertionSort_time = sortRun(insertionSort)
mergeSort_time = sortRun(mergeSort)
countingSort_time = sortRun(countingSort)
quickSort_time = sortRun(quickSort)
timSort_time = sortRun(timSort)

##################################################

#Console output containing the results

def dataframeResult():
  sort_name = ["Insertion Sort", "Merge Sort", "Counting Sort","Quicksort", "Timsort"] #will be used as the index of the dataframe
  input_size = ["20","50","100","250","500","750","1000","1250","2500","3750","5000","6250","7500","8750","10000"] #will be used as header

  #Create the arrays with the avg running time 
  insertionSort_t = np.array(insertionSort_time)
  mergeSort_t = np.array(mergeSort_time)
  countingSort_t = np.array(countingSort_time)
  quickSort_t = np.array(quickSort_time)
  timSort_t = np.array(timSort_time)


  #Tuple containing all the avg running time
  time_result = (insertionSort_t,mergeSort_t,countingSort_t, quickSort_t,timSort_t)

  #Append multiple arrays into an array of arrays
  time_result = np.vstack(time_result)

  #Create dataframe to get a neat console output containing the average time vs input size for all the sorting algorithms tested
  time_output = pd.DataFrame(time_result, sort_name, input_size)

  #Set options on how to display the dataframe
  pd.set_option('display.max_rows', 20) #max number of rows to be displayed: 20
  pd.set_option('display.max_columns', 20) #max number of columns to be displayed: 20
  pd.set_option('display.width', 150)

  return time_output

#################################################################

def plotResult():
  #Graph of the test showing array size and average time of 10 runs per array size
  #fig, ax = plt.subplots(nrows=1,ncols=2,figsize=(8,4))
  #plt.style.use("dark_background")
  plt.figure().canvas.manager.set_window_title(
      "Sorting Algorithms - Time Complexity")
  #axs.subplots_adjust(0.125, 0.1, 0.9, 0.9, 0.2, 0.2)
  x = size_n
  plot1 = plt.plot(x, insertionSort_time, '-g', marker='o',
                   label='Insertion sort')  # insertionSort is solid green
  plot2, = plt.plot(x, mergeSort_time, '-y', marker='o',
                    label='Merge sort')  # mergeSort is solid yellow
  plot3, = plt.plot(x, countingSort_time, '-b', marker='o',
                    label='Courting sort')  # countingSort is solid blue
  plot4, = plt.plot(x, quickSort_time, '-k', marker='o',
                    label='Quicksort')  # quickSort is solid black
  plot5, = plt.plot(x, timSort_time, '-m', marker='o',
                    label='Timsort')  # timSort is solid magenta
  
  plt.ylabel = 'Running time (in milliseconds)'
  #ax.set_title = ('Complexity plot')
  plt.legend()

  plt.grid()  # show grid
  #plt.savefig("sortPerformance.png") #save the plot

  plt.show()

####################################################################################################################

if __name__ == "__main__":

  #show dataframe containing the results of running time with different input sizes
  dataframe = dataframeResult()
  print(dataframe)

  #show the Complexity plot of chosen sorting algorithms
  plotResult()
