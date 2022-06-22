import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/home', methods=['GET'])
def home():
    print('hi')
    # return jsonify(message=str("index.html"))
    language = "Python"
    company = "Oreivaton"
    Itemid = 1
    price = 0.00

    # Create Dictionary
    value = {
        "language": language,
        "company": company,
        "Itemid": Itemid,
        "price": price
    }
    return json.dumps(value)


if __name__ == "__main__":
    from waitress import serve

    serve(app, host="0.0.0.0", port=8082)
