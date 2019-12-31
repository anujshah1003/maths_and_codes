'''
John works at a clothing store. He has a large pile of socks that he must pair 
by color for sale. Given an array of integers representing the color of each 
sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar = [1,2,1,2,1,3,2]. 
There is one pair of color 1 and one of color 2. There are three odd socks left,
one of each color. The number of pairs is 2.
'''
import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    result_dict = {}
    for i in range(n):
        elem = ar[i]
        if elem not in result_dict.keys():
            result_dict[elem]=1
        else:
            result_dict[elem]+=1
    print (result_dict)
    num_pairs=0
    for val in result_dict.values():
        pair=val//2
        num_pairs+=pair
    return num_pairs

