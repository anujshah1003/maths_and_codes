'''
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention
to small details like topography. During his last hike he took exactly n steps.
For every step he took, he noted if it was an uphill, U, or a downhill, D step.
Gary's hikes start and end at sea level and each step up or down represents a 1 
unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a 
step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a 
step down from sea level and ending with a step up to sea level.

Given Gary's sequence of up and down steps during his last hike, find and print 
the number of valleys he walked through.

For example, if Gary's path is s=[DDUUUUDD] , he first enters a valley  units 
deep. Then he climbs out an up onto a mountain  units high. 
Finally, he returns to sea level and ends his hike.

'''

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
