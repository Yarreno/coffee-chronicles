import matplotlib.pyplot as plt
import pymongo
import matplotlib.ticker as mtick



myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")

mydb = myclient['CaffeineChronicles']

df = mydb['customersdb']


def find_df(answer):
    current_answer = df.find({
        "What kind of cup do you prefer to drink coffee in?": {
            "$in": [f"{answer}"]
        }
    })
    count = 0

    for i in current_answer:
        count += 1

    return count



thermos_consumption = find_df('Thermos')


plastic_consumption = find_df('Plastic cup')


cardboard_consumption = find_df('Cardboard cup')


mug_consumption = find_df('Mug cup')


cup_consumption = find_df('Cup')

x_axis = ["Thermos", "Plastic cup", "Cardboard cup", "Mug cup", "Cup"]

y = [thermos_consumption, plastic_consumption, cardboard_consumption, mug_consumption, cup_consumption]

total = 0
for i in range(len(x_axis)):
    total += y[i]


y_perc = []
for i in range(len(x_axis)):
    y_perc.append((y[i] * 100 / total))

# **************************Customization**************************


fig, ax = plt.subplots(figsize=(10, 5))


colors = ["#7D4F50", "#D1BE9C", "#AA998F", "#A78776", "#BB9D99"]


font = {'color':  'black',
        'weight': 'normal',
        'size': 11,
        'style': 'italic'
        }


ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0, symbol='%'))


ax.grid(axis="y", visible=True, color='grey', alpha=0.2, linestyle=":")


bar = plt.bar(x_axis, y_perc, width=0.5, color=colors)


for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.1f}%',
             font, ha='center', va='bottom')



plt.xticks(fontsize=8, fontstyle="italic")
plt.title('Cup Preference for Coffee', font, fontsize='16')
plt.xlabel('Types of cups', font, labelpad=10)
plt.ylabel('Share of respondents (%)', font, labelpad=10)

plt.savefig('web/graphs/exported/Figure7.png')
