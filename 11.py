from PIL import Image

im = Image.open("11.jpg")
(width, height) = im.size

even = Image.new(im.mode, (width//2, height//2))
odd = Image.new(im.mode, (width//2, height//2))

for y in range(0, height, 2):
    for x in range(0, width, 2):
        even.putpixel((x//2, y//2), im.getpixel((x, y)))

for y in range(1, height, 2):
    for x in range(1, width, 2):
        odd.putpixel((x//2, y//2), im.getpixel((x, y)))

even.save("11_even.jpg")
odd.save("11_odd.jpg")
