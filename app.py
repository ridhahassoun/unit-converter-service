from flask import Flask, render_template, request
from flask_cors import CORS
from conversions import types

app = Flask(__name__)
CORS(app)


def process_data(data):
    conversion_dict = types[data["type"]]
    conversion_from = conversion_dict[data["from"]["units"]]
    conversion = conversion_from[data["to"]]

    value = data["from"]["value"]
    if not (isinstance(value, int) or isinstance(value, float)):
        raise TypeError

    if data["type"] == "temp":
        result = conversion(value)
    else:
        result = conversion * data["from"]["value"]

    data["result"] = result

    return data


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/", methods=["POST"])
def api():
    if request.method == "POST" and request.mimetype == "application/json":
        data = request.get_json(silent=True)
        if data:
            try:
                if "multiple" in data:
                    number_of_conversions = len(data) - 1
                    for index in range(number_of_conversions):
                        processed_data = process_data(data[str(index)])
                        data[str(index)] = processed_data
                    return data
                else:
                    return process_data(data)
            except KeyError as e:
                return {"Error":
                        "Invalid value ({}) used. Check syntax/docs".format(e)}
            except TypeError:
                return {"Error":
                        "Value passed not of type int or float."}

        else:
            return {"Error":
                    "Could not parse JSON. Check syntax."}
    else:
        return {"Error":
                "Invalid data. Please ensure type is 'application/json'."}


@app.errorhandler(400)
def handle_bad_request(e):
    return {"Error": "Bad request"}, 400
