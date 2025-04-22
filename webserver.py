from flask import Flask, request
import json

app = Flask(__name__)
DATA_PATH = "/data/storage.json"

def load_data():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    data = load_data()
    queue = data["queue"]
    if not queue:
        data["queue"] = data["hebdo"].copy()
        queue = data["queue"]

    day_counter = data.get("day_counter", 0)
    task = queue[0] if queue else "Aucune tâche disponible"

    if day_counter % 4 == 0 and data["mensuel"]:
        task = f"[Mensuelle] {data['mensuel'][day_counter % len(data['mensuel'])]}"

    html = f"""
    <html>
    <head>
        <title>Ménage</title>
        <style>
        body {{ font-family: sans-serif; text-align: center; padding-top: 50px; }}
        h1 {{ font-size: 24px; }}
        button {{ padding: 10px 20px; font-size: 16px; margin: 10px; }}
        </style>
    </head>
    <body>
        <h1>Tâche du jour :</h1>
        <p>{task}</p>
        <form method="post" action="/done"><button>Fait</button></form>
        <form method="post" action="/skip"><button>Passer</button></form>
    </body>
    </html>
    """
    return html

@app.route("/done", methods=["POST"])
def done():
    data = load_data()
    if data["queue"]:
        task = data["queue"].pop(0)
        data["queue"].append(task)
    data["day_counter"] += 1
    save_data(data)
    return ("", 302, {"Location": "/"})

@app.route("/skip", methods=["POST"])
def skip():
    data = load_data()
    data["day_counter"] += 1
    save_data(data)
    return ("", 302, {"Location": "/"})