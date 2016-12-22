#from __future__ import absolute_import, division, print_function

def convert(input):
    if len(input) == 1:
        return '1' + input

    last = input[0]
    cnt = 1
    ret = ''
    for c in input[1:]:
        if c == last:
            cnt += 1
        else:
            ret += str(cnt) + last
            last = c
            cnt = 1

    return ret + str(cnt) + last

if __name__ == "__main__":
    seed = '1'
    for i in range(30):
        print(len(seed))
        seed = convert(seed)
    print(len(seed))
