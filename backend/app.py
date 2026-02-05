from flask import Flask
from routes.home import home
from routes.recommend import recommend
from utils.loaders import load_json
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "destinations.json")

destinations = load_json(DATA_PATH)

app.add_url_rule("/", "home", home)
app.add_url_rule("/recommend", "recommend", lambda: recommend(destinations), methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
