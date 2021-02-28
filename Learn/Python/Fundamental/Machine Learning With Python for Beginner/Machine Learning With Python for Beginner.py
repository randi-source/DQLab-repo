#[Eksplorasi Data: Memahami Data dengan Statistik - Part 1](https://academy.dqlab.id/main/livecode/169/328/1553)
import pandas as pd
dataset=pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/online_raw.csv')
print('Shape dataset:', dataset.shape)
print('\nLima data teratas:\n', dataset.head())
print('\nInformasi dataset:')
print(dataset.info())
print('\nStatistik deskriptif:\n', dataset.describe())

#[Eksplorasi Data: Memahami Data dengan Statistik - Part 2](https://academy.dqlab.id/main/livecode/169/328/1555)
dataset_corr = dataset.corr()
print('Korelasi dataset:\n', dataset.corr())
print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())
# Tugas praktek
print('\nKorelasi BounceRates-ExitRates:', dataset_corr.loc['BounceRates','ExitRates'])
print('\nKorelasi Revenue-PageValues:', dataset_corr.loc['Revenue','PageValues'])
print('\nKorelasi TrafficType-Weekend:', dataset_corr.loc['TrafficType','Weekend'])

#[Eksplorasi Data: Memahami Data dengan Visual](https://academy.dqlab.id/main/livecode/169/328/1558)
import matplotlib.pyplot as plt
import seaborn as sns
# checking the Distribution of customers on Revenue
plt.rcParams['figure.figsize']=(12,5)
plt.subplot(1, 2, 1)
sns.countplot(dataset['Revenue'], palette='pastel')
plt.title('Buy or Not', fontsize=20)
plt.xlabel('Revenue or not', fontsize=14)
plt.ylabel('count', fontsize=14)
# checking the Distribution of customers on Weekend
plt.subplot(1, 2, 2)
sns.countplot(dataset['Weekend'], palette='inferno')
plt.title('Purchase on Weekends', fontsize=20)
plt.xlabel('Weekend or not', fontsize=14)
plt.ylabel('count', fontsize=14)
plt.show()

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/169/328/1559)
import matplotlib.pyplot as plt
# visualizing the distribution of customers around the Region
plt.hist(dataset['Region'], color = 'lightblue')
plt.title('Distribution of Customers', fontsize = 20)
plt.xlabel('Region Codes', fontsize = 14)
plt.ylabel('Count Users', fontsize = 14)
plt.show()

#[Data Pre-processing: Handling Missing Value - Part 1](https://academy.dqlab.id/main/livecode/169/328/1561)
#checking missing value for each feature  
print('Checking missing value for each feature:')
print(dataset.isnull().sum())
#Counting total missing value
print('\nCounting total missing value:')
print(dataset.isnull().sum().sum())

#[Data Pre-processing: Handling Missing Value - Part 3](https://academy.dqlab.id/main/livecode/169/328/1565)
print("Before imputation:")
# Checking missing value for each feature  
print(dataset.isnull().sum())
# Counting total missing value  
print(dataset.isnull().sum().sum())

print("\nAfter imputation:")
# Fill missing value with mean of feature value  
dataset.fillna(dataset.mean(), inplace = True)
# Checking missing value for each feature  
print(dataset.isnull().sum())
# Counting total missing value  
print(dataset.isnull().sum().sum())

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/169/328/1566)
import pandas as pd
dataset1 = pd.read_csv('https://dqlab-dataset.s3-ap-southeast-1.amazonaws.com/pythonTutorial/online_raw.csv')

print("Before imputation:")
# Checking missing value for each feature  
print(dataset1.isnull().sum())
# Counting total missing value  
print(dataset1.isnull().sum().sum())

print("\nAfter imputation:")
# Fill missing value with median of feature value  
dataset1.fillna(dataset1.median(), inplace = True)
# Checking missing value for each feature  
print(dataset1.isnull().sum())
# Counting total missing value  
print(dataset1.isnull().sum().sum())

#[Tugas Praktek](https://academy.dqlab.id/main/livecode/169/328/1568)
from sklearn.preprocessing import MinMaxScaler  
#Define MinMaxScaler as scaler  
scaler = MinMaxScaler()  
#list all the feature that need to be scaled  
scaling_column = ['Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues']
#Apply fit_transfrom to scale selected feature  
dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])
#Cheking min and max value of the scaling_column
print(dataset[scaling_column].describe().T[['min','max']])

#[Data Pre-processing: Konversi string ke numerik](https://academy.dqlab.id/main/livecode/169/328/2464)
import numpy as np
from sklearn.preprocessing import LabelEncoder
# Convert feature/column 'Month'
LE=LabelEncoder()
dataset['Month']=LE.fit_transform(dataset['Month'])
print(LE.classes_)
print(np.sort(dataset['Month'].unique()))
print('')

# Convert feature/column 'VisitorType'
LE=LabelEncoder()
dataset['VisitorType']=LE.fit_transform(dataset['VisitorType'])
print(LE.classes_)
print(np.sort(dataset['VisitorType'].unique()))

#[Features & Label]()
# removing the target column Revenue from dataset and assigning to X
X = dataset.drop(['Revenue'], axis=1)
# assigning the target column Revenue to y
y = dataset['Revenue']
# checking the shapes
print("Shape of X:", X.shape)
print("Shape of y:", y.shape)

#[Training dan Test Dataset]()
from sklearn.model_selection import train_test_split
# splitting the X, and y
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.2, random_state=0)
# checking the shapes
print("Shape of X_train :", X_train.shape) 
print("Shape of y_train :", y_train.shape)
print("Shape of X_test :", X_test.shape)
print("Shape of y_test :", y_test.shape)

#[Training Model: Fit]()
from sklearn.tree import DecisionTreeClassifier
# Call the classifier
model=DecisionTreeClassifier()
# Fit the classifier to the training data
model=model.fit(X_train, y_train)

#[Training Model: Predict]()
# Apply the classifier/model to the test data
y_pred=model.predict(X_test)
print(y_pred.shape)

#[Evaluasi Model Performance - Part 2]()
from sklearn.metrics import confusion_matrix, classification_report

# evaluating the model
print('Training Accuracy :', model.score(X_train, y_train))
print('Testing Accuracy :', model.score(X_test, y_test))

# confusion matrix
print('\nConfusion matrix:')
cm=confusion_matrix(y_test, y_pred)
print(cm)

# classification report
print('\nClassification report:')
cr=classification_report(y_test, y_pred)
print(cr)

#[Pemodelan Permasalahan Klasifikasi dengan Logistic Regression]()
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Call the classifier
logreg = LogisticRegression()
# Fit the classifier to the training data  
logreg = logreg.fit(X_train, y_train)
#Training Model: Predict 
y_pred = logreg.predict(X_test)

#Evaluate Model Performance
print('Training Accuracy :', model.score(X_train, y_train))  
print('Testing Accuracy :', model.score(X_test, y_test))  

# confusion matrix
print('\nConfusion matrix')  
cm = confusion_matrix(y_test, y_pred)  
print(cm)

# classification report  
print('\nClassification report')  
cr = classification_report(y_test, y_pred)  
print(cr)

#[Classification - Decision Tree]()
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

# Call the classifier
decision_tree = DecisionTreeClassifier()
# Fit the classifier to the training data
decision_tree = decision_tree.fit(X_train, y_train)

# evaluating the decision_tree performance
print('Training Accuracy :', decision_tree.score(X_train, y_train))
print('Testing Accuracy :', decision_tree.score(X_test, y_test))

#[]()


#[]()


#[]()


#[]()


#[]()


#[]()
