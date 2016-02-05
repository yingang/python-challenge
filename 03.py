from __future__ import absolute_import, division, print_function

import re

def filter(filename):
    rule = '[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}'
    for line in open(filename):
        result = re.findall(rule, line)
        for item in result:
            if len(item) > 4:
                print(item[4], end="")
            
if __name__ == "__main__":
    filter('03.txt')