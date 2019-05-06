#!/usr/bin/python
# -*- coding: latin-1 -*-

#construction de sequences "abstraites" à partir d'neregistrements et de listes de signatures

from conductor import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('MacOSX')

# create a sequence by loading files :
seq = Sequence()
seq.load ('../datasets/data_txt/ck_id_01_01.txt',
            '../datasets/markers/ck_id_01_01_markers.txt',
            '../datasets/time_signatures/ck_id_01_01.csv')

#print(seq.tolist())

# find a bar corresponding to a bar signature in a sequence
# print (seq1.trouve('4/4_4/4_4/4'))
# print (seq2.trouve2('4/4_4/4_4/4',2000))
markers = [85, 2664, 5333, 7991, 10231]
signatures =['4/4', '7/4', '6/4','6/4','5/4']
seq_a = seq.cas1(signatures,markers)
print(seq_a)

#plot a bar
b = seq.bar_list[0]
b.plot(1)
b.plot(2)
b.plot(3)

#plot a sequence
#seq.plot(1)
seq_a.plot(1)


plt.vlines([1, 2], 0, 1, colors='r')
plt.show()


import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0.0, 5.0, 0.1)
s = np.exp(-t) + np.sin(2 * np.pi * t) + 1
nse = np.random.normal(0.0, 0.3, t.shape) * s

fig, (vax) = plt.subplots(1, 1, figsize=(12, 6))

vax.plot(t, s + nse, '^')
vax.vlines(t, [0], s)
# By using ``transform=vax.get_xaxis_transform()`` the y coordinates are scaled
# such that 0 maps to the bottom of the axes and 1 to the top.
vax.vlines([1, 2], 0, 1, transform=vax.get_xaxis_transform(), colors='r')
vax.set_xlabel('time (s)')
vax.set_title('Vertical lines demo')

plt.show()
