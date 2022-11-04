from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, request, abort, make_response

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except:
#         abort(make_response({"message": f"Invalid planet id {planet_id}: id must be an integer"}, 400))
    
#     planet = Planet.query.get(planet_id)
#     if not planet:
#         abort(make_response({"message": f"Planet with id {planet_id} does not exist"}, 404))
    
#     return planet

def validate_obj(cls, obj_id):
    try:
        obj_id = int(obj_id)
    except:
        abort(make_response({"message": f"Invalid {cls.__name__} id {obj_id}: id must be an integer"}, 400))
    
    object = cls.query.get(obj_id)
    if not object:
        abort(make_response({"message": f"{cls.__name__} with id {obj_id} does not exist"}, 404))
    
    return object

@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planets_bp.route("", methods=["GET"])
def list_planets():
    name_param = request.args.get("name")
    if name_param is None:
        planets = Planet.query.all()
    else:
        planets = Planet.query.filter_by(name=name_param)

    response = []
    for planet in planets:
        response.append(planet.to_dict())
    return jsonify(response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def get_one_planet(planet_id):
    planet = validate_obj(Planet, planet_id)
    return {
        "id": planet.id,
        "name": planet.name,
        "description": planet.description,
        "radius": planet.radius
    }, 200

@planets_bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_obj(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.radius = request_body["radius"]

    db.session.commit()
    return make_response(f"Planet with id {planet_id} successfully updated"), 200

@planets_bp.route("/<planet_id>", methods = ["DELETE"])
def delete_planet(planet_id):
    planet = validate_obj(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return make_response(f"Planet with id {planet_id} successfully deleted"), 200

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
