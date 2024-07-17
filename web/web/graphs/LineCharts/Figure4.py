import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pymongo

# 4. **Line Chart**: Preferred Coffee Consumption Time by Age Group
myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")

mydb = myclient['CaffeineChronicles']

df = mydb['customersdb']


def find_df(answer1, answer2):
    current_answer = df.find({
        "$and": [
            {"At what time of the day do you prefer to consume coffee?": {"$in": [f"{answer1}"]}},
            {"What is your age?": {"$in": [f"{answer2}"]}}
        ]
    })

    count = 0

    for i in current_answer:
        count += 1

    return count


# <18 age groups
mor_18 = find_df('Morning', '<18')
after_18 = find_df('Afternoon', '<18')
even_18 = find_df('Evening', '<18')
all_18 = find_df('All', '<18')

y_18 = [mor_18, after_18, even_18, all_18]


# 19-25 age groups
mor_19_25 = find_df('Morning', '19-25')
after_19_25 = find_df('Afternoon', '19-25')
even_19_25 = find_df('Evening', '19-25')
all_19_25 = find_df('All', '19-25')
y_19_25 = [mor_19_25, after_19_25, even_19_25, all_19_25]


# 26-35 age groups
mor_26_35 = find_df('Morning', '26-35')
after_26_35 = find_df('Afternoon', '26-35')
even_26_35 = find_df('Evening', '26-35')
all_26_35 = find_df('All', '26-35')
y_26_35 = [mor_26_35, after_26_35, even_26_35, all_26_35]


# 36-45 age groups
mor_36_45 = find_df('Morning', '36-45')
after_36_45 = find_df('Afternoon', '36-45')
even_36_45 = find_df('Evening', '36-45')
all_36_45 = find_df('All', '36-45')
y_36_45 = [mor_36_45, after_36_45, even_36_45, all_36_45]


# 46-55 age groups
mor_46_55 = find_df('Morning', '46-55')
after_46_55 = find_df('Afternoon', '46-55')
even_46_55 = find_df('Evening', '46-55')
all_46_55 = find_df('All', '46-55')
y_46_55 = [mor_46_55, after_46_55, even_46_55, all_46_55]


# 56< age groups
mor_56 = find_df('Morning', '56<')
after_56 = find_df('Afternoon', '56<')
even_56 = find_df('Evening', '56<')
all_56 = find_df('All', '56<')
y_56 = [mor_56, after_56, even_56, all_56]


x_axis = ("Morning", "Afternoon", "Evening", "Every time of the day")

# **************************Customization**************************

fig, ax = plt.subplots(figsize=(10, 5))


font = {'color': 'black',
        'weight': 'normal',
        'size': 11,
        'style': 'italic'
        }

plt.plot(x_axis, y_18, label="<18", marker='o', lw=3, color='#CC8B86')
plt.plot(x_axis, y_19_25, label="19-25", marker='o', lw=3, color='#BB9D99')
plt.plot(x_axis, y_26_35, label="26-35", marker='o', lw=3, color='#7D4F50')
plt.plot(x_axis, y_36_45, label="36-45", marker='o', lw=3, color='#A78776')
plt.plot(x_axis, y_46_55, label="46-55", marker='o', lw=3, color='#D1BE9C')
plt.plot(x_axis, y_56, label="56<", marker='o', lw=3, color='#AA998F')


plt.title(label="Preferred Coffee Consumption Time by Age Group", fontsize='16', fontstyle="italic")
plt.xlabel('Time of day', font, labelpad=10)
plt.ylabel('Number of respondents', font, labelpad=10)

ax.grid(axis="y", visible=True, color='grey', alpha=0.2, linestyle=":")

ax.legend(loc="upper left")

plt.savefig('web/graphs/exported/Figure4.png')
