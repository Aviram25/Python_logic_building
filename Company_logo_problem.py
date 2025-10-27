#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input().strip()
    chars = list(set(s))  # unique characters
    freq = [(c, s.count(c)) for c in chars]  # list of (char, count)
    
    # Sort: descending by count, then alphabetically
    sorted_char = sorted(freq, key=lambda x: (-x[1], x[0]))
    
    # Print top 3
    for c, count in sorted_char[:3]:
        print(c, count)


