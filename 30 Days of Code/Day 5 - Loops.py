#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input('Input the number you want to print first 10 mutiples of: ').strip())
    for i in range(1,11):
        result = n * i
        print('{} x {} = {}'.format(n,i,result))