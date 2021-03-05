import matplotlib.pyplot as plt

from random_molecular_motion import RandomMotion

#prepare your data
rm = RandomMotion()
rm.fill_motion()

#prepare the plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(rm.x_values, rm.y_values, linewidth=3)

#edit the plot
ax.set_title("Molecular motion", fontsize=14)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
