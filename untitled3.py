# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gbaB1ZQgS_Yn_VHyRFb4t3szCy4PKjWg
"""

import seaborn as sns

print(sns.get_dataset_names())

tips = sns.load_dataset('tips')

print(tips.head())

print(tips.head())

print(tips.describe())

print(tips.info())
tips

import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(tips['total_bill'], kde=True)
plt.title('distribution of total bill')
plt.show()

