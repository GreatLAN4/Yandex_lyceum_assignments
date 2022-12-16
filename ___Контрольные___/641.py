from PIL import Image


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" \
           f"{hex(g)[2:].rjust(2, '0')}" \
           f"{hex(b)[2:].rjust(2, '0')}"


def cristal_planet(file_name, res_name, **colors):
    im = Image.open(file_name)
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения

    for i in range(x):
        for j in range(y):
            rgb = pixels[i, j]
            hex = rgb_to_hex(rgb)
            if hex in colors.keys():
                pixels[i, j] = hex_to_rgb(colors[hex])
    im = im.transpose(Image.FLIP_TOP_BOTTOM)

    im.save(res_name)


colors = {
    "#bdf3fa": "#ffffff",
    "#688cd3": "#5f5f8b",
    "#5f5f8b": "#7bd3f1",
    "#c5f3ed": "#455c4a"
}
cristal_planet("markdown-image.png", "13.png", **colors)
