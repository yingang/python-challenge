from __future__ import absolute_import, division, print_function

def filter(filename):
    for line in open(filename):
        for ch in line:
            if ch.isalpha():
                print(ch, end="")
    print()
            
if __name__ == "__main__":
    filter('02.txt')