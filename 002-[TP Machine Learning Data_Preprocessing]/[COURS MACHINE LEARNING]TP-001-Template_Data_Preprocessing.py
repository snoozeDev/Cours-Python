"""
    PROGRAM NAME            :   [COURS MACHINE LEARNING]TP-001-Template_Data_Preprocessing.PY
    AUTHOR                  :   SLIM OUERGHI
    CREATION DATE           :
    PROJECT                 :   COURS MACHINE LEARNING
----------------------------------------------------------------------------------------------
    FUNCTION                :   Data Preprocessing
    PRAMETERS               :
----------------------------------------------------------------------------------------------
    VERSION	                : 1.0
    Modification date       :
    Modification author     :
    Modification description:
----------------------------------------------------------------------------------------------
"""

# Importer les librairies
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

"""   ------------2.	Comprendre le contexte et cas d’usage -------"""
# Importer le dataset
# (Remplacer avec le chemin d'accès avec le jeu de données voulu)
dataset = pd.read_csv("/Users/Jb/Documents/Cours Machine Learning/TP Machine Learning/002-[TP Machine Learning Data_Preprocessing]/Data.csv")
# créer la matrice des variables explicatives ( features)
X = dataset.iloc[:, :-1].values
# creer le vecteur de la variable expliquée ( Label)
Y = dataset.iloc[:, -1].values

# Structure
dataset.head()
dataset.columns
dataset.info()
# Dimension 
dataset.count()
dataset.shape
dataset.dtypes

# Gérer les données manquantes
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
imputer.fit(X[:, [1, 2]])
X[:, 1:3] = imputer.transform(X[:, 1:3])

# Gérer les variables catégoriques


""" Variables indicatrices"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
Y = labelencoder_y.fit_transform(Y)

# Diviser le dataset entre le Training set et le Test set
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
