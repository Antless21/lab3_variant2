class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def show_info(self):
        print(f"Имя студента: {self.name}")
        print(f"Группа: {self.group}")


student = Student("Иван Иванов", "ПИ-21")
student.show_info()