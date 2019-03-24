# Partie 1

> VOIR LE [CODE](./Exercices.py)

## Intro Python

### Pandas set-up

```python
import pandas as pd

df = pd.read_table('./heart.txt', sep='\t', header=0)
```

Avec ces lignes vous invoquez la librarie Pandas et stockez les données d'un ficher `heart.txt` dans un **dataframe**.

`import pandas as pd` invoque la librairie Pandas et lui assigne le nom `pd` .

`pd.readtable({{file_url}}, sep={{separator}}, header={{header_row}})` est la méthode pour charger un fichier avec Pandas. 

Elle prend 3 arguments :

| argument | example | type | description |
| -------- | ------- | --- | ----------- |
| _{{file_url}}_ | './heart.txt' | str | Data file path |
| _{{separator}}_ | '\t' | str | Separator character (ASCII) |
| _{{header_row}}_ | 0 | int | Header row number |

### General Information

```python
import pandas as pd
df = pd.read_table('./heart.txt', sep='\t', header=0)

print(df.describe(include='all'))       # Stats extraites de la table
print(df.head())
print(df.info())                        # Repérer les données manquantes dans les colonnes
print(df.shape)                         # Affiche la forme du tableau: (lignes, colonnes)
print(df.dtypes)                        # Affiche les types correspondants a chaque colonnes

```

#### Functions
- `df.describe()` renvoie des informations générales sur les données
- `df.head()` renvoie les 5 premières lignes du dataframe
- `df.info()` renvoie des informations générales sur le colonnes
#### Properties
- `df.shape` renvoie la "forme" du dataframe ( _x_ lines, _y_ columns)
- `df.dtypes` renvoie les différents types par colonnes

## Column specific functions
```python
import pandas as pd
df = pd.read_table('./heart.txt', sep='\t', header=0)

print(df[['sexe', 'sucre']].tail())     # Affiche les 5 dernières lignes des colonnes "sexe" & "sucre"
print(df['age'][:3])                    # Affiche les 3 premières ligne de la colonne age
print(df['sexe'].value_counts())        # Compte les valeurs d'une colonne

```

La notation `df[ {{NOM_DE_COLONNE}} ]` permet de faire référence à une ou plusieurs colonnes.

### iloc vs loc
```python
import pandas as pd
df = pd.read_table('./heart.txt', sep='\t', header=0)

print(df.loc[df['sexe'] == "masculin", :])      # Affiche toutes les lignes où le sexe est masculin

print(df.iloc[-1,0])                            # Affiche la denière ligne de la 1ere colonne
print(df.iloc[0:5,[0,2,4]])                     # Affiche les 5 premières lignes des colonnes 0, 2, et 4

```

`iloc[]` permet de trouver des données grâce aux indèxes des lignes et des colonnes.

`loc[]` permet de trouver des données grâce aux noms des colones

Chacune de ces méthodes peuvent être utilisées comme filtre. Par exemple :

```python
print(df.loc[df['sexe'] == "masculin", :])      # Affiche toutes les lignes où le sexe est masculin
```

## Filtres
```python
import pandas as pd
df = pd.read_table('./heart.txt', sep='\t', header=0)

# Addition de filtres
print(df.loc[(df['typedouleur'] == "A") & (df['angine'] == "oui"), :])
```

Les filtres peuvent être combinés.