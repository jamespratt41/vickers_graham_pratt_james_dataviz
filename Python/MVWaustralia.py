import csv
import numpy as np
import matplotlib.pyplot as plt

mencount = 0
womencount = 0



with open('../data/australia_skiing.csv') as f:
  reader = csv.reader(f)



  for row in reader:
      print(row)
      if row[1] == 'Men':
          mencount = mencount +1

      else:
          womencount = womencount +1





objects = ('Men', 'Women',)
y_pos = np.arange(len(objects))
performance = [mencount,womencount,]
colors = ['lightblue', 'lightpink',]


plt.barh(y_pos, performance, align='center', alpha=0.5, color = colors)

plt.yticks(y_pos, objects)
plt.xlabel('Amount')
plt.title('Australian Medals Men vs Women 1894-2014')

plt.show()



#  chart for our shiny new data
#
# labels = "Men,", "Women"
# sizes = [mencount, womencount]
# colors = ['lightblue', 'pink']
# explode = (0.1, 0.15)
#
# plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
# plt.axis('equal')
# plt.legend(labels, loc=1)
# plt.title("Australian Medal Count M v W")
# plt.xlabel("All Medals (B,S,G) 1894-2014")
# plt.show()
