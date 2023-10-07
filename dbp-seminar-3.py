#1
def palindrome(value):
    value_str = str(value)
    reversed_str = value_str[::-1]
    return value_str == reversed_str

#2
def count_upper_and_lower(lst):
    upper_count = 0
    lower_count = 0
    for string in lst:   
        for char in string:       
            if char.upper():
                upper_count += 1    
            elif char.lower():
                lower_count += 1
    return upper_count, lower_count

#3

def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

#4
def factorial(n):
    result = 1
    if n < 0:
        return "Сөрөг тоо байна."
    elif n == 0:
        return 1
    for i in range(1, n + 1):
        result *= i
    return result

#5
def reverse_list(lst):
    reversed_lst = lst[::-1]
    return reversed_lst

#6
def sum_of_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

#7
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#8
def ccc(x,y,z):
    if x>y>z:
        return x
    elif y>z>x:
        return y
    else:
        return z
