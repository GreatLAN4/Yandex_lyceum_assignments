from sys import stdin
from random import choice

friend_list = []
secret_friend = []
secret_santa = []
for friend in stdin:
    friend_list.append(friend.strip("\n"))
    secret_friend.append(friend.strip("\n"))

for i in friend_list:
    a = choice(secret_friend)
    if i == a:
        A = a
        secret_friend.remove(a)
        a = choice(secret_friend)
        secret_friend.append(A)

    if i != a:
        secret_santa.append(i)
        secret_santa.append(a)
        secret_friend.remove(a)

for i in range(len(friend_list)):
    print(list(secret_santa[::2])[i], "-", list(reversed(list(reversed(secret_santa))[::2]))[i])
# print(secret_santa)
# print(secret_santa[::2])
# print(list(reversed(list(reversed(secret_santa))[::2])))
