from flask import Flask
import predict

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/predict')
def predict_avg():
    # start_game = Flask.request.args.get('start_game')
    # end_game = Flask.request.args.get('end_game')
    # data = Flask.request.args.get('data')
    results =predict.predict_avg(1,10, 'ohtani.csv')
    data = {
        "avg": results[0],
        "mse": results[1],
        "mae": results[2]
    }
    return data


if __name__ == '__main__':
    app.run(port = 6942, debug = True)
