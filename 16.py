from PIL import Image

im = Image.open('mozart.gif')
width, height = im.size

for y in range(height):
    for x in range(width):
        # locate the first purple pixel in each row
        if im.getpixel((x, y)) != 195:
            continue

        if x < width:
            # rotate pixels in each row to align the purple segment
            row = [im.getpixel((_x, y)) for _x in range(width)]
            row = row[x:] + row[:x]
            for x in range(width):
                im.putpixel((x, y), row[x])

im.show()