import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__,template_folder="template",static_folder='Static Files')  # assign Flask = app
model = pickle.load(open('build.pkl','rb'))  ### import model 

@app.route('/')
def home():
    return render_template('index.html')  ## read index.html file 

@app.route('/predict',methods=['POST'])  # transfer data from html to python / server
def predict():
    int_features  = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = np.round(prediction[0],4)
    return render_template('index.html',prediction_text="premium will be {}".format(math.floor(output)))


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
