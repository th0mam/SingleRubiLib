# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 14:59:53 2024

@author: tlamich
"""

import time
import os
import matplotlib.pyplot as plt
import glob

path='C:/Users/tlamich/Data/fake_data/*.txt'
data=[]

plt.axis()
while True:
    try:
        if glob.glob(path):
            file_path=glob.glob(path)
            with open(file_path[0],'r') as f:
                data.append(float(f.read()))
            os.remove(file_path[0])
            plt.scatter(len(data),data[-1],c='black')
            plt.pause(0.1)
        else:
            time.sleep(0.1)
    except KeyboardInterrupt:
        plt.figure()
        plt.plot(data)
        plt.show()
        break