class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print("Animal is speaking")

    def get_info(self):
        animal_type = type(self).__name__
        return f'This {animal_type} is {self.age} year(s) old and its color is {self.color}'


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def speak(self):
        print("Dog says wow-wow")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)
    
    def speak(self):
        print("Cat says meow-meow")

class Cow(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, color)

    def speak(self):
        print("Cow says moow-moow")


cow1 = Cow("reks", 4, 'yellow')
cow1.speak()
print(cow1.get_info())

