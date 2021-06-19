import numpy as np
from flask import Flask, request
from predict import get_trained_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    json = request.get_json(force=True)
    features = json['features']
    substances = json['substances']

    inputs = np.array([features + substances])

    model = get_trained_model()
    labels = model.predict(inputs)

    return {
        'status': 1,
        'labels': labels.tolist(),
    }

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
