cheque = []
count = 0
count += 1


def add_item(item_name, item_cost):
    cheque.append((item_name, item_cost))


def print_receipt():
    global count, cheque
    if cheque:
        print('Чек {}. Всего предметов: {}'.format(count, len(cheque)))
        sum_price = 0
        for name, price in cheque:
            print('{} - {}'.format(name, price))
            sum_price += price
        print(f"Итого: {sum_price}")
        print("-----")
        count += 1
        cheque = []

#
# add_item('Блокнот', 100)
# print_receipt()
#
# add_item('Ручка', 70)
# print_receipt()
# print_receipt()
#
# add_item('Булочка', 15)
# add_item('Булочка', 15)
# add_item('Чай', 5)
# print_receipt()
