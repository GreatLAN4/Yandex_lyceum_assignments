from PIL import Image


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" \
           f"{hex(g)[2:].rjust(2, '0')}" \
           f"{hex(b)[2:].rjust(2, '0')}"


def alien_scientist(file_name, res_name, **colors):
    for key, value in colors.items():
        colors[key] = rgb_to_hex(value)
    im = Image.open(file_name)
    pixels = im.load()
    x, y = im.size

    for i in range(x):
        for j in range(y):
            rgb = pixels[i, j]
            hex = rgb_to_hex(rgb)
            if hex in colors.keys():
                pixels[i, j] = hex_to_rgb(colors[hex])
    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    im.save(res_name)
