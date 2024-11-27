#polymorphism
class Animal:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Dog(Animal):
    def move(self):
        return "Running"

class Cat(Animal):
    def move(self):
        return "Jumping"

class Bird(Animal):
    def move(self):
        return "Flying"


# Function to demonstrate polymorphism
def animal_movement(animals):
    for animal in animals:
        print(animal.move())

# Creating instances of animals
dog = Dog()
cat = Cat()
bird = Bird()

# List of animals
animals = [dog, cat, bird]

# Demonstrating polymorphism
print("\nAnimal Movements:")
animal_movement(animals)