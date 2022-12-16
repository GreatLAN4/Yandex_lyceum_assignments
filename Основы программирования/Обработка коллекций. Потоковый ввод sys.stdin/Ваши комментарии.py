import sys
count = 0
for line in sys.stdin:
    if line.find("#"):
        count += 1

print(count)