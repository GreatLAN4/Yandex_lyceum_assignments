from PIL import Image


# функция добавляет сероы квадрат на картинку
def image_filter(pixels, i, j, sizeX, sizeY):
    # принимает 2. мерный список кортежей, координаты центра квадрата и его размеры
    # приобразует все цвета в серый

    for row in range(i - sizeX, i + sizeX):
        for col in range(j - sizeY, j + sizeY):
            r = pixels[row, col][0]
            g = pixels[row, col][1]
            b = pixels[row, col][2]
            new_color = (r + g + b) // 3
            pixels[row, col] = (new_color, new_color, new_color)
    return pixels


im = Image.open("image.jpg")
x, y = im.size
pixels = im.load()
print(x, y)
pixels = image_filter(pixels, 500, 500, 300, 300)

im.show()
