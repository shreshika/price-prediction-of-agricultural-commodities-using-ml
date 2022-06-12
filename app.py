from flask import Flask, render_template,request
import pickle
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

app = Flask(__name__, template_folder='templates')
model=pickle.load(open('lrmodel.pkl','rb'))
model1=pickle.load(open('rfrmodel.pkl','rb'))
model2=pickle.load(open('dtrmodel.pkl','rb'))
@app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def home():
   if request.method == 'POST':
    data1=int(request.form['Commodity'])
    data2=int(request.form['Variety'])
    data3=int(request.form['Max'])
    data4=int(request.form['Min'])
    pred=model.predict([[data1,data2,data3,data4]])
    pred1=model1.predict([[data1,data2,data3,data4]])
    pred2=model2.predict([[data1,data2,data3,data4]])
    output=round(pred[0],2)
    output1=round(pred1[0],2)
    output2=round(pred2[0],2)
    print(output)
    print(output1)
    print(output2)
    return render_template('index.html', prediction=output,prediction1=output1,prediction2=output2)
   else:
      return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)