class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            print(f"{animal} додано до зоопарку.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal} видалено з зоопарку.")
        else:
            print(f"{animal} не знайдено в зоопарку.")

    def show_animals(self):
        if self.animals:
            print("Тварини в зоопарку:")
            for animal in self.animals:
                print(animal)
        else:
            print("У зоопарку немає тварин.")


if __name__ == "__main__":
    zoo = Zoo()
    zoo.show_animals()
    zoo.add_animal("Лев")
    zoo.add_animal("Мавпа")
    zoo.add_animal("Слон")
    zoo.show_animals()
    zoo.remove_animal("Страус")
    zoo.remove_animal("Лев")
    zoo.show_animals()
