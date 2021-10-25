from PIL import Image

def extract_level(s):
    print(s)
    for letter in s[s.find('[')+1:s.find(']')].split(','):
        print(chr(int(letter)), end='')

if __name__ == "__main__":
    im = Image.open('oxygen.png')
    (width, height) = im.size
   
    s = ''.join([chr(im.getpixel((x, height//2))[0]) for x in range(0, width, 7)])
    extract_level(s)

#    for x in range(0, width, 7):
#        p = im.getpixel((x, height//2))[0]
#        print(chr(p), end='')

#    print()
#    print(''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121])))
