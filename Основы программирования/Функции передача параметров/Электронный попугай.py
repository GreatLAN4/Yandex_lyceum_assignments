phrases = []


def parrot(phrase):
    if phrase in phrases:
        print(phrase)
    else:
        phrases.append(phrase)
