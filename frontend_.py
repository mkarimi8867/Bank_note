from flask import Flask,render_template,request,redirect,url_for
import pickle
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# @app.route('/color/<patette>/')
# def colors(palette):
#     """ Example endpoint returnng a list of colors by pallete
#     this is using docstring specifications
#     ---
#     parameters:
#         -name: pallete
#         in: path
#         type: string
#         enum: ['all','rgb','cmyk']
#         required: true
#         default: all
#     definitions:
#         pallete:
#             type: object
#             properties:
#                 palette_name:
#                     type: array
#                     items:
#                         $ref: '#/definitions/color'
#             color:
#                 type: string
#             responses:
#                 200:
#                     description: the output values
#     """
model = pickle.load(open('classifier_model.sav','rb'))
(print('model is loaded'))
@app.route('/')
def enter_data():
    print('data is entering')
    return render_template('index.html')

# @app.route('/result/<score>')
# def result(score):
#     res = "Authenticated" if int(score) == 1 else "Not Athenticated"
#     print(res)
#     return render_template('result.html', result=res)

@app.route('/predict',methods=['GET'])
def predict():
    """ Let's Authenticate the bank note
    this is using docstring for specifications.
    ---
    parameters:
        - name: variance
        in: query
        type: number
        required: true
        - name: skewness
        in: query
        type: number
        required: true
        - name: curtosis
        in: query
        type: number
        required: true
        - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: the output values

    """

    variance = request.args.get('variace')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    print('variace:',variance)
    print('skewness:',skewness)
    print('entropy:',entropy)

    pred = model.predict([[variance,skewness,curtosis,entropy]])
    print('prediction:',pred)

    return render_template('result_2.html',result = pred[0])


if __name__=='__main__':
    app.run(debug=True)
