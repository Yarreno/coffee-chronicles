import matplotlib.pyplot as plt
import pymongo

# 9. **Pie Chart**: Utilization of Campaigns and Discounts
myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")

mydb = myclient['CaffeineChronicles']

df = mydb['customersdb']


# Preference

def find_df(answer):
    current_answer = df.find({
        "Do you take advantage of campaigns and discounts when buying coffee?": {
            "$in": [f"{answer}"]
        }
    })
    count = 0

    for i in current_answer:
        count += 1

    return count


number_of_yes = find_df('Yes')
number_of_no = find_df('No')

answers = ["Yes", "No"]

number_of_answer = [number_of_yes, number_of_no]


# **************************Customization**************************

# Figure size and creating args
fig, ax = plt.subplots(figsize=(10, 5))

explodes = [0.01, 0.01]

# Colors
colors = ["#7D4F50", "#D1BE9C"]

patches, texts, autotexts = ax.pie(number_of_answer,
                                   labels=answers,
                                   explode=explodes,
                                   autopct='%1.2f%%',
                                   textprops={'fontsize': 14},
                                   pctdistance=1.30,
                                   labeldistance=.5,
                                   colors=colors,
                                   startangle=90,
                                   counterclock=False, )

for text in texts:
    text.set_horizontalalignment('center')
    text.set_fontstyle('italic')

for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_fontstyle('italic')

# Title

plt.title(label="Perception of Coffee Campaigns and Discounts", fontsize='16', fontstyle="italic")

plt.savefig('web/graphs/exported/Figure9.png')
