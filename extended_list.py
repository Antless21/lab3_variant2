class ExtendedList(list):
    def total(self):
        return sum(self)

    def even_numbers(self):
        return [number for number in self if number % 2 == 0]


numbers = ExtendedList([1, 2, 3, 4, 5])

print("Исходный список:", numbers)

numbers.append(6)

print("После добавления:", numbers)
print("Сумма элементов:", numbers.total())
print("Чётные числа:", numbers.even_numbers())