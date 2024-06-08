import random

# Zad 1 napisz funkcje która przyjmie jeden argument bedący listą stringów,
# funkcja ma zwrócic liste intów która bedzie zawierała długość odpowiednich stringów
print("\nZadanie 1:")

strList = ['Ala', 'Ola', 'Karol', 'Bogdan', 'StółZPowyłamywanymiNogami']

def len_of_strings(iter_arr):
    ret_list = []
    for item in iter_arr:
        ret_list.append(len(item))
    return ret_list


print(len_of_strings(strList))

# Zad 2 napisz funkcja która zwróci wszystkie dzielniki zadanej liczby w liscie
print("\nZadanie 2:")

num_a = 60

def dividers(number):
    dividers_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            dividers_list.append(i)
    return dividers_list


print(dividers(num_a))

# Zad 3 napisz funkcje która narysuje linie. Funkcja ma przyjmować dwa parametry, pierwsy to długość lini
# drugi to znaki z jakich ma funkcja wybierać symbol do rysowania lini. funkcja wybiera znaki losowo z
# równym prawdopodobieństwem
print("\nZadanie 3:")

length = 5
chars = '#*$'

def draw_line(line_length, char_set):
    for i in range(line_length):
        # random_char = random.choice(chars)
        random_char = char_set[random.randint(0, len(char_set) - 1)]
        print(random_char, end='')


draw_line(length, chars, )
print()

# Zad 4 napisz funkcje która przyjmuje jeden argument. Ten argument bedzie listą
# stringów, funkcja ma zliczyć ilośc wystąpień stringów o długość większej niż 2
# które zaczynają sie i konczą na tą samą litere
print("\nZadanie 4:")

list_of_strings = ['ala', 'ma', 'piegi']

def strings_grater_than(iter_arr, number):
    count = 0
    for item in iter_arr:
        if len(item) > number:
            count += 1
    return count


print(strings_grater_than(list_of_strings, 2))

# Zad 5 napisz funkcje która przyjmie jako parametr liste list, każda z tych list
# bedzie składać sie ze stringów. Funkcja ma zwrócić ilosc wystopien litery
# p we wszystkich tych stringach
print("\nZadanie 5:")

list_of_lists = [
    ["dziecko", "papier"],
    ["kopia", "zderzak"],
    ["kpina", "SAMOCHÓD"],
    ["pierwszeństwo przejazdu"]
]

def check_amount_of_p(arr_in_arr):
    for str_set in arr_in_arr:
        for item in str_set:
            counter = 0
            for ch in item:
                if ch == 'p':
                    counter += 1
            print(f"'{item}' ma {counter}")
            

check_amount_of_p(list_of_lists)

# Zad 6 napisz funkcje która przyjmie dwa parametry, pierwszy słownik, drugi tuple.
# funkcja ma za zadanie dodanie do słownika klucza który znajduje sie pod 0 indexem
# w tupli o wartość z indexu 1.
print("\nZadanie 6:")

tup_a = ("ala", ["ma kota"])
tup_b = ("ola", ["ma piegi"])
dict_a = {}

def add_key_value(dict, tup):
    list_of_keys = dict.keys()
    if tup[0] in list_of_keys:
        # dict[tup[0]].append(tup[1])
        dict[tup[0]] += tup[1]
    else:
        dict[tup[0]] = tup[1]


add_key_value(dict_a, tup_a)
add_key_value(dict_a, tup_a)
add_key_value(dict_a, tup_b)

print(dict_a)

# Zad 7 napisz funkcję która bedie wyliczać pierwiastek liczby, z zadaną
# dokłdnościa
print("\nZadanie 7:")

def sqrt(n, dec_place):
    ret_value = n ** 0.5
    return round(ret_value, dec_place)


print(sqrt(93, 2))

# Zad 8 napisz funkcję, która wyznaczy wszystkie dzielniki pierwsze liczby
print("\nZadanie 8:")

number = 60

    # Implementacja 1
def prime_numbers(num):
    list = []
    i = 2
    for i in range(num):
        if i > 1:
            match = True
            for x in range(2, i):
                if i % x == 0:
                    match = False
                    break
            if match:
                list.append(i)
    return list

def check_prime_divs(num):
    div_list = prime_numbers(num)
    ret_list = []
    work_number = num
    while work_number != 1:
        for divider in div_list:
            if work_number % divider == 0:
                ret_list.append(divider)
                work_number //= divider
    return sorted(ret_list)

    # Implementacja 2
def check_prime_divs_2(num):
    ret_list = []
    work_number = num
    while work_number != 1:
        for divider in range(2, num):
            if work_number % divider == 0:
                ret_list.append(divider)
                work_number //= divider
    return sorted(ret_list)


print(check_prime_divs(number))
print(check_prime_divs_2(120))