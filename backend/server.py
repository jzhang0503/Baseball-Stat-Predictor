from flask import Flask
from flask import request
import logging
import predict
import json

app = Flask(__name__)
app.debug = True
app.secret_key = 'bruh'

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test')
def test():
    test = request.args.get('test')
    return test

@app.route('/predict')
def predict_avg():
    start_game = request.args.get('start_game')
    end_game = request.args.get('end_game')
    player = request.args.get('player')
    print(start_game)
    print(type(start_game))
    results = predict.predict_avg(player+'.csv',int(start_game), int(end_game))
    predicted_data = {
        "avg": results[0],
        "mse": results[1],
        "mae": results[2]
    }
    print(results)
    return json.dumps(predicted_data)


if __name__ == '__main__':
    app.run(port = 6942, debug = True)
