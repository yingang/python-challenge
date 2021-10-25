import pickle

if __name__ == "__main__":
    f = open('05.pickle', 'rb')
    d = pickle.load(f)
    print(d)
    for row in d:
        for column in row:
            print(column[0]*column[1], end='')
        print()
