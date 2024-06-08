number = 60

# Implementacja 1
def prime_numbers(number):
    list = []
    i = 2
    for i in range(number):
        if i > 1:
            match = True
            for x in range(2, i):
                if i % x == 0:
                    match = False
                    break
            if match:
                list.append(i)
    return list


def check_prime_divs(number):
    div_list = prime_numbers(number)
    ret_list = []
    work_number = number
    while work_number != 1:
        for divider in div_list:
            if work_number % divider == 0:
                ret_list.append(divider)
                work_number //= divider
    return sorted(ret_list)

# Implementacja 2

def check_prime_divs_2(num):
    ret_list =[]
    work_number = num
    while work_number != 1:
        for divider in range(2, num):
            if work_number % divider == 0:
                ret_list.append(divider)
                work_number //= divider
    return sorted(ret_list)
    

print(check_prime_divs(60))
print(check_prime_divs_2(120))

# generator liczb pierwszych
    
    # i = 2
    # for i in range(number):
    #     if i > 1:
    #         match = True
    #         for x in range(2, i):
    #             if i % x == 0:
    #                 match = False
    #                 break
    #         if match:
    #             print(i)


    
    
    
    
    
    
    
    


