class Animal:
    def __init__(self,name,color,size):
        self.name = name
        self.color = color
        self.size = size

    def show_info(self):
        print(f"Name: {self.name}, Color: {self.color}, Size: {self.size}")


class Tiger(Animal):
    def __init__(self,name,color,size):
        super().__init__(name,color,size)


class Crocodile(Animal):
    def __init__(self,name,color,size):
        super().__init__(name,color,size)

class Kangaroo(Animal):
    def __init__(self,name,color,size):
        super().__init__(name,color,size)

print("Tiger:")
tiger = Tiger("Tiger","Orange,black and white", "big")
tiger.show_info()
print("Crocodile:")
crocodile = Crocodile("Crocodile","Green", "bigger than tiger")
crocodile.show_info()
print("Bunny:")
kangaroo = Kangaroo("Kangaroo","brown or grey", "smaller than crocodile but bigger than tiger")
kangaroo.show_info()