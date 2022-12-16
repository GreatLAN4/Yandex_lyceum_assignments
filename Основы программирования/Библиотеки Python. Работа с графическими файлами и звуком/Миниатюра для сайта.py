from PIL import Image


def make_preview(size, n_colors):
    im = Image.open("image.jpg")
    size_im = im.resize((size))
    res = size_im.quantize(n_colors)
    res.save("res.bmp")
