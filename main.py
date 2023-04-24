# Задача: Написать программу, которая из имеющегося массива строк
# формирует новый массив из строк, длина которых меньше, либо равна 3 символам.
# Первоначальный массив можно ввести с клавиатуры,
# либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
# Примеры:
# [“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
# [“1234”, “1567”, “-2”, “computer science”] → [“-2”]
# [“Russia”, “Denmark”, “Kazan”] → []
import sys
from modules.func import filter_array
from modules.request_array import requsetArrayFromUser

input_user_array = requsetArrayFromUser()
print(filter_array(input_user_array))
print("Для выхода нажмите Enter")
print(sys.stdin.readline())
