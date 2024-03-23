import math

with open('data/mereni.txt', encoding='utf-8') as file:
    text = file.read()

print(text)

output = []

with open('data/mereni.txt', encoding='utf-8') as file:
    for line in file:
        day, temp = line.split('\t')
        output.append([day, float(temp)])

print(output)


with open('data/mereni.txt', encoding = 'utf-8') as file:
    total_temp = 0
    count = 0
    for temp in file:
       day, temp = line.split('\t')
       total_temp += float(temp)
       count+= 1
    avg_temp = math.ceil(total_temp / count)

print(avg_temp)