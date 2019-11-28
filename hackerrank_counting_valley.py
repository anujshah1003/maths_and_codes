import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    if n<2 or n>1000000:
        return 0
    st=0
    num_valley=0
    valley_st=False
    valley_end=False
    for step in s:
        if step == 'D':
            st=st-1
        elif step == 'U':
            st=st+1
        if st==-1:
            valley_st = True
        if valley_st==True and st==0:
            valley_end=True
            num_valley+=1
            valley_st=False
            valley_end = False

    return num_valley
