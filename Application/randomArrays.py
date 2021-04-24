#GMIT 2020
#Computational Thinking with Algorithms module
#Computer Science - Data Analytics course
#Noa P Prada Schnor   G00364074

#Application used to benchmark 5 sorting algorithms: insertion sort, merge sort, counting sort, quicksort and timsort. Application's files:
#sorting_algorithms.py - contains the 5 sorting functions
#randomArrays.py - contains the functions that creates random arrays, and list with array of arrays of different sizes
#benchmark_plot.py - run this to get the results: table and plot

#########################################################################################################

#import library 

import numpy as np

#########################################################################################################

#Create arrays to test the sorting algorithms
def random_array(n): #function that randomly generates integers between 0 an 99

  listArray = []

  a = 1

  while a in range(1, 11): #will loop 10 times to create 10 arrays
    newArray = list(np.random.randint(0, 100, n)) #create an array with random positive integers (range from 0 to 99)
    listArray.append(newArray) #append the array
    a += 1

  return listArray #return an array with 10 arrays of same size

########################################################################################################


#list with several n size of array to be tested
size_n = [20, 50, 100, 250, 500, 750, 1000, 1250,2500, 3750, 5000, 6250, 7500, 8750, 10000]

##################################################

#Create random lists with different n of elements

#original list of 15 arrays of different size. Each array has 10 different arrays of same size.
arr20 = random_array(20)
arr50 = random_array(50)
arr100 = random_array(100)
arr250 = random_array(250)
arr500 = random_array(500)
arr750 = random_array(750)
arr1000 = random_array(1000)
arr1250 = random_array(1250)
arr2500 = random_array(2500)
arr3750 = random_array(3750)
arr5000 = random_array(5000)
arr6250 = random_array(6250)
arr7500 = random_array(7500)
arr8750 = random_array(8750)
arr10000 = random_array(10000)


##################################################

#list containing the arrays created

list_arr = [arr20, arr50, arr100, arr250, arr500, arr750, arr1000,arr1250, arr2500, arr3750, arr5000, arr6250, arr7500, arr8750, arr10000]

#Array size = index in the list of arrays
#arr20 = 0
#arr50 = 1
#arr100 = 2
#arr250 = 3
#arr500 = 4
#arr750 = 5
#arr1000 = 6
#arr1250 = 7
#arr2500 = 8
#arr3750 = 9
#arr5000 = 10
#arr6250 = 11
#arr7500 = 12
#arr8750 = 13
#arr10000 = 14
