# к, м, с
coffee = {'Эспрессо': [1, 0, 0], 'Капучино': [1, 3, 0],
          'Маккиато': [2, 1, 0], 'Кофе по-венски': [1, 0, 2],
          'Латте Маккиато': [1, 2, 1], 'Кон Панна': [1, 0, 1]}


def choose_coffee(*preferences):
    for ingr in preferences:
        if coffee[ingr][0] <= ingredients[0] and coffee[ingr][1] <= ingredients[1] \
                and coffee[ingr][2] <= ingredients[2]:
            ingredients[0] -= coffee[ingr][0]
            ingredients[1] -= coffee[ingr][1]
            ingredients[2] -= coffee[ingr][2]
            return ingr
    return 'К сожалению, не можем предложить Вам напиток'
