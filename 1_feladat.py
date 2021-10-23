# osszegezzuk a matrix minden elemet

m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]
sum = 0

# print(f'Sorok: {len(m)}')
# print(f'Oszlopok: {len(m[1])}')

for elem in m:
    for i in range(0, len(m[1])):
        sum = sum + elem[i]

print(f'Összeg: {sum}')
