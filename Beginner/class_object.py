#Represent marvel superheroes with classes and objects!
from typing import Self
class Avengers:
    def __init__(self,name,age,gender,super_power,weapon):
        self.name=name
        self.age=age
        self.gender=gender
        self.super_power=super_power
        self.weapon=weapon
    def get_info(self):
        return(f"Name:{self.name}\nAge:{self.age}\nGender:{self.gender}\nSuper_Power:{self.super_power}\nWeapon:{self.weapon}")
    def is_leader(self):
        if self.age>=45:
            return True
super_heroes = [
    {"name": "Captain America", "age": 100, "gender": "Male", "super_power": "Super Strength", "weapon": "Shield"},
    {"name": "Iron Man", "age": 48, "gender": "Male", "super_power": "Technology", "weapon": "Armor"},
    {"name": "Black Widow", "age": 35, "gender": "Female", "super_power": "Superhuman", "weapon": "Batons"},
    {"name": "Hulk", "age": 40, "gender": "Male", "super_power": "Unlimited Strength", "weapon": "No Weapon"},
    {"name": "Thor", "age": 1500, "gender": "Male", "super_power": "Super Energy", "weapon": "Mjölnir"},
    {"name": "Hawkeye", "age": 35, "gender": "Male", "super_power": "Fighting Skills", "weapon": "Bow and Arrows"}
]
for hero_data in super_heroes:
    hero=Avengers(**hero_data)
    print(hero.get_info())
    print(f"{hero.name} is a leader" if hero.is_leader() else f"{hero.name} is not a leader")
