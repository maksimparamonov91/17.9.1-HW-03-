sequence_number = input("Введите последовательность чисел через пробел:") #type str

number = int(input("Введите любое число:")) #type int

# 1. Преобразование введённой последовательности в список intов

li_sequence_number = sequence_number.split()
# print(li_sequence_number)
in_li_sequence_number = list(map(int, li_sequence_number))
# print(in_li_sequence_number)

# 2. Сортировка списка по возрастанию элементов в нем.
sor_in_li_sequence_number = sorted(in_li_sequence_number)
print(sor_in_li_sequence_number)

# 3.
def binary_search(array, element, left, right):
     if left > right: # если левая граница превысила правую,
         return False # значит элемент отсутствует

     middle = (right+left) // 2 # находимо середину
     if int(array[middle]) == element: # если элемент в середине,
         return middle # возвращаем этот индекс
     elif element < int(array[middle]): # если элемент меньше элемента в середине
         # рекурсивно ищем в левой половине
         return binary_search(array, element, left, middle-1)
     else: # иначе в правой
         return binary_search(array, element, middle+1, right)


indx_number = binary_search(sor_in_li_sequence_number, number, 0, len(sor_in_li_sequence_number))
print('индекс введеного числа в списке:', indx_number)
indx = sor_in_li_sequence_number.index(sor_in_li_sequence_number[indx_number-1])
print('индекс меньшего чем введеное число в списке:', indx)
# print(type(sor_in_li_sequence_number))