from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/novidades")
def novidades():

    try:

        with open(
            "updates.json",
            "r",
            encoding="utf-8"
        ) as file:

            updates = json.load(file)

    except:

        updates = []

    return jsonify(updates)

if __name__ == "__main__":
    app.run()