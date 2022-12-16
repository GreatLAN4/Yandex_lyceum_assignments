from PIL import Image


def mirror():
    im = Image.open("image.jpg")
    res_jpg = im.transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT)
    res_jpg.save('res1.jpg')

mirror()