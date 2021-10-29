import gzip
from difflib import Differ
from io import BytesIO
from PIL import Image

DELIM = '   '
with gzip.open('deltas.gz', 'rt') as f:
    left = []
    right = []
    for line in f:
        idx = line.find(DELIM)
        if idx == -1:
            continue
        l = line[0:idx].strip()
        r = line[idx:].strip()
        if len(l):
            left.append(l)
        if len(r):
            right.append(r)

'''
with open('0.png', 'wb') as f0, open('1.png', 'wb') as f1, open('2.png', 'wb') as f2:
    for line in Differ().compare(left, right):
        data = bytes([int(ch, 16) for ch in line[2:].split(' ')])
        if line[0] == '+':
            f1.write(data)
        elif line[0] == '-':
            f2.write(data)
        else:
            f0.write(data)
'''

f = [BytesIO() for _ in range(3)]
for line in Differ().compare(left, right):
    data = bytes([int(ch, 16) for ch in line[2:].split(' ')])
    if line[0] == '+':
        f[1].write(data)    # right only
    elif line[0] == '-':
        f[2].write(data)    # left only
    else:
        f[0].write(data)    # common

for i in range(3):
    Image.open(f[i], 'r').show()