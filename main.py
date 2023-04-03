
from flask import Flask,render_template,request,redirect,url_for
import pickle
import sklearn

print(sklearn.__version__)

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
    app.run(host='0.0.0.0',port=8080,debug=True)




