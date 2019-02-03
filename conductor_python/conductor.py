# analyse et visualisation des données du projet conductorfollowing/Idea/Haapamaki
# serge lemouton 2019

#for examples, see conductor_examples.py

# todo
# git repo + io
# dans trouve1, tri les solutions par difference croissantes
# function sdk
# loading mubu data with easdif library (axel ?)
# unit test

from typing import List, Any
import numpy as np
import copy
import matplotlib.pyplot as plt
import itertools

class Sequence:
    def __init__(self):
        data = 0
        self.marker_list = 0
        self.signature_list = 0
        self.context_list = 0
        self.bar_list = []

    def load(self, data_file, markers_file, signatures_file):
        data = Data(data_file)
        self.marker_list = duplets(np.loadtxt(markers_file, str))
        self.signature_list = np.loadtxt(signatures_file, str)
        self.context_list = triplets(self.signature_list)
        for m, s, c in itertools.zip_longest(self.marker_list, self.signature_list, self.context_list):
            b = Bar()
            b.limits = m
            b.duration = m[1][0].astype(np.float) - m[0][0].astype(np.float)
            b.index = len(self.bar_list)
            b.sequence = self
            b.mesure = s
            b.context = c
            b.data = data
            self.bar_list.append(b)

    def find(self, signature):
        a = np.array(self.signature_list)
        return np.where(a == signature)

    def trouve(self, context):
        a = np.array(self.context_list)
        return np.where(a == context)

    def trouve1(self, mesure, duration):
        epsilon = 1000
        a = np.array(self.signature_list)
        indexes = np.where(a == mesure)

        possible_bars = list(map(lambda x: (self.bar_list[x]), indexes[0].tolist()))
        result: List[Any] = []
        for b in possible_bars:
            print("diff", b.duration - duration)
            if (b.duration - duration < epsilon):
                result.append(b)
        if (result.__len__() == 0):
            print("trouve1: not found")  # raise error
        return result

    def trouve2(self, context,duration):
        epsilon = 1000
        a = np.array(self.context_list)
        indexes = np.where(a == context)

        possible_bars = list(map(lambda x: (self.bar_list[x]), indexes[0].tolist()))
        result: List[Any] = []
        for b in possible_bars:
            print("diff",b.duration - duration)
            if (b.duration - duration < epsilon):
                result.append(b)
        if (result.__len__()==0):
            print ("not found") # raise error
        return result

    def plot(self, index):
        "plotte les mesures les unes apres les autres !"
        res = np.array([])
        for b in self.bar_list:
            res = np.append(res,b.extract_data(index))
        plt.plot(res)

    def cas(self, signatures, markers):
        "create abstract sequence"
        result = Sequence()
        for s, m in itertools.zip_longest(signatures, markers):
            b = copy(self.find(s))
            result.bar_list.append(b)
        return result

    def cas0(self, signatures, markers):
        "create abstract sequence using context"
        result = Sequence()
        for s, m in itertools.zip_longest(signatures, markers):
            b = copy(self.trouve(s))
            result.bar_list.append(b)
        return result

    def cas1(self, mesures, markers):
        "create abstract sequence using bar signatures and duration"
        result = Sequence()
        segments = duplets(markers)
        for s, m in zip(mesures, segments):
            found_bars = self.trouve1(s, m[1] - m[0])
            found_bar = found_bars[0] # take the
            b = copy.copy(found_bar)
            result.bar_list.append(b)
        return result

    def cas2(self, signatures, markers):
        "create abstract sequence using context and duration"
        result = Sequence()
        segments = duplets(markers)
        for s, m in itertools.zip_longest(signatures, segments):
            found_bar = self.trouve2(s,m[1] - m[0])
            b = copy.copy(found_bar)
            result.bar_list.append(b)
        return result

    def tolist(self):
        return markers_to_list(self.marker_list)


class Bar:
    def __init__(self):
        self.limits = [0, 1]
        self.tempo = 60
        self.index = 1
        self.sequence = ()
        self.data = 0
        self.mesure = '4/4'
        self.mesure_context = '0_4/4_0'

    def plot(self, index):
        debut = float(self.limits[0][0]) * 0.02
        fin = float(self.limits[1][0]) * 0.02
        debut = int(debut)
        fin = int(fin)
        plt.plot(self.data.mat[debut:fin, index])
        plt.show

    def extract_data(self,index):
        debut = float(self.limits[0][0]) * 0.02
        fin = float(self.limits[1][0]) * 0.02
        debut = int(debut)
        fin = int(fin)
        return self.data.mat[debut:fin, index]


class Data:
    def __init__(self, file):
        self.mat = np.loadtxt(file)

    def plot(self, index):
        plt.plot(self.mat[:, index])
        plt.show


#utilities

def duplets(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable, 2)
    next(b, None)
    return list(zip(a, b))

def triplets(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    r = list(zip(a, b, c))
    return list(map(lambda x: str(x[0]) + '_' + str(x[1]) + '_' + str(x[2]), r))

def markers_to_dur(markers_list):
    return list(map(lambda x: ((x[1][0]).astype(np.float) - (x[0][0]).astype(np.float)).astype(np.int),markers_list))

def markers_to_list(markers_list):
    return list(map(lambda x:   (x[0][0]).astype(np.float).astype(np.int),markers_list))

def plot_bars(bar_l):
    map(plot, bar_l)


