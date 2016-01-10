from __future__ import absolute_import, division, print_function

import re

def filter(filename):
    rule = '[A-Z]{3}[a-z]{1}[A-Z]{3}'
    for line in open(filename):
        result = re.findall(rule, line)
        for item in result:
            if len(item) > 3:
                print(item[3], end="")
            
if __name__ == "__main__":
    filter('03.txt')