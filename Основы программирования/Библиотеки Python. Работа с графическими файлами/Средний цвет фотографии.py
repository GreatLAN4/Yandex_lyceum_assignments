from PIL import Image

im = Image.open('image.jpg')

w, h = im.size
pixels = im.load()
x, y = im.size  # ширина (x) и высота (y) изображения
pixel = []
for i in range(x):
    for j in range(y):
        pixel = pixels[i, j]
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]

print(pixel)