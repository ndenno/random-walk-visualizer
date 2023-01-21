import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk()   #You can insert any value as a parameter

rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()

point_numbers = range(rw.num_points)

    #highlight the first and last points
ax.scatter(0,0,c='green', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    #hide the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=10)
plt.show()

#Uncomment if you want to see all the x and y values
#print(f"X values: {rw.x_values}")
#print(f"Y values: {rw.y_values}")

