from flask import Flask

app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:morgan8514@127.0.0.1:5432/alpha_vantage"
app.config["SECRET_KEY"]="secret"

db = SQLAlchemy(app)

@app.before_first_request
def create():
    db.create_all()

# importing db
from models.alpha import Forex

@app.route("/")
def home():

    return "home"




if __name__ == "__main__":
    app.run()