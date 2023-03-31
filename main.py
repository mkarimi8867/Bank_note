# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score
from flask import Flask,render_template,request,redirect,url_for
import pickle
import sklearn
print(sklearn.__version__)

# data = pd.read_csv('BankNote_Authentication.csv')
# x_data = data.iloc[:,:-1]
# y_data = data.iloc[:,-1]
# x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.2,random_state=123)
# model = DecisionTreeClassifier()
# model.fit(x_train,y_train)
# #y_preds = model.predict(x_test)
# file_name = 'classifier_model.sav'
# pickle.dump(model,open(file_name,'wb'))

app = Flask(__name__)
model = pickle.load(open('classifier_model.sav','rb'))
(print('model is loaded'))
@app.route('/')
def enter_data():
    print('data is entering')
    return render_template('index.html')

@app.route('/result/<score>')
def result(score):
    res = "Authenticated" if int(score) == 1 else "Not Athenticated"
    print(res)
    return render_template('result.html', result=res)

@app.route('/predict',methods=['POST','GET'])
def predict():
    data = []
    print(request.method)
    if request.method == 'POST':
        variance = float(request.form['variance'])
        print('variace:',variance)
        data.append(variance)
        skewness = float(request.form['skewness'])
        print('skewness:',skewness)
        data.append(skewness)
        curtosis = float(request.form['curtosis'])
        print('curtosis:',curtosis)
        data.append(curtosis)
        entropy = float(request.form['entropy'])
        print('entropy:',entropy)
        data.append(entropy)
        pred = model.predict([data])
        print('prediction:',pred)

        return redirect(url_for('result',score=pred[0]))


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)




