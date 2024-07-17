import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymongo


myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
df = mydb['customersdb']

def find_df(answer1, answer2):
    current_answer = df.find({
        "$and": [
            {"How much is your monthly income?": {"$regex": f"{answer1}"}},
            {"How much is your budget when buying a coffee?": {"$regex": f"{answer2}"}}
        ]
    })

    count = 0

    for i in current_answer:
        count += 1

    return count


income_ranges = ["0-20.000 TL", "20.001-40.000 TL", "40.001-60.000 TL", "60.000-80.000 TL"]
budget_ranges = ["50-60 TL", "61-70 TL", "71-80 TL", "80+ TL"]

data = []
for income in income_ranges:
    for budget in budget_ranges:
        data.append(find_df(income, budget))


plt.figure(figsize=(10, 6))
colors = ['#FF5733', '#33FF57', '#5733FF', '#FF5733']

for i in range(len(income_ranges)):
    plt.scatter([i]*len(budget_ranges), data[i*len(budget_ranges):(i+1)*len(budget_ranges)], 
                s=100, alpha=0.8, label=income_ranges[i], color=colors[i])


plt.xticks(range(len(income_ranges)), income_ranges)
plt.xlabel('Monthly Income')
plt.ylabel('Coffee Budget')
plt.title('Relationship between Monthly Income and Coffee Budget')
plt.legend(title='Income Range')

plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('web/graphs/exported/Figure6.png')
