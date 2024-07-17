import matplotlib.pyplot as plt
import pymongo
import numpy as np


myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")

mydb = myclient['CaffeineChronicles']

df = mydb['customersdb']


def find_df(answer1, answer2):
    current_answer = df.find({
        "$and": [
            {"What is your favorite type of coffee?": {"$in": [f"{answer1}"]}},
            {"What is your gender?": {"$in": [f"{answer2}"]}}
        ]
    })

    count = 0

    for i in current_answer:
        count += 1

    return count


# Number of favorite type of coffees for Male

# Turkish Coffee for Male
number_of_turkishcoffee = find_df('Turkish Coffee', 'Man')


number_of_latte = find_df('Latte', 'Man')

# Cappuccino for Male
number_of_cappuccino = find_df('Cappuccino', 'Man')

# Macchiato for Male
number_of_macchiato = find_df('Macchiato', 'Man')

# Filter Coffee for Male
number_of_filtercoffee = find_df('Filter Coffee', 'Man')

# Flat White for Male
number_of_flatwhite = find_df('Flat White', 'Man')

# Other for Male
number_of_other = find_df('Other', 'Man')

number_of_answer_male = [number_of_turkishcoffee, number_of_latte, number_of_cappuccino,
                         number_of_macchiato, number_of_filtercoffee,
                         number_of_flatwhite, number_of_other]




number_of_turkishcoffee_w = find_df('Turkish Coffee', 'Woman')


number_of_latte_w = find_df('Latte', 'Woman')


number_of_cappuccino_w = find_df('Cappuccino', 'Woman')


number_of_macchiato_w = number_of_macchiato = find_df('Macchiato', 'Woman')


number_of_filtercoffee_w = find_df('Filter Coffee', 'Woman')


number_of_flatwhite_w = find_df('Flat White', 'Woman')


number_of_other_w = find_df('Other', 'Woman')

number_of_answer_female = [number_of_turkishcoffee_w, number_of_latte_w, number_of_cappuccino_w,
                           number_of_macchiato_w, number_of_filtercoffee_w, number_of_flatwhite_w, number_of_other_w]

species = ("Turkish Coffee",
           "Latte",
           "Cappuccino",
           "Macchiato",
           "Filter Coffee",
           "Flat White",
           "Other"
           )

# **************************Customization**************************

fig, ax = plt.subplots(figsize=(10, 5))


font = {'color': 'black',
        'weight': 'normal',
        'size': 11,
        'style': 'italic'
        }

N = 7
ind = np.arange(N)

width = 0.40


bar1 = plt.bar(ind, number_of_answer_male, width, color="#AA998F", label="Male")

for rect in bar1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}',
             font, ha='center', va='bottom')

bar2 = plt.bar(ind + width, number_of_answer_female, width, color="#7D4F50", label="Female")

for rect in bar2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2.0, height, f'{height:.0f}',
             font, ha='center', va='bottom')


ax.grid(axis="y", visible=True, color='grey', alpha=0.2, linestyle=":")


plt.xticks(ind + width / 2, species, fontsize=8, fontstyle="italic")

plt.title(label="Favorite Type of Coffee by Gender", fontsize='16', fontstyle="italic")
plt.xlabel('Types of coffee', font, labelpad=10)
plt.ylabel('Number of respondents', font, labelpad=10)

ax.legend(loc="upper right")

plt.savefig('web/graphs/exported/Figure3.png')
