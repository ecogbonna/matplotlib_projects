import matplotlib.pyplot as plt

"""data
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]
"""
#new data
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

#plot and style
plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#set title and label
ax.set_title("Cubes", fontsize=20)
ax.set_xlabel('Values', fontsize=18)
ax.set_ylabel('Cube of values', fontsize=18)

#set range of each axis
#ax.axis([0, 5500, 0, 5500000])

#set tick
ax.tick_params(axis='both', labelsize=12)

plt.show()