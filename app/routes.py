from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name=request_body["name"],
        description=request_body["description"],
        radius=request_body["radius"],
        # atmosphere=request_body["atmosphere"]
    )
    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planets_bp.route("", methods=["GET"])
def list_planets():
    planets = Planet.query.all()
    response = []
    for planet in planets:
        response.append(
            {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "radius": planet.radius,
            # "atmosphere": planet.atmosphere
            }
        )
    return jsonify(response)

# class Planet:
#     def __init__(self, id, name, description, radius, atmosphere):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.radius = radius
#         self.atmosphere = atmosphere


# planets = [
#     Planet(1, "Mercury", "", 1516, ["oxygen", "sodium", "hydrogen", "helium", "potassium"]),
#     Planet(2, "Venus", "", 3760, ["carbon dioxide", "nitrogen", "sulfur dioxide"]),
#     Planet(3, "Earth", "", 3959, ["nitrogen", "oxygen", "argon", "carbon dioxide"]),
#     Planet(4, "Mars", "", 2106, ["carbon dioxide", "nitrogen", "argon", "oxygen"]),
#     Planet(5,"Jupiter","", 43441, ["hydrogen", "helium", "methane", "ammonia"]),
#     Planet(6, "Saturn", "", 36184, ["hydrogen", "helium", "methane", "ammonia"]),
#     Planet(7, "Uranus", "", 15759, ["hydrogen", "helium", "methane"]),
#     Planet(8, "Neptune","", 15299, ["hydrogen","helium","methane"])
# ]



# @planets_bp.route("/<planet_id>", methods=["GET"])
# def get_one_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         response_str = f"Invalid planet_id '{planet_id}'. ID must be an integer"
#         return jsonify({"message": response_str}), 400
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id,
#                 "name": planet.name,
#                 "description": planet.description,
#                 "radius": planet.radius,
#                 "atmosphere": planet.atmosphere
#             }

#     response_str = f"Invalid planet_id '{planet_id}'. ID not found"
#     return jsonify({"message": response_str}), 404
