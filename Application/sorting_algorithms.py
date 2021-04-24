#GMIT 2020
#Computational Thinking with Algorithms module
#Computer Science - Data Analytics course
#Noa P Prada Schnor   G00364074

#Application used to benchmark 5 sorting algorithms: insertion sort, merge sort, counting sort, quicksort and timsort. Application's files:
#sorting_algorithms.py - contains the 5 sorting functions
#randomArrays.py - contains the functions that creates random arrays, and an array of arrays of different sizes
#benchmark_plot.py - run this to get the results: table and plot

#########################################################################################################

#import libraries and modules
import numpy as np

##################################################

#Sorting algorithms

#insertionSort code adapted from Tarcisio Marinho https://github.com/tarcisio-marinho/sorting-algorithms/blob/master/timsort.py
def insertionSort(array,left=0,right=None):
  if right is None:  # by default left is 0 and right is (lenght of array -1)
    right = len(array) - 1

  for i in range(left+1,right+1): #i = index of the array
    j = i #j gets the value of i

    while j > left and array[j] < array[j-1]: #if j is higher than 0 and element in the j position is smaller than the element of its left
      array[j],array[j-1] = array[j-1],array[j] #'swap' elements. Slide the element from its left to one position to the right and insert the element in the position j one place to its left.
      j -= 1 #decrease j by one


  return array

##################################################

# MergeSort code adapted from Panjak https://www.journaldev.com/31541/merge-sort-algorithm-java-c-python)
def mergeSort(array,left=None, mid = None, right=None): #divide and conquer sorting algorithm
  
  if len(array) > 1:#divide the array in subarrays
    if left is None and mid is None and right is None:
      mid = len(array)//2  # get the number of half of the length of the array
      left = array[:mid]  # first half of the array
      right = array[mid:]  # second half of the array
    
    #recursive function that splits the array in small chunks
    mergeSort(left)
    mergeSort(right)

    i, j, k = 0, 0, 0  # indexes for left, right and array


  #merge the subarrays
    while i < len(left) and j < len(right): #while the 'index' of i is less than the number of elements of left amd j is less than the n. of elements of right
      if left[i] < right[j]: #if the element in i index of left is less than the element in j element of right 
        array[k] = left[i] #then the element in k index of array will be the element in i index of left
        i += 1 #increase the index i by 1
      else: #if right[j] < left[i]
        array[k] = right[j] #then the element of k index of array will be the element in j index of right
        j += 1 #increase the index j by 1
      k +=1 #after the if or else statement is completed, increase de index k by 1
      
    #check if there is any element left in the subarrays
    while i < len(left):
      array[k] = left[i]
      i += 1
      k += 1
        
    while j < len(right):
      array[k] = right[j]
      j += 1
      k += 1
  
  return array

#merge_sort adapted from https://www.pythonpool.com/python-timsort/

def merge_sort(array,lt,mid,rt): #version of merge sort that will be called by timSort

  length_l = mid - lt + 1 #len of left array
  length_r = rt - mid #len of right array
  left,right = [],[] #create empty left and right arrays that will be populated in the next for loops
  
  for i in range(0, length_l):
    left.append(array[lt + i])
  for i in range(0, length_r):
    right.append(array[mid + 1 + i])

  i,j,k = 0,0,lt

  while j < length_r and i < length_l:
    if left[i] <= right[j]:
      array[k] = left[i]
      i += 1

    else:
      array[k] = right[j]
      j += 1

    k += 1

  while i < length_l:
    array[k] = left[i]
    k += 1
    i += 1

  while j < length_r:
    array[k] = right[j]
    k += 1
    j += 1


##################################################

#countingSort code by https://codezup.com/implementation-of-counting-sort-algorithm-in-python/
#non comparison sorting algorithm
def countingSort(array):

  counter = [0] * (100) #create a 'bucket' to each value. Max value = 99

  for i in array:
    counter[i] += 1 #keep counter for each 'bucket'
  
  #For each 'bucket', from smallest key to largest, add the index of the bucket to the input array
  i=0
  for j in range(100): #from 0 to 99 (max value)
    for _ in range(counter[j]):
      array[i] = j
      i += 1
  
  return array

##################################################

#quickSort code adapted from Santiago Valdarrama https://realpython.com/sorting-algorithms-python/
def quickSort(array):
  if len(array) < 2: #if the array contains less than 2 elements,, then return the array
    return array
  
  low,same,high = [],[],[] #creating empty arrays to populate them. Low = elements with values less than the pivot. Same will contain the pivot element and elements with same value than the pivot element. High array will contain elements with values more than the pivot element.

  pivot = array[np.random.randint(0,len(array)-1)] #randomly choose the pivot element

  for item in array: #itinerate through each element in the array
    if item < pivot:
      low.append(item) #add this element in the low array that will contain elements which value is less than the pivot
    elif item == pivot:
      same.append(item)
    elif item > pivot:
      high.append(item)
  
  return quickSort(low) + same + quickSort(high) #recursively runs through the low and high arrays, resulting in the combination of the sorted lists.

##################################################

 # minrun code from Karthik Desingu https://www.codespeedy.com/timsort-algorithm-implementation-in-python/

min_num = 32

#function that will be called in timSort to get the value of the min_run variable
def minrun(n):
  r = 0
  while n >= min_num:
    r |= n & 1
    n >>= 1
  
  return n + r

# timSort adapted from Tarcisio Marinho https://github.com/tarcisio-marinho/sorting-algorithms/blob/master/timsort.py and DrYshio https://github.com/DrYshio/TimSort/blob/main/main.py
def timSort(array):  #hybrid sorting algorithm = insertion sort + merge sort
  n = len(array)
  min_run = minrun(n) #minimum number of elements of a run

  for s in range(0,n,min_run):
    e = min(s + min_run - 1, n-1)
    insertionSort(array,s,e)

  size = min_run

  while size < n:

    for left in range(0,n,2*size):
      mid = min(n-1,left+size-1)
      right = min((left+2*size-1),(n-1))
      merge_sort(array,left,mid,right)
    
    size = 2*size

  return array
