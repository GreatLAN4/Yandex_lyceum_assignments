with open('input.bmp', 'rb') as data:
    starter = data.read(54)
    pixels = [255 - p for p in data.read()]

with open('res.bmp', 'wb') as final_data:
    final_data.write(starter)
    final_data.write(bytes(pixels))
