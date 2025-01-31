from datetime import datetime
from flask import Flask, request, jsonify
from models.meal import Meal
from database import db


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db.init_app(app)
# Session <- conexão ativa


@app.route("/meals/meal", methods=["POST"])
def create_meal():
    data = request.json

    name = data.get("name")
    description = data.get("description")
    date_time = datetime.strptime(data.get("date_time"), "%d/%m/%Y - %H:%M")
    in_diet = data.get("in_diet")

    meal = Meal(
        name=name, description=description, date_time=date_time, in_diet=in_diet
    )
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": "Refeição adicionada com sucesso."})


@app.route("/meals", methods=["GET"])
def get_meals():
    meals = Meal.query.all()
    meals_dict = [meal.to_dict() for meal in meals]
    return jsonify(meals_dict)


@app.route("/meals/meal/<int:id_meal>", methods=["GET"])
def get_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        return meal.to_dict()

    return jsonify({"message": "Refeição não encontrada."}), 404


@app.route("/meals/meal/<int:id_meal>", methods=["PUT"])
def update_meal(id_meal):
    data = request.json
    meal = Meal.query.get(id_meal)

    if meal:
        meal.name = data.get("name")
        meal.description = data.get("description")
        meal.date_time = datetime.strptime(data.get("date_time"), "%d/%m/%Y - %H:%M")
        meal.in_diet = data.get("in_diet")
        db.session.commit()

        return jsonify({"message": f"Refeição {id_meal} atualizada com sucesso."})

    return jsonify({"message": "Refeição não encontrada."}), 404


if __name__ == "__main__":
    app.run(debug=True)
