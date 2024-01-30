# app.py

from flask import Flask, request, render_template
import pickle
# import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('lineaamodel.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')
						
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = request.form.get('Year')
        Present_Price = float(request.form.get('Present_Price'))  
        Kms_Driven = float(request.form.get('Kms_Driven'))  
        Fuel_Type = float(request.form.get('Fuel_Type'))  
        Seller_Type = float(request.form.get('Seller_Type'))  
        Transmission = float(request.form.get('Transmission'))  
        Owner = float(request.form.get('Owner'))

        print(Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner)
        input=pd.DataFrame([[Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]],
                           columns=['Year','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner'])

        prediction=model.predict(input)[0]

        return str(prediction)
if __name__ == "__main__":
    app.run(debug=True)







