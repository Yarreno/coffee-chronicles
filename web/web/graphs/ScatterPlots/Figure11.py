import pymongo
import pandas as pd
import matplotlib.pyplot as plt


myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
collection = mydb['customersdb']


data = collection.find()
data_list = list(data)


df = pd.DataFrame(data_list)


age_mapping = {
    "18<": 18,
    "19-25": 22,
    "26-35": 30,
    "36-45": 40,
    "46-55": 50,
    "56>": 60
}

income_mapping = {
    "0-20.000 TL": 10000,
    "20.001-40.000 TL": 30000,
    "40.001-60.000 TL": 50000,
    "60.000-80.000TL": 70000,
    "80.001 +": 90000
}

df['Age'] = df['What is your age?'].map(age_mapping)
df['Monthly Income'] = df['How much is your monthly income?'].map(income_mapping)


plt.figure(figsize=(10, 6))
plt.scatter(df['Age'], df['Monthly Income'], alpha=0.5)

plt.xlabel('Age')
plt.ylabel('Monthly Income (TL)')
plt.title('Relationship between Age and Monthly Income')

plt.grid(True)
plt.tight_layout()
plt.savefig('web/graphs/exported/Figure11.png')
