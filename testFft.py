#testFft.py
#Author: David Strube
#Date: 2020-07-22
#What is: testing python maths stuffs - particularly FFT as described here:
#https://numpy.org/doc/stable/reference/generated/numpy.fft.fft.html
#(in preparation for CS 6515 described here:
#http://catalog.gatech.edu/courses-grad/cs/

import numpy as np

#this works
#result = np.fft.fft(np.exp(2j * np.pi * np.arange(8) / 8))
#print(result)

#this works
import matplotlib.pyplot as plt
t = np.arange(256)
sp = np.fft.fft(np.sin(t))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)
plt.show()

#TODO: check out the "see also"s