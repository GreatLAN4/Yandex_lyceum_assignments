from sys import stdin

the_word = [i for i in input()]
cash = []
result = []
for word in stdin:

    for letter in word.rstrip("\n"):
        Pass = True

        if letter in the_word:
            the_word.remove(letter)
            cash.append(letter)

        else:
            Pass = False
            break

    if Pass:
        result.append(word.rstrip("\n"))
    the_word = the_word + cash
    cash = []

print(len(result))
for i in result:
    print(i)
