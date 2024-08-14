import pandas as pd    
import numpy as np
import seaborn as sns

data=pd.read_csv("USA_Housing.csv")

data.head()

data.info()

data.describe()

data.columns

sns.pairplot(data)

sns.displot(data["Price"], bins=100, kde=True, rug=True)

data.columns

X=data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]

y=data["Price"]

from sklearn.model_selection import train_test_split 

X_train,X_text,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=101)
from sklearn.linear_model import LinearRegression 
lr=LinearRegression()
lr.fit(X_train,y_train)
coficent_data_frame = pd.DataFrame(lr.coef_, X.columns , columns=["Coeff"])
coficent_data_frame
predict=lr.predict(X_text)
import matplotlib.pyplot as plt 
plt.scatter(y_test, predict)