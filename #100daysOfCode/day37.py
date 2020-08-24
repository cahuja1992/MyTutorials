#!/bin/python

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
  word_map = {}
  for ch in magazine:
    if ch!=" ":
      if ch in word_map:
        word_map[ch]+=1
      else:
        word_map[ch]=1
  
  for ch in note:
    if ch in word_map and word_map[ch]!=0:
      word_map[ch]-=1
    else:
      print("No")
      return
  print("Yes")

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
