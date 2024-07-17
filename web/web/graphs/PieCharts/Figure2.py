import matplotlib.pyplot as plt
import pymongo

# 2. * *Pie Chart**: Preference for Hot or Cold Coffee
myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")

mydb = myclient['CaffeineChronicles']

df = mydb['customersdb']

def find_df(answer):
    current_answer = df.find({
        "Do you prefer hot or cold coffee?": {
            "$in": [f"{answer}"]
        }
    })
    count = 0

    for i in current_answer:
        count += 1

    return count


# Preference
number_of_hot = find_df('Hot')
number_of_cold = find_df('Cold')
number_of_both = find_df('Both of them')

answers = ["Hot", "Cold", "Both of them"]

number_of_answer = [number_of_hot, number_of_cold, number_of_both]

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

plt.title(label="Preference for Hot or Cold Coffee", fontsize='14', fontstyle="italic")

plt.savefig('web/graphs/exported/Figure2.png')
 