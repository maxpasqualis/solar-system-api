from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    radius = db.Column(db.Integer)
    # atmosphere = db.Column()

    def to_dict(self):
        planet_dict = {
            "id": self.id,
            "name" :self.name,
            "radius": self.radius, 
            "description": self.description 
        }
        return planet_dict

    @classmethod
    def from_dict(cls, data_dict):
        if "name" in data_dict and "radius" in data_dict and "description" in data_dict:
            new_object = cls(name=data_dict["name"], 
            radius=data_dict["radius"], 
            description=data_dict["description"])
            
            
            return new_object