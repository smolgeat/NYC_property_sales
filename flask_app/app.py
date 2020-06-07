from flask import Flask,request,jsonify
import json
import pickle
import pandas as pd
from zipfile import ZipFile
app = Flask(__name__)

def load_models():
    """Load model from pickel file"""
    with ZipFile('models/model.zip') as myzip:
        with myzip.open('model_file.p') as myfile:
            data = pickle.load(myfile)
            model = data['model']
            return model


@app.route('/predict', methods=['GET'])
def predict():
    """takes features via request. Makes prediction using features
        returns prediction as a response"""
    # parse input features from request
    request_json = request.get_json()
    print(request_json)
    # x=request_json['BLOCK','GROSS SQUARE FEET','LOT','ZIP CODE','LAND SQUARE FEET','YEAR BUILT']
    df= pd.DataFrame(request_json,index=[0])
    
    #load model
    model = load_models()
    prediction = model.predict(df)[0]
    response = json.dumps({'Sale Price Prediction': prediction})
    return response,200


if __name__ == '__main__':
    app.run(port=3000,debug=True)# for local development
    #application.run(debug=True)

"""
Sample request
curl -X GET http://0.0.0.0:3000/predict -H "Content-Type: application/json" -d '{"BLOCK":"400","GROSS SQUARE FEET":"4000","LOT":"500","ZIP CODE":"1092","LAND SQUARE FEET":"3000","YEAR BUILT":"1995"}'
"""


