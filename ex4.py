import random

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
total = d1 + d2

#名前を聞く
name = input("What is your name? ")

#ダイスの出力
print("Hello, {0}!".format(name))
print("Rolling the dice...")
print("Die 1: %d" % d1)
print("Die 2: %d" % d2)
print("Total value: %d" % total)
