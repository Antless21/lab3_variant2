class Animal:
    def speak(self):
        raise NotImplementedError("Метод должен быть переопределён")


class Dog(Animal):
    def speak(self):
        return "Гав!"


class Cat(Animal):
    def speak(self):
        return "Мяу!"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()


        else:
            raise ValueError("Неизвестный вид животного")
dog = AnimalFactory.create_animal("dog")
cat = AnimalFactory.create_animal("cat")

print("Собака говорит:", dog.speak())
print("Кошка говорит:", cat.speak())