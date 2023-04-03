import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
from sklearn.metrics import accuracy_score

data = pd.read_csv('BankNote_Authentication.csv')
x_data = data.iloc[:,:-1]
y_data = data.iloc[:,-1]
x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.2,random_state=123)
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
preds = model.predict(x_test)
acc = accuracy_score(y_test,preds)
#y_preds = model.predict(x_test)
file_name = 'classifier_model.sav'
pickle.dump(model,open(file_name,'wb'))