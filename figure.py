class Figure:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


figure = Figure(5, 3)

print("Ширина:", figure.width)
print("Высота:", figure.height)
print("Площадь:", figure.area())
print("Периметр:", figure.perimeter())