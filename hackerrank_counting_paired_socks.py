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

