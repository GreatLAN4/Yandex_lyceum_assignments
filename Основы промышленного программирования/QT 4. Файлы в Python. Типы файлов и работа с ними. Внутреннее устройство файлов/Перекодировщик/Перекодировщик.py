file_input = open('cyrillic.txt', mode='r', encoding='utf8')
file_output = open('transliteration.txt', mode='w', encoding='utf8')

translit = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
            "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
            "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
            "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
            "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
            "б": "b", "ю": "ju", "ё": "jo"}
for line in file_input.readlines():
    new = ""
    for i in line:
        if i.lower() in translit.keys():
            if i.isupper():
                new += translit[i.lower()].capitalize()
            else:
                new += translit[i.lower()]
        else:
            new += i
    file_output.writelines(new)
file_input.close()
file_output.close()


