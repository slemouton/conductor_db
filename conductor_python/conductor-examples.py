#construction de sequences "abstraites" à partir d'neregistrements et de listes de signatures

from conductor import *

# create a sequence by loading files :
seq = Sequence()
seq.load ('/Users/lemouton/Desktop/conductor_db/datasets/data_txt/ck_id_01_01.txt',
            '/Users/lemouton/Desktop/conductor_db/datasets/markers/ck_id_01_01_markers.txt',
            '/Users/lemouton/Desktop/conductor_db/datasets/time_signatures/ck_id_01_01.csv')

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
seq.plot(1)
seq_a.plot(1)

