# Cours Predictive Analytics

## Intro Python

### Pandas set-up

```python
import pandas as pd

df = pd.read_table('./heart.txt', sep='\t', header=0)
```

With these you load Pandas library & load a file in a **dataframe**.

`import pandas as pd` loads pandas library & sets name to `pd`.

`pd.readtable({{file_url}}, sep={{separator}}, header={{header_row}})` is the method for  loading a file with Pandas. It takes 3 arguments:

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
- `df.describe()` gives general stats on dataframe
- `df.head()` returns 5 first lines of dataframe
- `df.info()` returns information on columns
#### Properties
- `df.shape` returns dataframe shape (lines, columns)
- `df.dtypes` returns types by columns

## Column specific functions
```python
import pandas as pd
df = pd.read_table('./heart.txt', sep='\t', header=0)

print(df[['sexe', 'sucre']].tail())     # Affiche les 5 dernières lignes des colonnes "sexe" & "sucre"
print(df['age'][:3])                    # Affiche les 3 premières ligne de la colonne age
print(df['sexe'].value_counts())        # Compte les valeurs d'une colonne

```

### iloc vs loc
```python
import pandas as pd
df = pd.read_table('./heart.txt', sep='\t', header=0)

print(df.loc[df['sexe'] == "masculin", :])      # Affiche toutes les lignes où le sexe est masculin

print(df.iloc[-1,0])                            # Affiche la denière ligne de la 1ere colonne
print(df.iloc[0:5,[0,2,4]])                     # Affiche les 5 premières lignes des colonnes 0, 2, et 4

```

## Filtres
```python
import pandas as pd
df = pd.read_table('./heart.txt', sep='\t', header=0)

# Addition de filtres
print(df.loc[(df['typedouleur'] == "A") & (df['angine'] == "oui"), :])
```
