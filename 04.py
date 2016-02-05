from __future__ import absolute_import, division, print_function

import urllib

def autobot(nothing):
    param = urllib.urlencode({'nothing' : nothing})
    f = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % param)
    words = f.read()
    if words == "Yes. Divide by two and keep going.":
        return str(int(nothing)//2)
    else:
        return words.split()[-1]
        
if __name__ == "__main__":
    start = '12345'
    while len(start) > 0:
        start = autobot(start)
        print(start)
        if not start.isdigit():
            break
