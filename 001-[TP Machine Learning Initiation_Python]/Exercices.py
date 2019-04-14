#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:57:34 2019

@author: Jb
"""

# ===================
# Pandas Set-up
# ===================
import pandas as pd                     # Import librairie pandas

df = pd.read_table('/Users/Jb/Documents/Cours Machine Learning/TP Machine Learning/001-[TP Machine Learning Initiation_Python]/heart.txt', sep='\t', header=0)   # Pandas : charger un fichier dans pandas

# ===================
# Fonctions pandas
# ===================

# General information
print(df.describe(include='all'))       # Stats extraites de la table
print(df.info())                        # Repérer les données manquantes dans les colonnes
print(df.shape)                         # Affiche la forme du tableau: (lignes, colonnes)
print(df.dtypes)                        # Affiche les types correspondants a chaque colonnes

# Show data
print(df.head())                        # Affiche les 5 premières lignes du tableau
print(df.columns)                       # Lister les colonnes
print(df.sexe)                          # Affiche la colonne "sexe"
print(df[['sexe', 'sucre']].tail())     # Affiche les 5 dernières lignes des colonnes "sexe" & "sucre"
print(df['age'][:3])                    # Affiche les 3 premières ligne de la colonne age

print(df['sexe'].value_counts())        # Compte les valeurs d'une colonne
print(df.iloc[-1,0])                    # Affiche la dernière ligne de la 1ere colonne
print(df.iloc[0:5,[0,2,4]])             # Affiche les 5 premières lignes des colonnes 0, 2, et 4

print(df.loc[df['sexe'] == "masculin", :])      # Affiche toutes les lignes où le sexe est masculin

# Addition de filtres
print(df.loc[(df['typedouleur'] == "A") & (df['angine'] == "oui"), :])

