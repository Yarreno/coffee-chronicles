import matplotlib.pyplot as plt
import pymongo
import matplotlib.ticker as mtick

myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
df = mydb['customersdb']

def find_df(question, answer):
    current_answer = df.find({
        f"{question}": {
            "$in": [f"{answer}"]
        }
    })
    count = 0
    for i in current_answer:
        count += 1
    return count


married = find_df("What is your marital status?", 'Married')
single = find_df("What is your marital status?", 'Single')
divorced = find_df("What is your marital status?", 'Divorced')


one_to_three = find_df("How often do you consume coffee in a week?", 'Per week 1-3')
four_to_six = find_df("How often do you consume coffee in a week?", 'Per week 4-6')
plus_seven = find_df("How often do you consume coffee in a week?", 'Per week +7')



fig, ax = plt.subplots(figsize=(10, 5))


font = {'color': 'black',
        'weight': 'normal',
        'size': 11,
        'style': 'italic'}


colors = ["#7D4F50", "#D1BE9C", "#AA998F", "#A78776", "#BB9D99", "#CC8B86"]


for s in ['top', 'left', 'right']:
    ax.spines[s].set_visible(False)


ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')


ax.grid(axis="y", visible=True, color='grey', alpha=0.2, linestyle=":")


ax.yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0, symbol='%'))


marital_status = ['Married', 'Single', 'Divorced']
frequency = [married, single, divorced]
bars = plt.bar(marital_status, frequency, color=colors)


for rect in bars:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height}',
             font, ha='center', va='bottom')


plt.xticks(fontsize=8, fontstyle="italic")
plt.title('Distribution of Marital Status', fontsize='16', fontstyle='italic')
plt.xlabel('Marital Status', font, labelpad=10)
plt.ylabel('Frequency', font, labelpad=10)

plt.savefig('web/graphs/exported/Figure19.png')
