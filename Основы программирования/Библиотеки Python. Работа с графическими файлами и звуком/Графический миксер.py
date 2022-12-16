from PIL import Image


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    x, y = im.size
    desk = Image.new("RGB", (x, y), (255, 255, 255))
    im_left = im.crop((0, 0, x // 2, y))
    im_right = im.crop((x // 2, 0, x, y))
    desk.paste(im_left, (x // 2, 0, x, y))
    desk.paste(im_right, (0, 0, x // 2, y))

    desk.save(output_file_name)
