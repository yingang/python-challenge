from PIL import Image

im = Image.open("cave.jpg")
(width, height) = im.size

# put even/odd in same image (left/right)
output = Image.new(im.mode, (width, height//2))

# even
for y in range(0, height, 2):
    for x in range(0, width, 2):
        output.putpixel((x//2, y//2), im.getpixel((x, y)))

# odd
for y in range(1, height, 2):
    for x in range(1, width, 2):
        output.putpixel((x//2 + width//2, y//2), im.getpixel((x, y)))

output.show()
