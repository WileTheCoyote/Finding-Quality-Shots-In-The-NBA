import matplotlib.pyplot as plt
from scipy.misc import imread
from matplotlib.patches import Circle, Arc
import math
# Author ~ WileTheCoyote

# Intialize figure and axes objects of plot
fig, ax = plt.subplots()

# jpg of bball court
jpgCourt = ('nba-basketball-court.jpg')

# variable for background image of court jpg
court = imread(jpgCourt)

# plot background and set x and y limts of background
plt.imshow(court, extent=[-25.5, 25.4, -42.25, 5.43])

# variable for line thickness
lweight = 3

# plot straight lines for shot regions
plt.plot([-25, -25], [4.75, -9.25], 'r--', lw=lweight)
plt.plot([25, 25], [4.75, -9.25], 'r--', lw=lweight)
plt.plot([-22, -22], [4.75, -9.25], 'r--', lw=lweight)
plt.plot([22, 22], [4.75, -9.25], 'r--', lw=lweight)
plt.plot([-22, -25], [-8.9, -8.9], 'r--', lw=lweight)
plt.plot([22, 25], [-8.9, -8.9], 'r--', lw=lweight)
plt.plot([-8, -8], [-14, 4.75], 'r--', lw=lweight)
plt.plot([8, 8], [-14, 4.75], 'r--', lw=lweight)
plt.plot([-8, 8], [-14, -14], 'r--', lw=lweight)

# plot lines that point from legend text boxes to specific region
plt.plot([-20, -1.7], [-27.78,-1.4], 'k--', lw=1.4)
plt.plot([22, 23], [-27.78,-2], 'k--', lw=1.4)
plt.plot([16, 15], [-29.78,-16.5], 'k--', lw=1.4)
plt.plot([-13.7, 0], [-29.78,-12], 'k--', lw=1.4)
plt.plot([-8.4, 9], [-31.78,-15.5], 'k--', lw=1.4)
plt.plot([9.2, 8], [-31.78,-24], 'k--', lw=1.4)


# create arcs that create shot regions
arc1 = Arc((0, 0), 8, 8, theta1=0, theta2=180, color='r',
           linestyle='dashed', lw=lweight)
arc2 = Arc((0, 0), 8, 8, theta1=180, theta2=0, color='r',
           linestyle='dashed', lw=lweight)
arc3 = Arc((0, 0), 41, 41, theta1=160, theta2=20, color='r',
           linestyle='dashed', lw=lweight)
arc4 = Arc((0, 0), 47.6, 47.6, theta1=202, theta2=-22, color='red',
           linestyle='dashed', lw=lweight)
arc5 = Arc((0, 0), 53, 53, theta1=200, theta2=-20, color='r',
           linestyle='dashed', lw=lweight)

# hoop
hoop = plt.Circle((0, 0), .85, facecolor='none', edgecolor ='black')

# plot legend text
ax.text(-23, -29,'Restricted = < 4ft' , style='oblique',
         bbox={'facecolor':'r', 'alpha':0.5, 'pad':10}, size=6.6)

ax.text(-23, -31,'Non Restricted = In paint and > 4ft' , style='oblique',
        bbox={'facecolor':'r', 'alpha':0.5, 'pad':10}, size=6.6)
ax.text(-23, -33.1,'Mid Range Two = Two and <= 20.75ft' , style='oblique',
        bbox={'facecolor':'red', 'alpha':0.5, 'pad':10}, size=6.6)

ax.text(19.2, -29,'Corner 3pt' , style='oblique',
        bbox={'facecolor':'r', 'alpha':0.5, 'pad':10}, size=6.6)

ax.text(11.45, -31,'Deep Two = Two and > 20.75ft' , style='oblique',
        bbox={'facecolor':'r', 'alpha':0.5, 'pad':10}, size=6.6)
ax.text(8.6, -33.1,'Top Three = Top Three and <= 29.75ft' , style='oblique',
        bbox={'facecolor':'r', 'alpha':0.5, 'pad':10}, size=6.6)

# remove all ticks and tick labels
ax.tick_params(
                axis='both',
                which='both',
                left ='off',
                right ='off',
                bottom='off',
                top='off',
                labelleft='off',
                labelright='off',
                labelbottom='off')

# plot title
plt.suptitle('Six Shot Locations', fontsize=30, style='oblique')

# plot arcs for regions we have already created
ax.add_patch(arc1)
ax.add_patch(arc2)
ax.add_patch(arc3)
ax.add_patch(arc4)
ax.add_patch(arc5)
ax.add_patch(hoop)

# set x and y limits of plot
plt.xlim(-25.1, 25.1)
plt.ylim(-35, 4.75)

# save off finished figure
plt.savefig('sixLocs.png')


