# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path
data = pd.read_csv(path)
data['Gender'].replace('Agender','-',inplace=True)
gender_count = data.Gender.value_counts()
print(gender_count)
#print(gender_count.value())
plt.bar(gender_count.keys(),gender_count)
plt.show()
#Code starts here 




# --------------
#Code starts here
alignment = data.Alignment.value_counts()
print(alignment)
plt.pie(alignment,labels=alignment.keys())
plt.show()


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.Strength.cov(sc_df.Combat)
sc_strength = sc_df.Strength.std()
sc_combat = sc_df.Combat.std()
sc_pearson = sc_covariance/ (sc_strength*sc_combat)
print('sc_pearson:',sc_pearson)
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.Intelligence.cov(sc_df.Combat)
ic_intelligence = ic_df.Intelligence.std()
ic_combat = ic_df.Combat.std()
ic_pearson = ic_covariance/ (ic_intelligence*ic_combat)
print('ic_pearson:',ic_pearson)


# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
super_best = data[data['Total']>total_high]
super_best_names = list(super_best['Name'])
print(super_best_names)


# --------------
#Code starts here
ax_1 = data.boxplot(column=['Intelligence'])
ax_2 = data.boxplot(column=['Speed'])
ax_3 = data.boxplot(column=['Power'])


