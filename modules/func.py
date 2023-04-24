def filter_array(array):
  if(len(array) > 0):
    output_array = []
    for el in array:
      if (len(el) <= 3):
        output_array.append(el)
    return output_array
  else: print("Исходный массив должен содержать данные")