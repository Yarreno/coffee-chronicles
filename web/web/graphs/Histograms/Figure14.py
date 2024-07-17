import matplotlib.pyplot as plt
import pymongo
import seaborn as sns
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
df = mydb['customersdb']

def get_data():
    data = list(df.find({}, {"_id": 0, "What is your age?": 1, "What is your favorite type of coffee?": 1}))
    return data

data = get_data()


df_plot = pd.DataFrame(data)


age_map = {
    "18<": "<18",
    "19-25": "19-25",
    "26-35": "26-35",
    "36-45": "36-45",
    "46-55": "46-55",
    "56>": ">56"
}

df_plot['Age'] = df_plot['What is your age?'].map(age_map)


coffee_map = {
    "Turkish Coffee": "Turkish Coffee",
    "Latte": "Latte",
    "Cappuccino": "Cappuccino",
    "Macchiato": "Macchiato",
    "Filter Coffee": "Filter Coffee",
    "Flat White": "Flat White",
    "Other": "Other"
}

df_plot['Favorite Coffee'] = df_plot['What is your favorite type of coffee?'].map(coffee_map)


fig, ax = plt.subplots(figsize=(10, 5))

font = {'color': 'black',
        'weight': 'normal',
        'size': 11,
        'style': 'italic'
        }


colors = ["#7D4F50", "#D1BE9C", "#AA998F", "#A78776", "#BB9D99", "#CC8B86", "#E0C2A2"]

sns.histplot(data=df_plot, x='Age', hue='Favorite Coffee', multiple='stack', palette=colors, shrink=0.8, ax=ax)


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)


ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')


ax.grid(axis="y", visible=True, color='grey', alpha=0.2, linestyle=":")


plt.xticks(fontsize=10, fontstyle="italic")
plt.yticks(fontsize=10, fontstyle="italic")
plt.title('Distribution of Age Among Respondents and Their Favorite Coffee Types', fontsize='16', fontstyle='italic')
plt.xlabel('Age', font, labelpad=10)
plt.ylabel('Count of Favorite Coffee Types', font, labelpad=10)

plt.legend(title='Favorite Coffee', title_fontsize='13', fontsize='11', frameon=False)

plt.savefig('web/graphs/exported/Figure14.png')
