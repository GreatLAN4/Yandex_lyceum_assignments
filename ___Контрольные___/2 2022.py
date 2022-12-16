file1 = input()
file2 = input()
use_color = input()
f1 = open(file1, 'r', encoding='utf8')
lines1 = f1.readlines()
f2 = open(file2, 'r', encoding='utf8')
lines2 = f2.readlines()

f3 = open('regards.txt', 'w')
list_number = {}

for line in lines1:
    line.rstrip('\n')
    number, color = line.split()
    list_number[number] = color
    if use_color == color:
        use_number = number
use_color = lines2[int(use_number) - 1]

my_list = []
f = 1

for i in use_color.split():

    if i in list_number.keys():
        my_list.append(list_number[i])
    else:
        f3.write('Error')
        f = 0
        break
if f:
    f3.write('\n'.join(my_list))
f1.close()
f2.close()
f3.close()
