import csv
import numpy as np
import matplotlib.pyplot as plt

# figure out what data we want to use
categories = []
installs = []
ratings = []

with open('data/googeplaystore.csv') as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        # move the page column headers out of the actual data to get a clean dataset
        if line_count is 0: # this will be text, not data
            # print("pushing categories into a seperate array")
            categories.append(row) # push the text into this array
            line_count += 1 # increment the line count fo rthe next loop
        else:
            # print("pushing ratings data into the ratings array")
            ratingsData = row[2]
            ratingsData = ratingsData.replace("NaN","0")
            ratings.append(float(ratingsData))

            installs.append(np.char.strip(ratingsData, "+"))
            line_count += 1

# get some ratings we can work with
# how many ratings are above 4
# how many ratings are below 2
# how many ratings are in the middle


np_ratings = np.array(ratings) #turn a regular array into a numpy array
popular_apps = np_ratings > 4
unpopular_apps = np_ratings < 2
print("popular apps", len(np_ratings[popular_apps]))
percent_popular = len(np_ratings[popular_apps]) / len(np_ratings) * 100
print(percent_popular)
percent_unpopular = len(np_ratings[unpopular_apps]) / len(np_ratings) * 100
print(percent_unpopular)

kinda_popular = int(100 - (percent_popular + percent_unpopular))
print(kinda_popular)

# print('processed', line_count, 'lines of data')
# print(categories)
# print('first row of data:', installs[0])
# print('last row of data:', installs[-1])

# chart for our shiny new data

labels = "Sucks,", "Meh", "I LOVE IT"
sizes = [percent_unpopular, kinda_popular, percent_popular]
colors = ['red', 'yellow', 'green']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Do we love us some apps?")
plt.xlabel("User Ratings - App Installs (10000+ apps)")
plt.show()
