from PIL import Image

iim = Image.open('wire.png')
assert iim.size == (10000, 1)

oim = Image.new(iim.mode, (100, 100))

route = list(zip(
    range(100, 0, -2),
    range(99, -1, -2),
    range(99, -1, -2),
    range(98, -2, -2),
))
assert len(route) == 50

ix = -1
ox = -1
oy = 0
for a, b, c, d in route:
    print(a, b, c, d)
    for _ in range(a):  # left -> right
        ix += 1
        ox += 1
        oim.putpixel((ox, oy), iim.getpixel((ix, 0)))
    for _ in range(b):  # top -> bottom
        ix += 1
        oy += 1
        oim.putpixel((ox, oy), iim.getpixel((ix, 0)))
    for _ in range(c):  # right -> left
        ix += 1
        ox -=1
        oim.putpixel((ox, oy), iim.getpixel((ix, 0)))
    for _ in range(d):  # bottom -> top
        ix += 1
        oy -=1
        oim.putpixel((ox, oy), iim.getpixel((ix, 0)))

oim.show()