import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
total = d1 + d2

print("Rolling the dice...")
print("Die 1: %d" % d1)
print("Die 2: %d" % d2)
print("Total value: %d" % total)

#勝ち負け判定
if total > 7:
    print(name + " won!")
else:
    print(name + " lost...")
