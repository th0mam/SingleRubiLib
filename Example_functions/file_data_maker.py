# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 11:28:57 2024

@author: tlamich
"""

"""
This script creates files with fake data for further testing of other real time 
python processes that should be responsive to one by one incoming data.
"""

import time
from numpy.random import randn

x=0
while True:
    try:
        with open(f'C:/Users/tlamich/Data/fake_data/{x}.txt','w') as f:
            f.write(str(x*randn()))
        x+=1
        time.sleep(0.5)
    except KeyboardInterrupt:
        print("Fake data creator was killed by you you monster!!!")
        break
        