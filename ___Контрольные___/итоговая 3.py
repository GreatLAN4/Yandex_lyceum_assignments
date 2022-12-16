def borderland(*args, **kwargs):
    list_letter = []
    list_short = []
    list_punct = []
    for key, value in kwargs.items():
        for word in args:
            if key == 'letter':
                if value.upper() in word or value.lower() in word:
                    list_letter.append(word)
            if key == 'short':
                if len(word) <= value:
                    list_short.append(word)
            if key == 'punct':
                if value:
                    if not word.isalpha():
                        list_punct.append(word)
                else:
                    if word.isalpha():
                        list_punct.append(word)
    data = dict()
    if 'key' in kwargs.keys():
        key = kwargs['key']
        list_punct.sort(key=key)
        list_letter.sort(key=key)
        list_short.sort(key=key)
    else:
        list_punct.sort()
        list_letter.sort()
        list_short.sort()
    if list_letter:
        data['letter'] = list_letter
    if list_punct:
        data['punct'] = list_punct
    if list_short:
        data['short'] = list_short

    return data




words = [
    "Through", "giant", "Glass", "windows",
    "river", "cliffs", "Iowa state", "in the old days"
]
params = {
    "letter": "x",
    "punct": False,
    "short": 5,
    "key": len
}
print(borderland(*words, **params))