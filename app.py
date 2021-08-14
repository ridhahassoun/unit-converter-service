from flask import Flask, render_template, request
from flask_cors import CORS
from conversions import types

app = Flask(__name__)
CORS(app)


def process_data(data):
    # gets appropriate conversion dict
    # see conversions.py
    conversion_table = types[data["type"]]
    unit_converting_from = conversion_table[data["from"]["units"]]
    conversion_factor = unit_converting_from[data["to"]]

    value = data["from"]["value"]
    if not (isinstance(value, int) or isinstance(value, float)):
        # only dealing with numbers here
        raise TypeError

    if data["type"] == "temp":
        # temperature conversion is more complex, so requires a lambda function
        # stored in conversions.py, hence the function call
        result = conversion_factor(value)
    else:
        # everything else is simply multiplying by ratio
        result = conversion_factor * data["from"]["value"]

    data["result"] = result

    return data


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/", methods=["POST"])
def api():
    if request.method == "POST" and request.mimetype == "application/json":
        data = request.get_json(silent=True)  # silent to force parsing
        if data:
            try:
                if "multiple" in data:
                    # if multiple flag set, we loop through object and convert
                    number_of_conversions = len(data) - 1
                    for index in range(number_of_conversions):
                        processed_data = process_data(data[str(index)])
                        data[str(index)] = processed_data
                    return data
                else:
                    # just perform one conversion
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
