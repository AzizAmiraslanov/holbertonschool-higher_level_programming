#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    unique_numbers = []

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)
            total += number

    return total
