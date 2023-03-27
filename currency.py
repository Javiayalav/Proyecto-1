#Final pr
yuan = 560
yen = 2455
won = 3280
usd = (yuan * 0.15) + (yen * 0.0076) + (won * 0.00077)
#usd = 105.18
print("what do you have left in yuan? 560")
print("what do you have left in yen? 2455")
print("what do you have left in won? 3280")

print(usd)

yuan = int(input('What do you have left in yuan? '))
yen = int(input('What do you have left in yen? '))
won = int(input('What do you have left in won? '))

total = yuan * 0.15 + yen * 0.0077 + won * 0.00080

print(total)
