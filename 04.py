from urllib.parse import urlencode
from urllib.request import urlopen

def autobot(nothing):
    param = urlencode({'nothing' : nothing})
    f = urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?%s" % param)
    words = f.read()
    print(words)
    if words == b"Yes. Divide by two and keep going.":
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
