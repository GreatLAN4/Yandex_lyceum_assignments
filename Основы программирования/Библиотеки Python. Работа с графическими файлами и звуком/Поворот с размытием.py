from PIL import Image, ImageFilter


def motion_blur(n):
    im = Image.open("image.jpg")
    tr_im = im.transpose(Image.ROTATE_270).filter(ImageFilter.GaussianBlur(radius=n))
    tr_im.save('res.jpg')
