from flask import Blueprint

class Planet:
    def __init__(self, id, name, description, radius, atmosphere):
        self.id = id
        self.name = name
        self.description = description
        self.radius = radius
        self.atmosphere = atmosphere

planets = [
    Planet(1, "Mercury", "", 1516, ["oxygen", "sodium", "hydrogen", "helium", "potassium"]),
    Planet(2, "Venus", "", 3760, ["carbon dioxide", "nitrogen", "sulfur dioxide"]),
    Planet(3, "Earth", "", 3959, ["nitrogen", "oxygen", "argon", "carbon dioxide"])
    Planet(4, "Mars", "", 2106, ["carbon dioxide", "nitrogen", "argon", "oxygen"]),
    Planet(5,"Jupiter","", 43441, ["hydrogen", "helium", "methane", "ammonia"]),
    Planet(6, "Saturn", "", 36184, ["hydrogen", "helium", "methane", "ammonia"]),
    Planet(7, "Uranus", "", 15759, ["hydrogen", "helium", "methane"]),
    Planet(8, "Neptune","", 15299, ["hydrogen","helium","methane"])
]