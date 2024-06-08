import random
size = random.randint(3,9)

print('\nWielkość choinki:', size)
print("Choinka:\n")

for i in range(1, size+1):
    for j in range(i):
        print('*', end='')
    print()
    
print("\nOdwrotna choinka:\n")

for i in range(size, 0, -1):
    for j in range(i):
        print('*', end=('' if j < i - 1 else '\n'))
      
 
print("\nŁadna choinka:\n")

rows = size
leafs = size + size - 1
#  Implementacja 1
for row in range(rows):
    for leaf in range(leafs):
        if leaf < leafs // 2 - row or leaf > leafs // 2 + row:
            print(' ', end=('' if leaf < leafs - 1 else '\n'))
        else:
            print('*', end=('' if leaf < leafs - 1 else '\n'))

#  Implementacja 2
for row in range(rows):
    for leaf in range(leafs):
        if leaf < leafs // 2 - row or leaf > leafs // 2 + row:
            print(' ', end='')
        else:
            print('*', end='')
    print()

#  Implementacja 3
for row in range(rows):
    for leaf in range(leafs):
        endVal = '' if leaf < leafs - 1 else '\n'
        if leaf < leafs // 2 - row or leaf > leafs // 2 + row:
            print(' ', end=endVal)
        else:
            print('*', end=endVal)

#  Implementacja 4
for i in range(1, size+1):
    for _ in range(size - i):
        print(" ", end="")
    for _ in range(2*i - 1):
        print("*", end="")
    print()
