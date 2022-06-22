import json

from flask import Flask, request

from transformers import pipeline

#sentiment_analysis = pipeline("sentiment-analysis", model="rabindralamsal/BERTsent")
model_path = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
sentiment_analysis = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)
app = Flask(__name__)

@app.route("/detect_sentiment", methods=['POST'])
def detect_sentiment():
    print('hello')
    print('hello')
    data_text = request.form.get('data_text')
    data = request.get_json(force=True)
    print(request.get_json())
    print(data["data_text"])
    res = sentiment_analysis(data["data_text"])
    return json.dumps(res[0])
    #return json.dumps({"meg": data_text})

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
