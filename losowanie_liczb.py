import random

stars_amount = random.randint(5, 50)
# losuje liczbę z przedziału odustronnie domkniętego [5, 50]

print(f"Ilość gwiazd: {stars_amount}")
for i in range(stars_amount):
    print('*', end='')
