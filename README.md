In this repository you will find an application used to benchmark five different sorting algorithms.
You will also find a report which introduces the chosen sorting algorithms, and discusses the results of the benchmarking process.
The five sorting algorithms chosen are:
1. Insertion Sort
2. Merge Sort
3. Counting Sort
4. Quicksort
5. Timsort

- Python 3.6v was used

The following libraries/modules were imported:

``` python
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt
```

* numpy was used to generate random arrays with n different sizes
* pandas was used to create a dataframe containing the running times of all sorting algorithms 
* time was used to "measure" the running time of the chosen sorting algorithms
* matplotlib.pyplot was used to plot the running time of the sorting algorithms
  
File name | Description
----------|-------------
sorting_algorithms.py| File that contains functions of the the five sorting algorithms 
benchmark.py | File that contains the functions that runs and measure the running time of the sorting algorithms, prints the results as a dataframe and shows the plot of the results
Project instructions | PDF file that contains the project instructions
Report | PDF file that introduces the algorithms you have chosen, and discusses the results of the benchmarking process.
