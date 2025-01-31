from datetime import datetime 
from flask import Flask, request, jsonify
from models.meal import Meal
from database import db


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db.init_app(app)
# Session <- conexão ativa


@app.route("/meal", methods=["POST"])
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


if __name__ == "__main__":
    app.run(debug=True)
