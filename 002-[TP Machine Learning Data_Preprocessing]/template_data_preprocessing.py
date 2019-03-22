#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:00:00 2019

@author: Jb
"""

# import libraries
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# ==============
# 1. Comprendre le contexte et cas d'usages
# ==============

# import dataset (REPLACE WITH PATH TO YOUR OWN DATAFILE)
dataset = pd.read_csv("./Data.csv")

X = dataset.iloc[:, :-1].values             # X train (Features)
Y = dataset.iloc[:, -1].values              # Y train (Labels)

# ==============
# 2. Exploration  des données
# ==============

# Structure
dataset.head()
dataset.info()
dataset.count()
print(dataset.columns)
print(dataset.shape)
print(dataset.dtypes)

# Label: purchased
dataset.Purchased.value_counts()
dataset["Purchased"].hist()
