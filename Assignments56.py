import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import VotingClassifier



border="-"*40
print(border)
print("Step 1:- Load the dataset")
print(border)
df =pd.read_csv("Customer_Loan_Approval.csv")
print(df.head)

print(border)
print("Step 2: Find missing values")
print(border)
print(df.isnull().sum())


print(border)
print("Step 3: Separate input and output:-")
print(border)
X=df.drop(columns=['LoanApproved'])
Y=df['LoanApproved']
print("Indepndt variable are :",X)
print("Dependent variable are :",Y)


print(border)
print("Step 4: Split dataset into training and testing datset")
print(border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

print(border)
print("Step 5: model selection and traing")
print(border)

K_model=KNeighborsClassifier()
d_model=DecisionTreeClassifier()
l_model=LogisticRegression()


print(border)
print("Step 6: Create votting model")
print(border)
model =VotingClassifier(
    estimators=[
        ('logistic',l_model),
        ('decision_tree',d_model),
        ('knn',K_model)
    ],
    voting="hard"
)

print(border)
print("Step 6 : Train the model")
print(border)

model=model.fit(X_train,Y_train)

print(border)
print("Step 7:- Predict the model")
print(border)
Y_pred=model.predict(X_test)
accuracy=accuracy_score(Y_test,Y_pred)
print("Accuracy is :",accuracy*100)












