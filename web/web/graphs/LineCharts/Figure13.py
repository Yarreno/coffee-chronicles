import pymongo
import pandas as pd
import matplotlib.pyplot as plt


myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
collection = mydb['customersdb']


data = collection.find()
data_list = list(data)


df = pd.DataFrame(data_list)


gender_coffee_freq = df.groupby(['What is your gender?', 'How often do you consume coffee in a week?']).size().unstack(fill_value=0)


plt.figure(figsize=(10, 6))

for gender in gender_coffee_freq.index:
    plt.plot(gender_coffee_freq.columns, gender_coffee_freq.loc[gender], marker='o', label=gender)

plt.xlabel('Frequency of Coffee Consumption (Per Week)')
plt.ylabel('Frequency')
plt.title('Trend of Coffee Consumption Frequency for Gender')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('web/graphs/exported/Figure13.png')
