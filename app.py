from flask import Flask, request, render_template
import joblib
import numpy as np
app = Flask(__name__)
#load the model
model= joblib.load('model.pk1')
@app.route('/', methods=['Get','Post'])
def index():
    if request.method=='Post':
        try:
            # Get users inpute
            feature1=float(request.form['feature1'])
            feature2=float(request.form['feature2'])
            # make prediction
            input_data=np.array([[feature1,feature2]])
            prediction =model.predict(input_data)[0]
        
            return render_template('index.html', prediction=prediction)
        except Exception as e:
            return render_template('index.html',error='invalid input.please enter a number')  
        return render_template('index.html')
    if _name_ =='main_':
        app.run(debug=True)          