from cs50 import get_float
# TODO

quarter = 0
dime = 0
nickel = 0
penny = 0
coins = 0
change = 0

while change < 1:
    change = get_float("Change: ") * 100

change = round(change, 2)

while change >= 25:
    coins += 1
    quarter += 1
    change = change - 25
    print(quarter)

while change >= 10:
    coins += 1
    dime += 1
    change = change - 10


while change >= 5:
    coins += 1
    nickel += 1
    change = change - 5


while change >= 1:
    coins += 1
    penny += 1
    change = change - 1


print(coins)