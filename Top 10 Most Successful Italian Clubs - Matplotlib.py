import matplotlib.pyplot as plt

m = [27,26,25,12,10]
labels = ['Juventus','Inter','Milan','Napoli','Roma']

explode_values = [0.05,0.01,0.009,0.006,0.002]
color_values = ['blue', 'red', 'brown', 'green', 'gold']

plt.pie(m, labels=labels,startangle=90,explode=explode_values, colors=color_values)
plt.title("Top 10 Most Successful Italian Football Clubs Of All Time")

plt.show()