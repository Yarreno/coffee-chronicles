import matplotlib.pyplot as plt
import pymongo


myclient = pymongo.MongoClient("mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/")
mydb = myclient['CaffeineChronicles']
df = mydb['customersdb']


def find_df(question, answer):
    current_answer = df.find({f"{question}": {"$in": [f"{answer}"]}})
    count = 0
    for i in current_answer:
        count += 1
    return count


primary_school = find_df("What is your education status?", 'Primary school')
middle_school = find_df("What is your education status?", 'Middle school')
high_school = find_df("What is your education status?", 'High school')
undergraduate = find_df("What is your education status?", 'UnderGraduate')
postgraduate = find_df("What is your education status?", 'ProstGraduate - Doctorate')


x_axis = ["Primary school", "Middle school", "High school", "Undergraduate", "Postgraduate"]
y = [primary_school, middle_school, high_school, undergraduate, postgraduate]


fig, ax = plt.subplots(figsize=(10, 5))


plt.bar(x_axis, y, color="#7D4F50")


plt.title('Distribution of Education Status', fontsize='16', fontstyle='italic')
plt.xlabel('Education Status', fontstyle='italic', labelpad=10)
plt.ylabel('Frequency of Consumption', fontstyle='italic', labelpad=10)


plt.savefig('web/graphs/exported/Figure15.png')
