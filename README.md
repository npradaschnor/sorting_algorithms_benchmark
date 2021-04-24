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
import copy
import matplotlib.pyplot as plt
```

* numpy was used to generate random arrays with n different sizes
* pandas was used to create a dataframe containing the running times of all sorting algorithms 
* time was used to "measure" the running time of the chosen sorting algorithms
* copy was used to make a copy.deepcopy() of the original arrays
* matplotlib.pyplot was used to plot the running time of the sorting algorithms
  
File name | Description
----------|-------------
[sorting_algorithms.py](https://github.com/npradaschnor/sorting_algorithms_benchmark/blob/master/Application/benchmark_plot.py)| File that contains functions of the the five sorting algorithms 
[benchmark.py](https://github.com/npradaschnor/sorting_algorithms_benchmark/blob/master/Application/benchmark_plot.py) | File that contains the functions that runs and measure the running time of the sorting algorithms, prints the results as a dataframe and shows the plot of the results
[randomArrays.py](https://github.com/npradaschnor/sorting_algorithms_benchmark/blob/master/Application/randomArrays.py)| File that contains the function that generate random arrays of different size and also contains the arrays created 
[CTA_Project.pdf](https://github.com/npradaschnor/sorting_algorithms_benchmark/tree/master/Project%20Instructions) | PDF file that contains the project instructions
[CTA_report.docx](https://github.com/npradaschnor/sorting_algorithms_benchmark/tree/master/Report) | PDF file that introduces the chosen sorting algorithms, and discusses the results of the benchmarking process.
