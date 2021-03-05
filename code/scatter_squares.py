import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

#using scatter
ax.scatter(x_values, y_values, c='blue', s=10)

#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

#set title and label axis
ax.set_title('Square Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

#set range of each axis
ax.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plt.png', bbox_inches='tight')

