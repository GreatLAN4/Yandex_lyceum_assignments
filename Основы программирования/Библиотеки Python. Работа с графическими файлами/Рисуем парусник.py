from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color="#87CEEB", ocean_color="#017B92", boat_color="#874535",
            sail_color="#FFFFFF", sun_color="#FFCF40"):
    im = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(im)
    draw.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)
    draw.rectangle(((0, int(height * 0.8)), (width, height)),
                   ocean_color)
    draw.ellipse((
        (int(0.8 * width), -int(0.2 * height)),
        (int(1.2 * width), int(0.2 * height))),
        sun_color)
    draw.rectangle(((int(width * 0.49), int(height * 0.7)), (int(width * 0.51), int(height * 0.3))), boat_color)

    draw.polygon(((int(width * 0.51), int(height * 0.3)),
                  (int(width * 0.66), int(height * 0.45)),
                  int(width * 0.51), int(height * 0.6)), sail_color)
    draw.polygon(((int(width * 0.25), int(height * 0.65)),
                 (int(width * 0.3), int(height * 0.85)),
                 (int(width * 0.7), int(height * 0.85)),
                 (int(width * 0.75), int(height * 0.65))), boat_color)

    im.save(str(file_name))
    im.show()


picture('test.jpg', 1000, 800)
