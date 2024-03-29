numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# print(numbers[4])
# len_ = len(numbers)
# print(len_)
# numbers[4] = 0
# sum_ = sum(numbers)
# print(sum_)
# avg = sum_ / len_
# print(avg)
# numbers[4] = avg
# print("Измененный список:", numbers)

len_ = len(numbers)
numbers.remove(None)
sum_ = sum(numbers)
avg_ = sum_ / len_
numbers.insert(4, avg_)
print("Измененный список:", numbers)

