# Задача: Написать программу, которая из имеющегося массива строк
# формирует новый массив из строк, длина которых меньше, либо равна 3 символам.
# Первоначальный массив можно ввести с клавиатуры,
# либо задать на старте выполнения алгоритма.
# При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
# Примеры:
# [“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
# [“1234”, “1567”, “-2”, “computer science”] → [“-2”]
# [“Russia”, “Denmark”, “Kazan”] → []
input_array = ['Hello', '2', 'world', ':-)']
input_array_2 = ['1234', '1567', '-2', 'computer science']
input_array_3 = ['Russia', 'Denmark', 'Kazan']
input_array_empty = []

def filter_array(array):
  if(len(array) > 0):
    output_array = []
    for el in array:
      if (len(el) <= 3):
        output_array.append(el)
    return output_array
  else: print("Исходный массив должен содержать данные")


print(filter_array(input_array_empty))
