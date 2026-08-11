import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report

)

border="-"*30
##############################
# Step No 1:- Load the Dataset
##############################

print(border)
print("Step No 1:- Load the Dataset")
print(border)

Datapath=("iris.csv")

df=pd.read_csv(Datapath)
print(df)
print("Data loaded successfully")
print("Inital 5 entrie are :")
print(df.head(5))


##############################
# Step No 2:- Anylayse  the Dataset
##############################

print(border)
print("Step No 2:- Anylayse  the Dataset")
print(border)

print("Shape of the dataset is :",df.shape)
print("Names of columns :",list(df.columns))

print("Missing values per column:")

print(df.isnull().sum())
print("Class Distribution(Species count)")
print(df["species"].value_counts())



##############################
# Step No 3:- Decide the features and lebal
##############################

print(border)
print("Step No 3:- Decide the features and lebal")
print(border)

X=df[[
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)"
]]

Y=df["species"]
print("Shape of X:",X.shape)
print("Shape of Y:",Y.shape)


###########################
# Step 4: Visualization of the dataset
###########################

print(border)
print("Step 4: Visualization of the dataset")
print(border)

#Scatter plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"]== sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label=sp)

plt.title("MArvellous case study")
plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()


###########################
# Step 5: Splite the dataset into traing and testing
###########################

print(border)
print("Step 5: Splite the dataset into traing and testing")
print(border)

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)

print("Data is splited successfully"
      )

###########################
# Step 6: Built the model
###########################

print(border)
print("Step 6: Built the model")
print(border)

model = DecisionTreeClassifier(max_depth=5)
print("Model is created successfully")


###########################
# Step 7 :Train the model
###########################

print(border)
print("Step 7 :Train the model")
print(border)

model =model.fit(X_train,Y_train)
print("Model train successfully ")


###########################
# Step 8:Evaluate the model
###########################

print(border)
print("Step 8:Evaluate the model")
print(border)

Y_Pred= model.predict(X_test)

print("Model tested suceessfully")
print("Actual result is :",Y_Pred)
print("Expected result is :",Y_test)



###########################
# Step 9:Evaluate the model performance
###########################

print(border)
print("Step 9:Evaluate the model performance")
print(border)

accuracy =accuracy_score(Y_test,Y_Pred)
print("Accuracy of the model is :",accuracy * 100)


cm = confusion_matrix(Y_test,Y_Pred)
print("Confusion matrix is ",cm)


print(classification_report(Y_test,Y_Pred))
print("Classfication report")


