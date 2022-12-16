import sys

print(not all([all(map(int, i.split())) for i in [x.rstrip("\n") for x in sys.stdin.readlines()]]))
