class Animal:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Age: {self.age}")


class Cat(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name,breed,age)


class Bear(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name,breed,age)

class Bunny(Animal):
    def __init__(self,name,breed,age):
        super().__init__(name,breed,age)

print("Cat:")
cat = Cat("Cat","Scottish fold cat", 3)
cat.show_info()
print("Bear:")
bear = Bear("Bear","Panda", 8)
bear.show_info()
print("Bunny:")
bunny = Bunny("Bunny","Scottish fold rabbit", 1)
bunny.show_info()
