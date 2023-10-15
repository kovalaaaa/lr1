numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
index = numbers.index(None)
str_1 = numbers[: index]
str_2 = numbers[index+1:]
str_ = str_1+str_2
new = sum(str_)/len(numbers)
numbers[index] = new

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
