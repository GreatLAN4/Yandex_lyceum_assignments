from PIL import Image, ImageDraw

im = Image.new("RGB", (1980, 1080))
drawer = ImageDraw.Draw(im)

drawer.rectangle(((0, 0), (1980, int(1080 * 0.8))), "#0080d5")
drawer.ellipse((-90, -90, 90, 180), fill = 'blue', outline ='red')
drawer.ellipse()
drawer.point((100, 100), 'red')
im.save("prep_test.jpg")
im.show()
