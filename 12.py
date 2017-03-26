with open('12.gfx', 'rb') as src:
    d = src.read()
    for i in range(5):
        with open('12_' + str(i) + '.jpg', 'wb') as dst:
            for j in range(i, len(d), 5):
                dst.write(d[j:j+1])
