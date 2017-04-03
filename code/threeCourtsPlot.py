import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from matplotlib.patches import Circle, Arc
import math
import re
import matplotlib.cm as cm
# Author ~ WileTheCoyote

# a replacement function for re.sub I found online
# that resolves a bug python experiences with the normal re.sub
def re_sub(pattern, replacement, string):
	def _r(m):
        
		class _m():
			def __init__(self, m):
				self.m=m
				self.string=m.string
			def group(self, n):
				return m.group(n) or ""
        
		return re._expand(pattern, _m(m), replacement)
	
	return re.sub(pattern, _r, string)

# Read in csv to data frame
data = pd.read_csv('../newShots.csv')

# Intialize figure and axes objects of plot
fig = plt.figure()
# subplot for A  shots
ax1 = fig.add_subplot(1,2,1, aspect = 1)
# subplot for NA  shots
ax2 = fig.add_subplot(1,2,2, aspect= 1)
# subplot for Not  shots


# figure title
plt.suptitle('eFG% By Region', fontsize=30, style='oblique')

# each subplot title
ax1.set_title('After Off Rebound', fontsize=16, fontweight='bold')
ax2.set_title('Not After Off Rebound', fontsize=16, fontweight='bold')


# sublot axes limits
ax1.axis([-25, 25, -35, 4.75])
ax2.axis([-25, 25, -35, 4.75])


# regex functions removes the zero before each decimal
# Corner Three Shots eFG%
AfterOffCornerThree = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(
                     .3645 + .1269), 2)))
notAfterCornerThree = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(
                     .3694 + .2713 ), 2)))


# Restricted Shots eFG%
AfterOffRestricted = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(.3645
                    + .424), 2)))
notAfterRestricted = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(.3694
                    + .446), 2)))

# Medium Two Shots eFG%
AfterOffMediumTwo = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(.3645
                    ), 2)))
notAfterMediumTwo = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(.3694
                    ), 2)))


# NonRestricted Paint Shots eFG%
AfterOffNonRestrictedPaint = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float
        (.3645 + .1267), 2)))
notAfterNonRestrictedPaint = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float
        (.3694 + .087), 2)))


# Range Three Shots eFG%
AfterOffRangeThree = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(.3645 +
    .1192), 2)))
notAfterRangeThree = re_sub('^(-)?0[.]', '\\1.', ("%.2f" % round(float(.3694 +
    .1582), 2)))


# vaariable for line thickness
lweight = 3

# plot lines for each of three sub plots
ax2.plot([-25, -25], [4.75, -9.25], 'r--', lw=lweight)
ax2.plot([25, 25], [4.75, -9.25], 'r--', lw=lweight)
ax2.plot([-22, -22], [4.75, -9.25], 'r--', lw=lweight)
ax2.plot([22, 22], [4.75, -9.25], 'r--', lw=lweight)

ax2.plot([-22, -25], [-9.25, -9.25], 'r--', lw=2.75)
ax2.plot([22, 25], [-9.25, -9.25], 'r--', lw=2.75)
ax2.plot([-8, -8], [-14.25, 4.75], 'r--', lw=lweight)
ax2.plot([8, 8], [-14.25, 4.75], 'r--', lw=lweight)
ax2.plot([-8, 8], [-14.25, -14.25], 'r--', lw=lweight)

ax1.plot([-25, -25], [4.75, -9.25], 'r--', lw=lweight)
ax1.plot([25, 25], [4.75, -9.25], 'r--', lw=lweight)
ax1.plot([-22, -22], [4.75, -9.25], 'r--', lw=lweight)
ax1.plot([22, 22], [4.75, -9.25], 'r--', lw=lweight)

ax1.plot([-22, -25], [-9.25, -9.25], 'r--', lw=2.75)
ax1.plot([22, 25], [-9.25, -9.25], 'r--', lw=1.75)
ax1.plot([-8, -8], [-14.25, 4.75], 'r--', lw=lweight)
ax1.plot([8, 8], [-14.25, 4.75], 'r--', lw=lweight)
ax1.plot([-8, 8], [-14.25, -14.25], 'r--', lw=lweight)


# create arcs for each of three subplots, same arcs cannot be used
arc1 = Arc((0, 0), 8, 8, theta1=0, theta2=180, color='r',
           linestyle='dashed', lw=lweight)
arc2 = Arc((0, 0), 8, 8, theta1=180, theta2=0, color='r',
           linestyle='dashed', lw=lweight)
arc3 = Arc((0, 0), 41, 41, theta1=160, theta2=20, color='r',
           linestyle='dashed', lw=lweight)
arc4 = Arc((0, 0), 47.6, 47.6, theta1=202, theta2=-22, color='r',
           linestyle='dashed', lw=lweight)
arc5 = Arc((0, 0), 53, 53, theta1=200, theta2=-20, color='r',
           linestyle='dashed', lw=lweight)
arc1_1 = Arc((0, 0), 8, 8, theta1=0, theta2=180, color='r',
             linestyle='dashed', lw=lweight)
arc2_1 = Arc((0, 0), 8, 8, theta1=180, theta2=0, color='r',
             linestyle='dashed', lw=lweight)
arc3_1 = Arc((0, 0), 41, 41, theta1=160, theta2=20, color='r',
             linestyle='dashed', lw=lweight)
arc4_1 = Arc((0, 0), 47.6, 47.6, theta1=202, theta2=-22, color='red',
             linestyle='dashed', lw=lweight)
arc5_1 = Arc((0, 0), 53, 53, theta1=200, theta2=-20, color='r',
             linestyle='dashed', lw=lweight)

# font size varaibles
fs = 18.5
fs2 = 9.5

# add specific eFG text to each subplot
# 1st plot, A 
ax1.text(-1.2, -1, AfterOffRestricted, style='oblique',
         fontweight='bold', fontsize=fs)
ax1.text(0, -8.5, AfterOffNonRestrictedPaint, style='oblique',
         fontweight='bold', fontsize=fs)
ax1.text(-14.5, -7.5, AfterOffMediumTwo, style='oblique',
         fontweight='bold', fontsize=fs)
ax1.text(1, -25.8, AfterOffRangeThree, style='oblique',
         fontweight='bold', fontsize=fs)
ax1.text(-24.2, -3.7, AfterOffCornerThree, style='oblique',
         fontweight='bold', fontsize=fs, rotation='vertical')
ax1.text(22.2, -.75, AfterOffCornerThree, style='oblique',
         fontweight='bold', fontsize=fs, rotation='270')
# 2nd plot, NA 
ax2.text(-1.2, -1, notAfterRestricted, style='oblique',
         fontweight='bold', fontsize=fs)
ax2.text(0, -8.5, notAfterNonRestrictedPaint, style='oblique',
         fontweight='bold', fontsize=fs)
ax2.text(-14.5, -7.5, notAfterMediumTwo, style='oblique',
         fontweight='bold', fontsize=fs)
ax2.text(1, -25.8, notAfterRangeThree, style='oblique',
         fontweight='bold', fontsize=fs)
ax2.text(-24.2, -3.7, notAfterCornerThree, style='oblique',
         fontweight='bold',  fontsize=fs, rotation='vertical')
ax2.text(22.2, -.75, notAfterCornerThree, style='oblique',
         fontweight='bold', fontsize=fs, rotation='270')


# variables that help manipulate color maping
x = .4
y = 0

# add arcs we created earlier for making shot regions
ax1.add_patch(arc1)
ax1.add_patch(arc2)
#ax1.add_patch(arc3)
ax1.add_patch(arc4)
ax1.add_patch(arc5)

ax2.add_patch(arc1_1)
ax2.add_patch(arc2_1)
#ax2.add_patch(arc3_1)
ax2.add_patch(arc4_1)
ax2.add_patch(arc5_1)


# removes ticks, and tick labels from each plot
ax1.tick_params(
                axis='both',          
                which='both',      
                left ='off',
                right ='off',
                bottom='off',      
                top='off',         
                labelleft='off',
                labelright='off',
                labelbottom='off') 

ax2.tick_params(
                axis='both',          
                which='both',      
                left ='off',
                right ='off',
                bottom='off',     
                top='off',
                labelleft='off',
                labelright='off',
                labelbottom='off')


# add explanatory text to each subplot
ax1.text(-23, -33,'4,006 shots were off an offensive rebound' , style='oblique',
         bbox={'facecolor':'white', 'alpha':0.5, 'pad':10}, size=10)

ax2.text(-23, -33,'23,396 shots were not off an offensive rebound' , style='oblique',
         bbox={'facecolor':'white', 'alpha':0.5, 'pad':10}, size=10)




# fix how tightly teh plots fit together
plt.tight_layout(pad=1.5, w_pad=1, h_pad=0)


# set figure size
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 8)
fig.savefig('Three_C.png', dpi=100)

