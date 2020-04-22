# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data = pd.read_csv(path)
data.hist(bins=30)
print(data.shape)
data = data[data['Rating']<=5]
print(data.shape)
data.hist(bins=30)
plt.show()
#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = total_null/data.isnull().count()
missing_data = pd.concat([total_null, percent_null],keys=['Total','Percent'],axis=1 )
print(missing_data)
print(missing_data.shape)

data.dropna(axis = 0,inplace = True)
total_null_1 = data.isnull().sum()
percent_null_1 = total_null_1/data.isnull().count()
missing_data_1 = pd.concat([total_null_1, percent_null_1],keys=['Total','Percent'],axis=1 )
print(missing_data_1)
print(missing_data_1.shape)
# code ends here


# --------------

#Code starts here
pl = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
pl.set_xticklabels(rotation=90)
pl.set_titles("Rating vs Category [BoxPlot]")


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
def def_replace(x):
    return x.replace(',','').replace('+','')


print(data['Installs'].value_counts())
data['Installs'] = data['Installs'].str.replace('+','')
data['Installs'] = data['Installs'].str.replace(',','')
#data['Installs'] = data['Installs'].map(def_replace)
data['Installs'] = data['Installs'].astype('int')
print(data['Installs'].value_counts())
print(data.info())

le = LabelEncoder()
data['Installs']=le.fit_transform(data['Installs'])
sns.regplot(x="Installs", y="Rating" , data=data)
pl.set_titles("Rating vs Installs [RegPlot]")
plt.show()
#Code ends here



# --------------
#Code starts here
data['Price'].head()
print(data['Price'].value_counts())
print(data.isnull().sum())
data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype('float')
pl = sns.regplot(x="Price", y="Rating" , data=data)
plt.title("Rating vs Price [RegPlot]")
plt.show()
#Code ends here


# --------------

#Code starts here
def split_genres(x):
    return x.split(';')[0]

data['Genres'].unique()

data['Genres'] = data['Genres'].map(split_genres)
gr_mean = data[['Genres','Rating']].groupby(['Genres'],as_index=False).mean()
gr_mean.describe()

gr_mean = gr_mean.sort_values(by=['Rating'])
print(gr_mean.head(1))
print(gr_mean.tail(1))

#Code ends here


# --------------

#Code starts here
data['Last Updated'].head()
#data['Last Updated'].hist(bins=20)

data['Last Updated'] = pd.to_datetime(data['Last Updated'] , format='%B %d, %Y')
#data['Last Updated'].head()
#data.info()
max_date = data['Last Updated'].max()
print(max_date)

data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days
print(data['Last Updated Days'])

sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
plt.show()
#Code ends here


