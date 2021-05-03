class Animal:
    cool = True

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} palys with {self.toy}")


# blue = Cat("Blue", "Scottish Fold", "String")
# blue.make_sound("MEOW")
# # print(blue.cool)
# # print(Cat.cool)
# # print(Animal.cool)

# print(isinstance(blue, object))

blue = Cat("Blue", "Scottish Fold", "String")
blue.play()
blue.make_sound("MEOW")
