import json

class teacher:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def dict_self 

        



"""     
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
    def to_dict(self):
        return {"make": self.make, "model": self.model, "year": self.year, "image": self.image}

cars = [
    Car("Toyota", "Camry", 2023, "camry_image.jpg"),
    Car("Honda", "Civic", 2022, "civic_image.jpg"),
    Car("Ford", "Mustang", 2021, "mustang_image.jpg")
]

# Convert objects to dictionaries
cars_data = [car.to_dict() for car in cars]

# Save to a JSON file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)
    new_car = Car("Chevrolet", "Malibu", 2024, "malibu_image.jpg")

# Load existing data
try:
    with open("cars.json", "r") as file:
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []

# Append new car
cars_data.append(new_car.to_dict())

# Save updated data back to file
with open("cars.json", "w") as file:
    json.dump(cars_data, file, indent=4)     """
  