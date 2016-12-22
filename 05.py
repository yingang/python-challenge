from __future__ import absolute_import, division, print_function

import pickle

if __name__ == "__main__":
    f = open('05.pickle', 'r')
    d = pickle.load(f)
    for row in d:
        for column in row:
            print(column[0]*column[1], end='')
        print()
