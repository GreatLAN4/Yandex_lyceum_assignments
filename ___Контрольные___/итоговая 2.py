def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def rgb_to_hex(rgb):
    r, g, b = rgb
    return f"#{hex(r)[2:].rjust(2, '0')}" \
           f"{hex(g)[2:].rjust(2, '0')}" \
           f"{hex(b)[2:].rjust(2, '0')}"


from PIL import Image

def alien_leisure(file_name, res_name, **colors):
    im = Image.open(file_name)
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    for i in range(x):
        for j in range(y):
            rgb = pixels[i, j]
            hex = rgb_to_hex(rgb)
            if hex in colors.keys():

                pixels[i, j] = hex_to_rgb(colors[hex])

    im.save(res_name)

colors = {
    "#ca86f2": "#a4f957",
    "#585858": "#3a7676",
    "#ffca18": "#f3508d",
    "#b83dba": "#ffacd6"
}
alien_leisure("recreation.png", "spare_time.png", **colors)