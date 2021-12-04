# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:42:05 2021

@author: User
"""

pip install mlxtend
import matplotlib.pylab as plt
import pandas as pd

from mlxtend.frequent_patterns import apriori, association_rules

groceries= [] 
with open("F:/Association Rules/Assignment/groceries.csv") as f:
    groceries = f.read()
    
groceries =  groceries.split("\n")

groceries_list = []
for i in groceries:
    groceries_list.append(i.split(","))
    
allgroceries_list = [i for item in groceries_list for i in item]

from collections import Counter

itemsFrequencies  = Counter(allgroceries_list)

itemsFrequencies = sorted(itemsFrequencies.items(), key = lambda x:x[1])

frequencies_groceries =list(reversed([i[1] for i in itemsFrequencies]))
itemgroceries = list(reversed([i[1] for i in itemsFrequencies]))

plt.bar(height = frequencies_groceries[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), itemgroceries[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

# Creating Data Frame for the transactions data
groceries_series = pd.DataFrame(pd.Series(groceries_list))
groceries_series = groceries_series.iloc[:9835, :] # removing the last empty transaction

groceries_series.columns = ["collections"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name
X = groceries_series['collections'].str.join(sep = '*').str.get_dummies(sep = '*')

frequent_groceriessets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

frequent_groceriessets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_groceriessets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_groceriessets.itemsets[0:11], rotation=20)
plt.xlabel('book-sets')
plt.ylabel('support')
plt.show()


rules = association_rules(frequent_groceriessets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

