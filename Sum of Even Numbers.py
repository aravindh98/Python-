# Sum of Even Numbers

total = 0
for number in range(2, 101):
  if number % 2 == 0:
    total = total + number

print(total)
