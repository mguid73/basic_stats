#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Basic stats module
"""

def mean(a):

	"""
	input is the list of numbers you want to take the mean
	"""

	# computing amount 
	ctlist= []
	for n in a:
		n=1                    # changing every value in the list to 1
		ctlist.append(n)      # creating a new list made up of 1's
	count = 0
	for s in ctlist:          # for loop to iteratively add values in sumlist
		count += s             # augmented assignment expression calculates count
	# Compute the mean of the elements in list a.
	listsum = 0
	for n in a:          # for loop to iteratively add values
		listsum += n             # augmented assignment expression calculates sum
	# we have the sum and the N of the list, now lets calculate mean
	avg = listsum/count
    
	return avg