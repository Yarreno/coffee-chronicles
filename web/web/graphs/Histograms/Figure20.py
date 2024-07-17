import pymongo
import pandas as pd
import matplotlib.pyplot as plt


myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
collection = mydb['customersdb']


data = collection.find()
data_list = list(data)

df = pd.DataFrame(data_list)


reasons_by_age = df.groupby(['What is your age?', 'What is your reason for consuming coffee?']).size().unstack(fill_value=0)


plt.figure(figsize=(12, 8))

reasons = reasons_by_age.columns
bar_width = 0.15
opacity = 0.8

for i, (age_group, row) in enumerate(reasons_by_age.iterrows()):
    plt.barh(range(len(reasons)), row, bar_width, label=age_group)

plt.xlabel('Frequency of Respondents')
plt.ylabel('Reasons for Consuming Coffee')
plt.title('Reasons for Consuming Coffee in Different Ages')
plt.yticks(range(len(reasons)), reasons)
plt.legend(title='Age Group', loc='upper right')
plt.grid(axis='x', linestyle='--')

plt.tight_layout()
plt.savefig('web/graphs/exported/Figure20.png')
