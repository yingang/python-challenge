from __future__ import absolute_import, division, print_function

import sys
import zipfile

def next(z, nothing):
    filename = nothing + '.txt'

    if filename not in z.namelist():
        sys.exit(0)

    info = z.getinfo(filename)
    print(info.comment, end='')

    words = z.open(filename).read()
    if words == "Yes. Divide by two and keep going.":
        return str(int(nothing)//2)
    else:
        return words.split()[-1]

if __name__ == "__main__":
    z = zipfile.ZipFile('06.zip', 'r')
    start = '90052'
    while len(start) > 0:
        start = next(z, start)
