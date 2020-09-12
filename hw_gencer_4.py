###############################################################
########################	HOMEWORK	#######################	
###############################################################

##
##
##
##
##	Author: Alper Sukru Gencer
##	Start Date: September 12, 2020
##	End Date: 	September 14. 2020
##
##
##
##


################################
####	QUESTIONS
################################

##	This homework is meant to give you feel for how dierent algorithms can affect runtime.
##
##	For this homework you will be required to implement two different sorting algorithms. 
##		You can choose from the ones we covered in class (not random sort) or use your own 
##		(there are lots if you spend some time searching online).
##
##	The only constraint on the two that you pick is that they must be in different complexity 
##		classes. Most likely you will need to find something that is O(n2) and O(nlogn) but 
##		feel free to find something exotic or make up your own. You must implement the 
##		sorting algorithms yourself.
##
##	Once you have verified that your sorts are working properly (using tests), you will need
##		to run a simulation and graph the results. Specifically, produce a graph with the 
##		following characteristics:
##			• The vertical axis is some measure of time
##			• The horizontal axis is N (size of set to sort)
##			• You have one line for each sort algorithm, showing how time goes up with N
##			• Everything is labeled appropriately
##
##	Try to pick an N such that the eect is visually noticeable. It should not take a
##		very large increase to make this possible.
##
##
##	Bonus: Also graph quicksort. Note whether you are graphing average, best or worst case 
##		run-time. To test average run times try generating an array full of random numbers 
##		and sorting it. Do this a number of times and take the mean run-time.







################################
####	SOLUTION:
################################




##
##
##
##	Loading Required Modules:

import matplotlib.pyplot as plt
import math
import numpy as np
import array
from random import shuffle



##
##
##
##	Let's create our sequence and then randomize it: 

my_numbers = list(range(1,30,2))
random.shuffle(my_numbers)
my_numbers




##
##
##
##	First Sorting Algorithm:

def bubble_sort(numbers): # Not the most efficient
    # Answer object 
    answer = numbers.copy()
    # N of numbers in numbers
    n = len(numbers) - 2
    # Index used in the while loop
    i = 0
    # Object to stop the while loop
    notSwap = len(my_numbers) - 2
    while notSwap != 0:   
        if answer[i] > answer[i + 1]: # Compare numbers
            answer[i], answer[i + 1] = answer[i + 1], answer[i] # Swap numbers
            if i == n: # Check index
                i = 0
            else: 
                i += 1            
        else:
            if i == n: # Check index
                i = 0
                notSwap = n
            else: 
                notSwap -= 1
                i += 1
    return answer



##
##
##
##	Second Sorting Algorithm:

def selection_sort(numbers):
    # Answer object 
    numbers = numbers.copy()  # to not modify the original input
    answer = []
    while len(numbers) > 0:
        answer.append(min(numbers))
        del numbers[numbers.index(answer[-1])]    
    return answer
                   


##
##
##
##	Third Sorting Algorithm:
##	Source: https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889

def merge_sort(arr):
    # The last array split
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return merge(left, right, arr.copy())

def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
      
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
        
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged




##
##
##
##	Let's See the Resulst from Various Sorting Algorithms:

my_numbers
bubble_sort(my_numbers)
selection_sort(my_numbers)
merge_sort(my_numbers)

merge_sort(my_numbers) == selection_sort(my_numbers) == bubble_sort(my_numbers) # It's True!




##
##
##
##	Let's See the Resulst from Various Sorting Algorithms:

