#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max = -99 # we can not assign 0
    for i in range(4):
        for j in range(4):
            temp = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1]+arr[i + 2][j + 2]
            if (temp > max):
                max = temp;
    print(max)

# 1 1 0 1 1 0
# 1 1 1 5 5 5
# 1 1 1 1 1 0
# 1 1 0 7 5 6
# 5 5 5 1 1 5
# 7 5 6 1 5 5
