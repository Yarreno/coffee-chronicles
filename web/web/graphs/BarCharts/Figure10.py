import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pymongo



myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")

mydb = myclient['CaffeineChronicles']

df = mydb['customersdb']

def find_df(answer):
    current_answer = df.find({
        "How much is your budget when buying a coffee?": {
            "$in": [f"{answer}"]
        }
    })
    count = 0

    for i in current_answer:
        count += 1

    return count


lowest_count = find_df("50-60 TL")
medium_low_count = find_df("61-70 TL")
medium_high_count = find_df("71-80 TL")
highest_count = find_df("80+ TL")

x_axis = ["50-60 TL", "61-70 TL", "71-80 TL", "80+ TL"]

y = [lowest_count, medium_low_count, medium_high_count, highest_count]

total = 0
for i in range(len(x_axis)):
    total += y[i]


y_perc = []
for i in range(len(x_axis)):
    y_perc.append((y[i] * 100 / total))




fig, ax = plt.subplots(figsize=(10, 5))


colors = ["#7D4F50", "#D1BE9C", "#AA998F", "#A78776"]


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



plt.xticks(fontsize='8', fontstyle="italic")
plt.title('Budget for Buying Coffee', font, fontsize='16')
plt.xlabel('Budget range', font, labelpad=10)
plt.ylabel('Share of respondents (%)', font, labelpad=10)

plt.savefig('web/graphs/exported/Figure10.png')
