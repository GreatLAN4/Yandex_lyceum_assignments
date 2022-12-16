def mirror(arr):
    mirrored_part = arr[::-1]
    arr.extend(mirrored_part)
# mirrored_part = arr.reverse() не работал тк методы ничего не возрощают
# в итоге переменая mirrored_part присваевалась None
# заменил на срез с обратным ходом
