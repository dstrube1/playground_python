'''2020-05-19

/nv/aps/ml_workshop
/nv/ap2/ml_workshop

ssh dstrube3@pace-ice.pace.gatech.edu
ssh dstrube3@login-s.pace.gatech.edu
ssh dstrube3@login7-d.pace.gatech.edu
cd to /nv/ap2/ml_workshop
pace-jupyter-notebook -q pace-training -l walltime=2:00:00 —anaconda=anaconda3/2019.10 —conda-env=ml

https://drive.google.com/drive/folders/117fhAhh_FefBtFj_8H-2v1K0lVnPMVmt
https://jupyter.org/try
https://www.anaconda.com/products/individual
https://colab.research.google.com/notebooks/intro.ipynb#recent=true

in jupyter notebook:
%matplotlib inline'''

from sklearn.datasets import load_boston
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

data  = load_boston()
data.feature_names

X,y = load_boston(return_X_y=True)
#print(X.shape)
#print(y.shape)
X = X[:,7]
#print(X.shape)
X = X[:,np.newaxis]
#print(X.keys)
#print(X.description)
#print(X)
lnrg = linear_model.LinearRegression()
lnrg.fit(X,y)
a_y_pred = lnrg.predict([[5]])
print(a_y_pred)
#plt.scatter(X,y,color='black')
#y_pred=lnrg.predict(X)
#a = input("hit enter")
print("all good")
