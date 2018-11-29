import csv
import numpy as np
import matplotlib.pyplot as plt

cancount = 0
usacount = 0



with open('../data/canada_vs_usa.csv') as f:
  reader = csv.reader(f)



  for row in reader:
      print(row)
      if row[0] == 'CAN':
          cancount = cancount +1

      else:
          usacount = usacount +1





 # chart for our shiny new data

labels = "CAN,", "USA"
sizes = [cancount, usacount]
colors = ['lightblue', 'pink']
explode = (0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Can vs USA")
plt.xlabel("Hockey Medals CAN vs USA (B,S,G) 1894-2014")
plt.show()
