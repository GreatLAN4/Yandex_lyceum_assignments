en = ["January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December"]
ru = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
      "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]


def month_name(n, leng):
    if leng == "en":
        return en[n - 1]
    elif leng == "ru":
        return ru[n - 1].lower()
