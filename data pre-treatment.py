# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 22:48:19 2016

@author: wudi
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

train_path="/Users/wudi/Documents/data/train.csv"
town_state_path="/Users/wudi/Documents/data/town_state.csv"
cliente_tabla_path="/Users/wudi/Documents/data/cliente_tabla.csv"
producto_tabla_path="/Users/wudi/Documents/data/producto_tabla.csv"
test_path="/Users/wudi/Documents/data/test.csv"

train=pd.read_csv(train_path)
town=pd.read_csv(town_state_path)
cliente=pd.read_csv(cliente_tabla_path)
producto=pd.read_csv(producto_tabla_path)
test=pd.read_csv(test_path)

cm=train.corr()
sns.heatmap(cm,square=True)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()