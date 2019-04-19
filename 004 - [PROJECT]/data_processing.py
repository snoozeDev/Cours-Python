# Import
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Import dataset
dataset = pd.read_csv('004 - [PROJECT]/Life Expectancy Data.csv')

# Features matrix
X = dataset.iloc[:, [0,1,2,3,4,5,6,9]].values              # Exclusion des colonnes 'country-year' & 'HDI for year'
X = dataset.iloc[:, :-1].values                # Exclusion des colonnes 'country-year' & 'HDI for year'
# Label Vector
Y = dataset.iloc[:, -1].values

cor = X_data.corr()
sns.heatmap(cor, xticklabels=cor.columns.values, yticklabels=cor.columns.values)
plt.show()

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()