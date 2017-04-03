import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc
import math
import re
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

# Intialize figure and axes objects of plot
fig, ax = plt.subplots()

# variable for line weight
lweight = 1.5

# plot lines that will make up our different shot regions
plt.plot([-25, -25], [4.75, -9.25], 'k--', lw=lweight)
plt.plot([25, 25], [4.75, -9.25], 'k--', lw=lweight)
plt.plot([-22, -22], [4.75, -9.25], 'k--', lw=lweight)
plt.plot([22, 22], [4.75, -9.25], 'k--', lw=lweight)
plt.plot([-20, -20], [4.75, -9.25], 'k--', lw=lweight)
plt.plot([20, 20], [4.75, -9.25], 'k--', lw=lweight)
plt.plot([-20, -25], [-9.25, -9.25], 'k--', lw=lweight)
plt.plot([20, 25], [-9.25, -9.25], 'k--', lw=lweight)
plt.plot([-20, -10], [-6, -6], 'k--', lw=lweight)
plt.plot([20, 10], [-6, -6], 'k--', lw=lweight)
plt.plot([-10, -10], [-16.25, 4.75], 'k--', lw=lweight)
plt.plot([10, 10], [-16.25, 4.75], 'k--', lw=lweight)
plt.plot([-10, -4], [-4, -4], 'k--', lw=lweight)
plt.plot([10, 4], [-4, -4], 'k--', lw=lweight)
plt.plot([-4, -4], [-21.5, 4.75], 'k--', lw=lweight)
plt.plot([4, 4], [-21.5, 4.75], 'k--', lw=lweight)
plt.plot([-10, 10], [-9.25, -9.25], 'k--', lw=lweight)
plt.plot([-14, 14], [-16.25, -16.25], 'k--', lw=lweight)
plt.plot([-4, 4], [1.75, 1.75], 'k--', lw=lweight)
plt.plot([-8, -8], [-20.75, -25.35], 'k--', lw=lweight)
plt.plot([8, 8], [-20.75, -25.35], 'k--', lw=lweight)


# create borders of shot regions that are made up of arcs
arc1 = Arc((0, 0), 8, 8, theta1=180, theta2=0, color='k', linestyle='dashed', lw=lweight)
arc2 = Arc((0, 0), 44, 44, theta1=205, theta2=-25, color='k', linestyle='dashed', lw=lweight)
arc3 = Arc((0, 0), 47.6, 47.6, theta1=202, theta2=-22, color='k', linestyle='dashed', lw=lweight)
arc4 = Arc((0, 0), 53, 53, theta1=200, theta2=-20, color='k', linestyle='dashed', lw=lweight)

# create circle for hoop
hoop = plt.Circle((0, 0), .85, facecolor='none', edgecolor ='black')

# harded coded regression values from STATA
# first ensure variable is float, round the number and
# ensure 2 decimal places (turns to string)
# and lastly convert back to float so it can be added with other values
cons = float("%.2f" % round(float(.2040), 2))
baselineTwo = float("%.2f" % round(float(.1149 + float(cons)), 2))
baselineDeepTwo = float("%.2f" % round(float(.1072 + float(cons)), 2))
restricted = float("%.2f" % round(float(.3199 + float(cons)), 2))
aboveRestricted = float("%.2f" % round(float(.2224 + float(cons)), 2))
besideRestricted = float("%.2f" % round(float(.1449 + float(cons)), 2))
besideAboveRestricted = float("%.2f" % round(float(.1281 + float(cons)), 2))
freethrow = float("%.2f" % round(float(.1667 + float(cons)), 2))
elbow = float("%.2f" % round(float(.1589 + float(cons)), 2))
topkey = float("%.2f" % round(float(.1557 + float(cons)), 2))
topkeyDeepTwo = float("%.2f" % round(float(.0752 + float(cons)), 2))
wing = float("%.2f" % round(float(.0824 + float(cons)), 2))
wingDeepTwo = float("%.2f" % round(float(.0581 + float(cons)), 2))
besideTopkey = float("%.2f" % round(float(.1062 + float(cons)), 2))
topkeyThree = float("%.2f" % round(float(.2029 + float(cons)), 2))
wingThree = float("%.2f" % round(float(.1982 + float(cons)), 2))
cornerThree = float("%.2f" % round(float(.2916 + float(cons)), 2))
bool = float("%.2f" % round(float(.1234), 2))
right = float("%.2f" % round(float(.0479), 2))
left = float("%.2f" % round(float(.0394), 2))

# variable for number location offset, which helps make red and blue numbers visible
x = .34

# plot eFG value for open shots, regex function removes the zero before each decimal
ax.text(5.5, -1 + x, re_sub('^(-)?0[.]', '\\1.', str(besideRestricted + right + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-8.5, -1+ x, re_sub('^(-)?0[.]', '\\1.', str(besideRestricted + left + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-18, -2+ x, re_sub('^(-)?0[.]', '\\1.', str(baselineTwo + left + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(12, -2+ x, re_sub('^(-)?0[.]', '\\1.', str(baselineTwo + left + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-16, -10.7+ x, re_sub('^(-)?0[.]', '\\1.', str(wing + left + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(12, -10.7+ x, re_sub('^(-)?0[.]', '\\1.', str(wing + right + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-1.5, -2.75, re_sub('^(-)?0[.]', '\\1.', str(restricted + bool)),
        style='oblique', fontsize=16.75, color='r')
ax.text(5.5, -7.5+ x, re_sub('^(-)?0[.]', '\\1.', str(besideAboveRestricted + right + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-8.5, -7.5+ x, re_sub('^(-)?0[.]', '\\1.', str(besideAboveRestricted + left + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(5.5, -13.5+ x, re_sub('^(-)?0[.]', '\\1.', str(elbow + right + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-8.5, -13.5+ x, re_sub('^(-)?0[.]', '\\1.', str(elbow + left + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-1.5, -13.5+ x, re_sub('^(-)?0[.]', '\\1.', str(freethrow + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-1.5, -7.5+ x, re_sub('^(-)?0[.]', '\\1.', str(aboveRestricted + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-1.5, -19.5+ x, re_sub('^(-)?0[.]', '\\1.', str(topkey + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(-8.9, -19+ x, re_sub('^(-)?0[.]', '\\1.', str(besideTopkey + left + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(5.75, -19+ x, re_sub('^(-)?0[.]', '\\1.', str(besideTopkey + right + bool)),
        style='oblique', fontsize=19, color='r')
ax.text(1, -23.3, re_sub('^(-)?0[.]', '\\1.', str(topkeyDeepTwo + bool)),
        style='oblique', fontsize=14, color='r')
ax.text(-4, -25.95, re_sub('^(-)?0[.]', '\\1.', str(topkeyThree + bool)),
        style='oblique', fontsize=18, color='r')
ax.text(-21.5, -5, re_sub('^(-)?0[.]', '\\1.', str(baselineDeepTwo + left + bool)),
        style='oblique', fontsize=13, rotation='vertical', color='r')
ax.text(-24.3, -1.5, re_sub('^(-)?0[.]', '\\1.', str(cornerThree + bool + left)),
        style='oblique', fontsize=18.5, rotation='vertical', color='r')
ax.text(20.2, -5, re_sub('^(-)?0[.]', '\\1.', str(baselineDeepTwo + bool + right)),
        style='oblique', fontsize=13, rotation=270, color='r')
ax.text(22.3, -1.5, re_sub('^(-)?0[.]', '\\1.', str(cornerThree + bool + right)),
        style='oblique', fontsize=18.5, rotation=270, color='r')
ax.text(-17.5, -19.5, re_sub('^(-)?0[.]', '\\1.', str(wingThree + left + bool)),
        style='oblique', fontsize=18, rotation=-38, color='r')
ax.text(15.5, -18.5+ x, re_sub('^(-)?0[.]', '\\1.', str(wingThree + right + bool)),
        style='oblique', fontsize=18, rotation=42, color='r')
ax.text(-19, -14.75, re_sub('^(-)?0[.]', '\\1.', str(wingDeepTwo + left + bool)),
        style='oblique', fontsize=14.5, rotation=-43, color='r')
ax.text(17.75, -12.75, re_sub('^(-)?0[.]', '\\1.', str(wingDeepTwo + right + bool)),
        style='oblique', fontsize=15, rotation=56, color='r')

# plot eFG values for not open shots
ax.text(5.5, -1.6, re_sub('^(-)?0[.]', '\\1.', str(besideRestricted + right  )),
        style='oblique', fontsize=10, color='b')
ax.text(-8.5, -1.6, re_sub('^(-)?0[.]', '\\1.', str(besideRestricted + left  )),
        style='oblique', fontsize=10, color='b')
ax.text(-18, -2.6, re_sub('^(-)?0[.]', '\\1.', str(baselineTwo + left  )),
        style='oblique', fontsize=10, color='b')
ax.text(12, -2.6, re_sub('^(-)?0[.]', '\\1.', str(baselineTwo + left  )),
        style='oblique', fontsize= 10, color='b')
ax.text(-16, -11.6, re_sub('^(-)?0[.]', '\\1.', str(wing + left  )),
        style='oblique', fontsize= 10, color='b')
ax.text(12, -11.6, re_sub('^(-)?0[.]', '\\1.', str(wing + right  )),
        style='oblique', fontsize= 10, color='b')
ax.text(1.2, -2.75, re_sub('^(-)?0[.]', '\\1.', str(restricted  )),
        style='oblique', fontsize=8, color='b')
ax.text(5.5, -8.1, re_sub('^(-)?0[.]', '\\1.', str(besideAboveRestricted + right  )),
        style='oblique', fontsize= 10, color='b')
ax.text(-8.5, -8.1, re_sub('^(-)?0[.]', '\\1.', str(besideAboveRestricted + left  )),
        style='oblique', fontsize= 10, color='b')
ax.text(5.5, -14.1, re_sub('^(-)?0[.]', '\\1.', str(elbow + right  )),
        style='oblique', fontsize= 10, color='b')
ax.text(-8.5, -14.1, re_sub('^(-)?0[.]', '\\1.', str(elbow + left  )),
        style='oblique', fontsize= 10, color='b')
ax.text(-1.5, -14.1, re_sub('^(-)?0[.]', '\\1.', str(freethrow  )),
        style='oblique', fontsize= 10, color='b')
ax.text(-1.5, -8.1, re_sub('^(-)?0[.]', '\\1.', str(aboveRestricted  )),
        style='oblique', fontsize=10, color='b')
ax.text(-1.5, -20.1, re_sub('^(-)?0[.]', '\\1.', str(topkey  )),
        style='oblique', fontsize=10, color='b')
ax.text(-8.9, -19.6, re_sub('^(-)?0[.]', '\\1.', str(besideTopkey + left  )),
        style='oblique', fontsize=10, color='b')
ax.text(5.75, -19.6, re_sub('^(-)?0[.]', '\\1.', str(besideTopkey + right  )),
        style='oblique', fontsize=10, color='b')
ax.text(2.3, -23.3, re_sub('^(-)?0[.]', '\\1.', str(topkeyDeepTwo  )),
        style='oblique', fontsize=8, color='b')
ax.text(-.9, -25.95, re_sub('^(-)?0[.]', '\\1.', str(topkeyThree  )),
        style='oblique', fontsize=9, color='b')
ax.text(-21.2, -3.2, re_sub('^(-)?0[.]', '\\1.', str(baselineDeepTwo + left  )),
        style='oblique', fontsize=9, rotation='vertical', color='b')
ax.text(-24, 1, re_sub('^(-)?0[.]', '\\1.', str(cornerThree   + left)),
        style='oblique', fontsize=10, rotation='vertical', color='b')
ax.text(20.4, -6.7, re_sub('^(-)?0[.]', '\\1.', str(baselineDeepTwo   + right)),
        style='oblique', fontsize=8, rotation=270, color='b')
ax.text(22.7, -4, re_sub('^(-)?0[.]', '\\1.', str(cornerThree   + right)),
        style='oblique', fontsize=9, rotation=270, color='b')
ax.text(-14.78, -21.1, re_sub('^(-)?0[.]', '\\1.', str(wingThree + left  )),
        style='oblique', fontsize=9, rotation=-30, color='b')
ax.text(17.8, -17.2, re_sub('^(-)?0[.]', '\\1.', str(wingThree + right  )),
        style='oblique', fontsize=9, rotation=49, color='b')
ax.text(-17, -16.35, re_sub('^(-)?0[.]', '\\1.', str(wingDeepTwo + left  )),
        style='oblique', fontsize=8, rotation=-43, color='b')
ax.text(19.5, -11.2, re_sub('^(-)?0[.]', '\\1.', str(wingDeepTwo + right  )),
        style='oblique', fontsize=8, rotation=60, color='b')

# plot region arcs
ax.add_patch(arc1)
ax.add_patch(arc2)
ax.add_patch(arc3)
ax.add_patch(arc4)
ax.add_patch(hoop)

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

# Plot title
ax.set_title('eFG%: Open Vs. Not Open by Specific Shot Location', fontsize=16, style = 'oblique')

# Add legend for open shots
ax.text(-23.3, -33,'Red = Shot Considered Open' , style='oblique',
         bbox={'facecolor':'Red', 'alpha':0.5, 'pad':10}, size=10)
ax.text(-23.3, -31,'Approx. 30% of shots' , size=7)

# Add legend for not open shots
ax.text(4.3, -33,'Blue = Shot Considered Not Open' , style='oblique',
         bbox={'facecolor':'Blue', 'alpha':0.5, 'pad':10}, size=10)

# fix x and y limits
plt.xlim(-25.1, 25.1)
plt.ylim(-35, 4.75)

# save off figure
plt.savefig('specificLocs.png')




