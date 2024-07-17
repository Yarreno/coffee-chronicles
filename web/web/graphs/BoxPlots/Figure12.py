import matplotlib.pyplot as plt
import pymongo


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


male_consumption = [find_df("How often do you consume coffee in a week?", 'Per week 1-3'), 
                    find_df("How often do you consume coffee in a week?", 'Per week 4-6'), 
                    find_df("How often do you consume coffee in a week?", 'Per week +7')]
female_consumption = [find_df("How often do you consume coffee in a week?", 'Per week 1-3'), 
                      find_df("How often do you consume coffee in a week?", 'Per week 4-6'), 
                      find_df("How often do you consume coffee in a week?", 'Per week +7')]


box_colors = ["#7D4F50", "#D1BE9C", "#AA998F"]


fig, ax = plt.subplots(figsize=(8, 6))


font = {'color': 'black',
        'weight': 'normal',
        'size': 11,
        'style': 'italic'}


for s in ['top', 'left', 'right']:
    ax.spines[s].set_visible(False)


ax.grid(axis="y", visible=True, color='grey', alpha=0.2, linestyle=":")

box_plot_data = [male_consumption, female_consumption]
box = plt.boxplot(box_plot_data, patch_artist=True, widths=0.5, vert=True, labels=['Male', 'Female'])


for patch, color in zip(box['boxes'], box_colors):
    patch.set_facecolor(color)


plt.title('Distribution of Coffee Consumption Frequency by Gender', fontsize='16', fontstyle='italic')
plt.xlabel('Gender', font, labelpad=10)
plt.ylabel('Frequency of coffee consumption per week', font, labelpad=10)

plt.savefig('web/graphs/exported/Figure12.png')
