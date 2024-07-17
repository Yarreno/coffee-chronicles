import matplotlib.pyplot as plt
import pymongo

# 8. **Pie Chart**: Perception of Coffee Addiction
myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")

mydb = myclient['CaffeineChronicles']

df = mydb['customersdb']


# Preference

def find_df(answer):
    current_answer = df.find({
        "Do you think you are addicted to coffee?": {
            "$in": [f"{answer}"]
        }
    })
    count = 0

    for i in current_answer:
        count += 1

    return count


number_of_yes = find_df('Yes')
number_of_no = find_df('No')
number_of_undecided = find_df('Undecided')

answers = ["Yes", "No", "Undecided"]

number_of_answer = [number_of_yes, number_of_no, number_of_undecided]

# **************************Customization**************************

# Figure size and creating args
fig, ax = plt.subplots(figsize=(10, 5))

explodes = [0.01, 0.01, 0.01]

# Colors
colors = ["#7D4F50", "#D1BE9C", "#AA998F"]

patches, texts, autotexts = ax.pie(number_of_answer,
                                   labels=answers,
                                   explode=explodes,
                                   autopct='%1.2f%%',
                                   textprops={'fontsize': 14},
                                   pctdistance=1.30,
                                   labeldistance=.5,
                                   colors=colors,
                                   startangle=90,
                                   counterclock=False,)

for text in texts:
    text.set_horizontalalignment('center')
    text.set_fontstyle('italic')

for autotext in autotexts:
    autotext.set_horizontalalignment('center')
    autotext.set_fontstyle('italic')

# Title
plt.title(label="Perception of Coffee Addiction", fontsize='16', fontstyle="italic")


plt.savefig('web/graphs/exported/Figure8.png')