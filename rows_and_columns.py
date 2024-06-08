rows = 5
columns = 10

print("Implementacja 1:")
for row in range(rows):
    for col in range(columns):
        print('*', end=('' if col < columns - 1 else '\n'))


print("Implementacja 2:")
for row in range(rows):
    for col in range(columns):
        print('*', end='')
    print()