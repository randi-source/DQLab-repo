#[Import Library yang digunakan](https://academy.dqlab.id/main/livecode/179/348/1703)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold

import string
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#[Import Data Set dan Concat Data Frame](https://academy.dqlab.id/main/livecode/179/348/1704)
def concat_df(train_data, test_data):
	#Return a concatenated df of training and test set
	return pd.concat([train_data, test_data], sort=True). reset_index(drop=True)
df_train=pd.read_csv('https://academy.dqlab.id/dataset/challenge/feature-engineering/titanic_train.csv')
df_test=pd.read_csv('https://academy.dqlab.id/dataset/challenge/feature-engineering/titanic_test.csv')
df_all=concat_df(df_train, df_test)

df_train.name='Training Set'
df_test.name='Test Set'
df_all.name='All Set'

dfs=[df_train, df_test]

#[Exploring Data](https://academy.dqlab.id/main/livecode/179/348/1705)
print('Number of Training Examples = {}'.format(df_train.shape[0]))
print('Number of Test Examples = {}\n'.format(df_test.shape[0]))
print('Training X Shape = {}'.format(df_train.shape))
print('Training y Shape = {}\n'.format(df_train['Survived'].shape[0]))
print('Test X Shape = {}'.format(df_test.shape))
print('Test y Shape = {}\n'.format(df_test.shape[0]))
print(df_train.columns)
print(df_test.columns)

#[Missing Value dan Contoh data](https://academy.dqlab.id/main/livecode/179/348/1707)
df_train.info(memory_usage=False)
print(df_train.head(10))

#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()


#[]()
