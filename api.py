import pandas as pd
from sklearn.externals import joblib
import traceback
from flask import Flask,request, jsonify

#Flask instance
app = Flask('IrisTestModel')


#url to redirect the method call
@app.route('/python-api-model/predict',methods=['POST'])
def predict():
    if model:
        try:
            #read the data and created a data frame for the which model needs to predict
            query = pd.DataFrame(request.json)
            prediction = list(model.predict(query))

            return jsonify({'prediction': str(prediction)})  #Retuns the prediction in json format.

        except:

            return jsonify({'trace': traceback.format_exc()})
    else:
        return ('model missing')




# default port will be set at 12345
print('Loading the saved model')
model = joblib.load("model.pkl")
print('Model Loaded')
app.run(port=12345, debug=True)


