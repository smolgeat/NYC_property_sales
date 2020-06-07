from flask import Flask
import request
import json
import pickle
app = Flask(__name__)


@app.route('/predict', methods=['GET'])
def load_models():
    """Load model from pickel file"""
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


def predict():
    """takes features via request. Makes prediction using features
        returns prediction as a response"""
    # parse input features from request
    request_json = request.get_json()
    x = float(request_json['Block', 'Gross Square Feet', 'Lot',
                           'Zipcode', 'Land Square Feet', 'Year Built',
                           'Sale Date'])

    # load model
    model = load_models()
    prediction = model.predict([[x]])[0]
    response = json.dumps({'response': prediction})
    return response, 200


if __name__ == '__main__':
    application.run(debug=True)
