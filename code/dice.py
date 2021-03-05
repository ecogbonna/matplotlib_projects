import matplotlib.pyplot as plt

from die import Die

die_1 = Die()
die_2 = Die()

results = [(die_1.roll() + die_2.roll()) for i in range(1000)]

max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

#preparing the data
x_values = list(range(2, max_result+1))
y_values = frequencies

#preparing the plot
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6,), dpi=128)
ax.bar(x_values, y_values, align='center')

#edit the plot
ax.set_title('Simulation of a dice', fontsize=16)
ax.set_xlabel('Results', fontsize=14)
ax.set_ylabel('Frequencies of Results', fontsize=14)
ax.set_xticks(x_values)
#ax.set_xticklabels(y_values, rotation='vertical')

plt.show()


