import sys

data = list(map(str.strip, sys.stdin))
ch_set = set()
nech_set = set()
for i in range(len(data)):
    str = data[i].split()
    if (i + 1) % 2 == 0:
        for word in str:
            if word[0] == word[0].upper():
                ch_set.add(word)
    else:
        for word in str:
            nech_set.add(word)

print("; ".join(nech_set))
print("; ".join(ch_set))
