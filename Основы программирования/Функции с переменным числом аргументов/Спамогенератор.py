e_mails = ["Q_werty@gmail.com", "Add_ol"]
names = ["Вера Кузнецова", "Адд Одифив"]

points = ["Уфе", "Оренбурге"]
dates = ["19:00", "20:00"]


def spam_bot(e_mail, name, date, point="Стерлитамаке"):
    return f"To:{e_mail}"\
           f"\nЗдравствуйте, {name}" \
           f"\nБыли бы рады видеть вас на встрече начинающих программистов в {point}," \
           f"\nкоторая пройдет {date}."


print(spam_bot(e_mails[0], names[0], dates[0], points[0]))
print()
print(spam_bot(e_mails[1], names[1], dates[1], points[1]))
print()
print(spam_bot(e_mails[0], names[0], dates[0]))


