import pymongo
import pandas as pd
import matplotlib.pyplot as plt


myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
collection = mydb['customersdb']


data = collection.find()
data_list = list(data)


df = pd.DataFrame(data_list)


income_mapping = {
    "0-20.000 TL": 10000,
    "20.001-40.000 TL": 30000,
    "40.001-60.000 TL": 50000,
    "60.000-80.000TL": 70000,
    "80.001 +": 90000
}

coffee_budget_mapping = {
    "50-60 TL": 55,
    "61-70 TL": 65,
    "71-80 TL": 75,
    "80+ TL": 85
}

df['Monthly Income'] = df['How much is your monthly income?'].map(income_mapping)
df['Coffee Budget'] = df['How much is your budget when buying a coffee?'].map(coffee_budget_mapping)


income_groups = df.groupby('Monthly Income')['Coffee Budget'].mean()


plt.figure(figsize=(10, 6))
plt.plot(income_groups.index, income_groups.values, marker='o')

plt.xlabel('Monthly Income (TL)')
plt.ylabel('Coffee Budget (TL)')
plt.title('Trend of Coffee Budget in Different Monthly Income')

plt.grid(True)
plt.tight_layout()
plt.savefig('web/graphs/exported/Figure18.png')
