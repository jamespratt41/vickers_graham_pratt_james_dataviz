import csv
import numpy as np
import matplotlib.pyplot as plt

gold = 0
silver = 0
bronze = 0


with open('data/canada_medals.csv') as f:
  reader = csv.reader(f)



  for row in reader:
      print(row)
      if row[0] == "Gold":
          gold = gold +1

      elif row[0] == "Silver":
          silver = silver +1

      else:
          bronze = bronze +1












# chart for our shiny new data

labels = "Gold,", "Silver","Bronze"
sizes = [gold, silver,bronze]
colors = ['#ffD700', '#c0c0c0','#daa520']
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Total Canadian Medals")
plt.xlabel("Canadian Medals All Sports 1894-2014")
plt.show()
