class Zoo:
    def __init__(self, animals):
        self.animals = animals
    
    def remove_at_index(self, index):
        if 0 <= index < len(self.animals):
            self.animals.pop(index)
    
    def add_animal(self, animal):
        self.animals.append(animal)
    
    def remove_first(self):
        if self.animals:
            self.animals.pop(0)
    
    def print_all_animals(self):
        print(self.animals)
        for animal in self.animals:
            print(animal)
    
    def print_first_n(self, n):
        print(self.animals[:n])
        for i in range(min(n, len(self.animals))):
            print(self.animals[i])

# Usage
zoo = Zoo(["Monkey", "Zebra", "Gorilla", "Lion", "Tiger"])
zoo.remove_at_index(3)
zoo.add_animal("Lizard")
zoo.remove_first()
zoo.print_all_animals()
zoo.print_first_n(3)


