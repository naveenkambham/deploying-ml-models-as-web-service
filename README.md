## flasking machine learning models
Using FLask to creat a Web API for a trained machine learning model to persist the model learning state and use it for predictions on the go. Since the focus of this project is to demonstrate the model integration to a website, a basic support vector machines model for predicting iris type is used.

Major steps involved are:
1) Create a model
2) Dump the trained model using Joblib or pickle, Joblib is efficient when the datasize is more and numpy arrays are involved.
3) Create a Flask API to receive the request from Website
4) Read the Json request in to a data frame. Please note that shape of the input needs to be same as the shape of the input features used while training model.
5) Load the persisted model
6) Predict using the loaded model and return the prediction in Json format.
