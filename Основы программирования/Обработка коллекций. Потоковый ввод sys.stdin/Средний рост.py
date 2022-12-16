import sys
M = list(map(lambda x: int(x), map(str.strip, sys.stdin)))
if not M:
    print("-1")
else:
    print(sum(M) / len(M))
