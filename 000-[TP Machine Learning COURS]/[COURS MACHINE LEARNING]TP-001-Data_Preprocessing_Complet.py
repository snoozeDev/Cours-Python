"""
	PROGRAM NAME			:	[COURS MACHINE LEARNING]TP-001-Data_Preprocessing_Complet.PY			                 
	AUTHOR					:	SLIM OUERGHI													               
	CREATION DATE			:																	
	PROJECT				:	COURS MACHINE LEARNING													
----------------------------------------------------------------------------------------------
	FUNCTION				:	Data Preprocessing									
	PRAMETERS				:																	
----------------------------------------------------------------------------------------------
	VERSION					: 1.0																
	Modification date		:																	
	Modification author		:																	
	Modification description:																	
----------------------------------------------------------------------------------------------
"""

# Importer les librairies
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
"""   ------------2.	Comprendre le contexte et cas d’usage -------"""
#Importer le dataset

dataset=pd.read_csv("Data.csv")
#créer la matrice des variables explicatives ( features)
X=dataset.iloc[:,:-1].values
#creer le vecteur de la variable expliquée ( Label)
Y=dataset.iloc[:,-1].values

# Structure
dataset.head()
dataset.columns
dataset.info()
# Dimension 
dataset.count()
dataset.shape
dataset.dtypes
""" --------------3.	Exploration des données : --------------"""
#1.	Compréhension de ce que représente chaque variable :

# Label : Purchased
dataset.Purchased.value_counts()
dataset["Purchased"].hist() 
plt.show()
# country
dataset.Country.value_counts()
sns.countplot(x='Country', data=dataset)

# age
dataset.Age.value_counts()
dataset["Age"].hist() 
plt.show()

#Salaire

dataset.Salary.value_counts()
dataset["Salary"].hist() 
plt.show()

""" Correlation entre la label et les features    """




#recoder la variable Purchased

from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelEncoder_Y=LabelEncoder()
dataset["Purchased"]=labelEncoder_Y.fit_transform(dataset["Purchased"])
oneHotEncoder=OneHotEncoder(dataset["Purchased"])
dataset.dtypes
# ou
dataset["Purchased_1"]=pd.Categorical(dataset["Purchased"],ordered=False)
dataset.dtypes
# Créer une fonction

def MaFonctionplot_Var(data, x_axis, y_axis, hue):
    plt.figure()    
    sns.barplot(x=x_axis, y=y_axis, hue=hue, data=data)
    sns.set_context("notebook", font_scale=1.6)
    plt.legend(loc="upper right", fontsize="medium")

# Country en fonction de Purchased
sns.countplot(x='Country', data=dataset)
MaFonctionplot_Var(dataset,"Country", "Purchased", None) 
plt.show()

"""--------- Correlation entre les variables -----"""
 corr = dataset.iloc [: , [1,2,3]].corr()
 
 #fonction pour plot
 def plot_correlation_map(df):
    corr = df.corr()
    _ , ax = plt.subplots( figsize =( 12 , 10 ) )
    cmap = sns.diverging_palette( 220 , 10 , as_cmap = True )
    _ = sns.heatmap(
        corr, 
        cmap = cmap,
        square=True, 
        cbar_kws={ 'shrink' : .9 }, 
        ax=ax, 
        annot = True, 
        annot_kws = { 'fontsize' : 12 }
    )
    
 plot_correlation_map(dataset)
plt.show()



# Gérer les données manquantes
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


#Discrétisation d’une variable quantitative
"""
Pour la discrétisation d’une variable quantitative. Il est d’un bon usage de
définir les bornes des classes à des quantiles, plutôt qu’également espacées,
afin de construire des classes d’effectifs sensiblement égaux. Ceci est obtenu
par la fonction qcut. La fonction cut propose par défaut des bornes équiréparties
à moins de fournir une liste de ces bornes.
"""
# recoder age
Q1=dataset["age"].quantile(.1)
dataset.quantile([0.25, 0.5, 0.75])
dataset["age_recode"]=pd.qcut(df.Age,3,labels=["Age1","Age2","Age3"])


# Gérer les variables catégoriques

""" Modifier / regrouper des modalités """
# Modifier
dataset["age_recode"]=dataset["age_recode"].cat.rename_categories(["01-[<=35 ans]","02-[35-48 ans]","03-[>=48 ans]"])

# Regrouper
"""Il est possible d’associer recodage et regroupement des modalités en définissant
un dictionnaire de transformation.
"""


data = pd.DataFrame({"Country":["France","Germany","Spain", ],"age": ["01-[<=35 ans]","02-[35-48 ans]","03-[>=48 ans]"]})

#country
"""Définition de la transformation :"""
Recoder_Country = {
"France": "F",
"Germany": "G",
"Spain": "S"
}



dataset["Country_recode2"] = dataset["Country"].map(Recoder_Country)

""" Variables indicatrices"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# Diviser le dataset entre le Training set et le Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
 
 



