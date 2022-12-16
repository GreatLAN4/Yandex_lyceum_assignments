from PIL import Image


def mirror():
    im = Image.open("image.jpg")
    res_jpg = im.transpose(Image.FLIP_LEFT_RIGHT)
    res_jpg.save("res.jpg")

mirror()
