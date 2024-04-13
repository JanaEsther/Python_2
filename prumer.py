import math

numbers = [10.5, 14.1, 124.5, 10.9, 11.2, 19.3, 17.6, 25.1, 36.7, 4.5, 17.9]
soucet = 0
for n in numbers:
    soucet += n

avg = soucet/len(numbers)

print(math.ceil(avg))