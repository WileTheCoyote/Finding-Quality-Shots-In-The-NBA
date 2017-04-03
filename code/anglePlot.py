import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Arc
# Author ~ WileTheCoyote

# Variable for degree sign 
degree_sign= u'\N{DEGREE SIGN}'

# Intialize figure and axes objects of plot
fig, ax = plt.subplots()

# equalize x and y axis
plt.axis('equal')
plt.axis([-1.2, 1.2, -1.2, 1.2])

# Plot line that go from -1,0 to 1,0 (-90 to 90)
# slightly offset to make both colors visible
plt.plot([-1, 0], [-.005, -.001], color = 'indigo', lw = 2.5)
plt.plot([1, 0], [-.005, -.001], color = 'indigo', lw = 2.5)
plt.plot([-1, 0], [0.012, 0.012], color = 'red', lw = 2.5)
plt.plot([.99, 0], [0.012, 0.012], color = 'red', lw = 2.5)

# y coord for plus and minus 150 degrees
value = (np.sqrt(3))/2

# y coord for plus and minus 45 degrees
value2 = (np.sqrt(2))/2

# y coord for plus and minus 15 degrees
value3 = (((np.sqrt(6) - (np.sqrt(2)))/4))

# y coord for plus and minus 15 degrees
value4 = (((np.sqrt(6) + (np.sqrt(2)))/4))

# Plot lines going from vertex (shooter) to plus and minus 150 degrees
# again slightly offset for visibility
plt.plot([0, -.5], [0, -value], color = 'indigo', lw = 2.5)
plt.plot([0, .5], [0, -value], color = 'indigo', lw = 2.5)
plt.plot([-.015, .478], [0, -value], color = 'gold', lw = 2.5)
plt.plot([.015, -.478], [0, -value], color = 'gold', lw = 2.5)

# Plot lines going from vertex (shooter) to plus and minus 45 degrees
# again slightly offset for visibility
plt.plot([0, value2], [0, value2], color = 'red', lw = 2.5)
plt.plot([0, -value2], [0, value2], color = 'red', lw = 2.5)
plt.plot([-0.015, value2-.0155], [0, value2+.005], color = 'cyan', lw = 2.5)
plt.plot([.015, -value2+.0155], [0, value2+.005], color = 'cyan', lw = 2.5)

# Plot lines going from vertex (shooter) to plus and minus 15 degrees
# again slightly offset for visibility
plt.plot([0, value3], [0, value4], color = 'darkgreen', lw = 2.5)
plt.plot([0, -value3], [0, value4], color = 'darkgreen', lw = 2.5)
plt.plot([-.015, -value3-.015], [0, value4], color = 'cyan', lw = 2.5)
plt.plot([+.015, value3+.015], [0, value4], color = 'cyan', lw = 2.5)

# Plot a circle to represent the hoop (at angle zero from shooter)
hoop = plt.plot(0.00, 1.085, marker='o', markersize=17, color = 'white',
                mew = 2, label='Basket')

# Variables for circle, represented as individual arcs (check labels for location)
arc1 = Arc((0, 0), 2, 2, theta1=75, theta2=105, color='darkgreen',
           lw=3, label='Directly In Front')
arc2 = Arc((0, 0), 2, 2, theta1=45, theta2=75, color='cyan',
           lw=3, label='Partially In Front')
arc3 = Arc((0, 0), 2, 2, theta1=-255, theta2=-225, color='cyan',
           lw=3)
arc4 = Arc((0, 0), 2, 2, theta1=0, theta2=45, color='red',
           lw=3, label='Adjacent/Front')
arc5 = Arc((0, 0), 2, 2, theta1=-225, theta2=-180, color='red',
           lw=3)
arc6 = Arc((0, 0), 2, 2, theta1=-60, theta2=0, color='indigo',
           lw=3, label='Adjacent/Behind')
arc7 = Arc((0, 0), 2, 2, theta1=-180, theta2=-120, color='indigo',
           lw=3)
arc8 = Arc((0, 0), 2, 2, theta1=-120, theta2=-60, color='gold',
           lw=3, label='Directly Behind' )

# Plot a triangle to represent the shooter (at vertex of circle)
shooter = plt.plot(-0.0037, 0.005, marker='^', markersize=20, color = 'white',
                   mew = 2, label='Shooter')

# add arcs (circle) to plot
ax.add_patch(arc1)
ax.add_patch(arc2)
ax.add_patch(arc3)
ax.add_patch(arc4)
ax.add_patch(arc5)
ax.add_patch(arc6)
ax.add_patch(arc7)
ax.add_patch(arc8)

# Degree labels
# 90
ax.text(1.05, -.05, '90' + degree_sign, style='oblique', fontsize=20)
# -90
ax.text(-1.31, -.05, '-90' + degree_sign, style='oblique', fontsize=20)
# 45
ax.text(.72, .72, '45' + degree_sign, style='oblique', fontsize=20)
# -45
ax.text(-.93, .72, '-45' + degree_sign, style='oblique', fontsize=20)
# -15
ax.text(-.44, 1.0, '-15' + degree_sign, style='oblique', fontsize=20)
# 15
ax.text(.19, 1.005, '15' + degree_sign, style='oblique', fontsize=20)
# -150
ax.text(-.81, -1.02, '-150' + degree_sign, style='oblique', fontsize=20)
# 150
ax.text(.42, -1.02, '150' + degree_sign, style='oblique', fontsize=20)

# Add lengend to bottom right of plot
ax.legend(bbox_to_anchor=(1.135, .4), shadow=True, numpoints=1)

# Title
plt.title('Angle Ratings', fontsize=30, style='oblique')

# Save Plot as PNG file
plt.savefig('AngleRatings.png')