#  Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
from random import randint

def get_list(n, frst, last):
    return [randint(frst, last) for i in range(n)]

def sum_odd_position(mylist):
    return sum(mylist[1::2])

n = 10
frst = 1
last = 10

mylist = get_list(n, frst, last)
print(mylist)
print(sum_odd_position(mylist))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0]*numbers[-1])
        del numbers[0] 
        del numbers[-1] 
    if len(numbers) ==1: results.append(numbers[0]**2)       
    return results

print(pairs_mult(mylist))

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform

def get_real_nums (n, frst, last):
    return [round(uniform(frst,last), 2) for i in range(n)]

def find_diff(mynums):
    nums = [round(x - int(x), 2) for x in (mynums)]
    return max(nums) - min(nums)

n = 5
frst = 1
last = 10
mynums = get_real_nums(n, frst, last)

print (mynums)
print(find_diff(mynums))

#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input('Введите число: '))

def conv_dec_to_bin(n):
    bin_num = ''
    while n > 1:
        bin_num += str(n % 2)
        n = n // 2
    return bin_num[::-1]

print(conv_dec_to_bin(n))

# Другие решения

def convert_dec_to_bin(n):
    bin_num = []
    while n > 1:
        bin_num.insert(0, n % 2)
        n = n // 2
    return bin_num

print(convert_dec_to_bin(n))

print(bin(n).replace('0b1',''))

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))

