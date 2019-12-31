#!/bin/python3

'''
Emma is playing a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. She can jump on any
cumulus cloud having a number that is equal to the number of the current cloud
plus 1 or 2. She must avoid the thunderheads. Determine the minimum number of 
jumps it will take Emma to jump from her starting postion to the last cloud. 
It is always possible to win the game.

For each game, Emma will get an array of clouds numbered 0 if they are safe or 1 
if they must be avoided. For example, c=[0,1,0,0,0,1,0] indexed from 0...6. 
The number on each cloud is its index in the list so she must avoid the clouds 
at indexes 1 and 5. 
She could follow the following two paths: 0->2->4->6 or 0->2->3->4->6.
The first path takes 3 jumps while the second takes 4.
'''

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    n = len(c)
    ind = 0
    step = 0
    while True:
        if ind+2<n and c[ind+2]==0:
            ind = ind+2
        elif ind+1<n and c[ind+1]==0:
            ind=ind+1
        else:
            break
        step+=1
    return step

res = jumpingOnClouds([0,1,0,0,0,1,0,1,0,0])
print(res)