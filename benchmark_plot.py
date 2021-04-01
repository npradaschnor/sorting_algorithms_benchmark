from sorting_algorithms import random_array,insertionSort,mergeSort,countingSort,quickSort,timSort
import time
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#Benchmark

def timer_run(num, function, array): #function to get the avg run time

  start_time = time.time()
  
  for r in range(0, num): #num is the number of times that the function will run
    function(array)
  
  end_time = time.time()

  avg_run = ((end_time - start_time) / num)*1000 #avg time in milliseconds
  
  return round(avg_run,3) #return the average run time with 3 decimal places


#list with several n size of array to be tested
size_n=[20, 50, 100, 250, 500, 750, 1000, 1250,2500, 3750, 5000, 6250, 7500, 8750, 10000]

#run the function 10 times and get the average run time for random array of different sizes
def sortRun(sort_function): 

  avg_time = [] #empty list to be populated with avg run time of the sorting function with different array sizes
  
  for array_len in size_n:
    array_test = random_array(array_len) #create random array 
    avg_run_test = timer_run(10, sort_function, array_test) #get the avg run time of 10 times the function run with a specific input size
    avg_time.append(avg_run_test) #populate the avg_time array with the results

  return avg_time #return the results after all the tests were done

#Create the list with running time for each sorting algorithm


insertionSort_time = sortRun(insertionSort)
mergeSort_time = sortRun(mergeSort)
countingSort_time = sortRun(countingSort)
quickSort_time = sortRun(quickSort)
timSort_time = sortRun(timSort)

def plotRun():
  #Graph of the test showing array size and average time of 10 runs per array size 
  fig, axs = plt.subplots((1, 2), constrained_layout=True)
  axs.subplots_adjust(0.125, 0.1, 0.9, 0.9, 0.2, 0.2)
  x = size_n
  plot1 = plt.plot(x,insertionSort_time, '-g', marker = 'o', label = 'Insertion sort') #insertionSort is solid green
  plot2, = plt.plot(x,mergeSort_time, '-y', marker = 'o', label = 'Merge sort') #mergeSort is solid yellow
  plot3, = plt.plot(x,countingSort_time, '-b', marker = 'o', label ='Courting sort') #countingSort is solid blue
  plot4, = plt.plot(x, quickSort_time, '-k', marker='o', label = 'Quicksort')  # quickSort is solid black
  plot5, = plt.plot(x,timSort_time, '-m', marker = 'o', label = 'Timsort') #timSort is solid magenta
  plt.xlabel = 'Input size (n)'
  plt.ylabel = 'Running time (in milliseconds)'
  plt.title = ('Performance of 5 Sorting Algorithms')
  plt.legend([plot1, plot2, plot3, plot4, plot5], ['Insertion sort', 'Merge sort', 'Counting sort',
                                                  'Quicksort', 'Timsort'], bbox_inches='tight', loc='lower left')

  plt.xlim(0, 10000) #limit to 10000 the the value of x axis
  #plt.tight_layout()  #prevent the legend box from being cropped
  plt.grid() #show grid
  plt.savefig("sortPerformance.png") #save the plot
  #plt.show()


#Console output containing the results

def dataframeRun():
  sort_name = ["Insertion Sort", "Merge Sort", "Counting Sort", "Quicksort", "Timsort"] #will be used as the index of the dataframe
  input_size = ["20","50","100","250","500","750","1000","1250","2500","3750","5000","6250","7500","8750","10000"] #will be used as header

  #Create the arrays with the avg running time 
  insertionSort_t = np.array(insertionSort_time)
  mergeSort_t = np.array(mergeSort_time)
  countingSort_t = np.array(countingSort_time)
  quickSort_t = np.array(quickSort_time)
  timSort_t = np.array(timSort_time)

  #Tuple containing all the avg running time
  time_result = (insertionSort_t,mergeSort_t,countingSort_t,quickSort_t,timSort_t) 

  #Append multiple arrays into an array of arrays
  time_result = np.vstack(time_result)

  #Create dataframe to get a neat console output containing the average time vs input size for all the sorting algorithms tested
  time_output = pd.DataFrame(time_result, sort_name, input_size)

  #Set options on how to display the dataframe
  pd.set_option('display.max_rows', 20) #max number of rows to be displayed: 20
  pd.set_option('display.max_columns', 20) #max number of columns to be displayed: 20
  pd.set_option('display.width', 150)

  print(time_output)



if __name__ == "__main__":
  dataframeRun()
  #plotRun()
