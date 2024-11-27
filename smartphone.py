# smartphone.py

class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def make_call(self, contact):
        return f"Calling {contact} from {self.brand} {self.model}..."

    def take_photo(self):
        return f"Taking a photo with {self.brand} {self.model}..."

    def display_info(self):
        return (f"Smartphone Info:\n"
                f"Brand: {self.brand}\n"
                f"Model: {self.model}\n"
                f"Storage: {self.storage} GB\n"
                f"Battery Life: {self.battery_life} hours")


class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu  # Graphics Processing Unit

    def play_game(self, game):
        return f"Playing {game} on {self.brand} {self.model} with {self.gpu} GPU!"


# Example usage of the Smartphone classes
if __name__ == "__main__":
    # Creating an instance of Smartphone
    my_phone = Smartphone("Apple", "iPhone 14", 128, 20)
    print(my_phone.display_info())
    print(my_phone.make_call("Alice"))
    print(my_phone.take_photo())

    # Creating an instance of GamingSmartphone
    gaming_phone = GamingSmartphone("Asus", "ROG Phone 5", 256, 18, "Adreno 660")
    print(gaming_phone.display_info())
    print(gaming_phone.play_game("PUBG Mobile"))