import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymongo

# Connect to MongoDB
myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
df = mydb['customersdb']

# Function to find count of respondents based on income and coffee budget
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

income_categories = ["0-20.000 TL", "20.001-40.000 TL", "40.001-60.000 TL", "60.000-80.000 TL"]
budget_categories = ["50-60 TL", "61-70 TL", "71-80 TL", "80+ TL"]

counts = np.zeros((len(income_categories), len(budget_categories)))


for i, income_cat in enumerate(income_categories):
    for j, budget_cat in enumerate(budget_categories):
        counts[i][j] = find_df(income_cat, budget_cat)


plt.figure(figsize=(10, 6))


colors = ["#7D4F50", "#AA998F", "#7D4F50", "#AA998F"]


for i in range(len(income_categories)):
    for j in range(len(budget_categories)):
        plt.scatter(i, j, s=counts[i][j]*50, color=colors[j], alpha=0.7)


plt.xticks(np.arange(len(income_categories)), income_categories, fontsize=8, fontstyle="italic")
plt.yticks(np.arange(len(budget_categories)), budget_categories, fontsize=8, fontstyle="italic")
plt.xlabel('Monthly Income', fontstyle="italic", labelpad=10)
plt.ylabel('Coffee Budget', fontstyle="italic", labelpad=10)
plt.title('Relationship between Monthly Income and Coffee Budget', fontsize=16)

plt.grid(True)
plt.savefig('web/graphs/exported/Figure16.png')
