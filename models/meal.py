from database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    date_time = db.Column(db.DateTime(), nullable=False)
    in_diet = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "date_time": self.date_time.strftime("%Y-%m-%d %H:%M:%S"),
            "in_diet": self.in_diet
        }
