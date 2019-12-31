
#!/bin/python3
'''
Lilah has a string,s, of lowercase English letters that she repeated 
infinitely many times.

Given an integer,n , find and print the number of letter a's in the first  
letters of Lilah's infinite string.

For example, if the string s='abcac'  and n=10, the substring we consider is , 
abcacabcac the first 10 characters of the infinite string. There are 4 occurrences of a in 
the substring.

'''

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s)==1 or len(s)==n:
        if s=='a':            
            return n
        else:
            a_count=0
            for elem in s:
                if elem=='a':
                    a_count+=1
            return a_count
    else:
        a_count_sub=0
        for elem in s:
            if elem=='a':
                a_count_sub+=1
        if n%len(s)==0:
            num_sub_str=n//len(s)
            a_count=a_count_sub*num_sub_str
            return a_count
        
        else :
            num_sub_str=int(n/len(s))
            a_count=a_count_sub*num_sub_str
            for i in range(0,n%len(s)):
                if s[i]=='a':
                    a_count+=1
            return a_count