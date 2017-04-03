import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.patches import Circle, Arc
import math
# Author ~ WileTheCoyote

# Read in csv to data frame
data = pd.read_csv('../newShots.csv')

# Intialize figure and axes objects of plot
fig, ax = plt.subplots()

# find total number of shots from region from data frame
numOfCornerThree = (len(data[(data.corner_three > 0)]))
numOfOpenResricted = (len(data[(data.loc_restricted > 0)]))
numOfNonRestricted = (len(data[(data.loc_nonrestricted_paint > 0)]))
numOfMediumTwo = (len(data[(data.loc_medium_two > 0)]))
numOfDeepTwo  = (len(data[(data.loc_deep_two > 0)]))
numOfRangeThree  = (len(data[(data.loc_range_three > 0)]))

# find total number of shots of specific openess and from region
# very open shots
numOfVeryOpenCornerThree = len(data[(data.corner_three > 0)
                                    & (data.openess_affect_high > 0)])
numOfVeryOpenResricted = len(data[(data.loc_restricted > 0)
                                  & (data.openess_affect_high > 0)])
numOfVeryOpenNonRestricted = len(data[(data.loc_nonrestricted_paint > 0)
                                      & (data.openess_affect_high > 0)])
numOfVeryOpenMediumTwo = len(data[(data.loc_medium_two > 0)
                                  & (data.openess_affect_high > 0)])
numOfVeryOpenDeepTwo = len(data[(data.loc_deep_two > 0)
                                & (data.openess_affect_high > 0)])
numOfVeryOpenRangeThree = len(data[(data.loc_range_three> 0)
                                   & (data.openess_affect_high > 0)])

# semi open shots
numOfFairlyOpenCornerThree = len(data[(data.corner_three > 0)
                                      & (data.openess_affect_medium > 0)])
numOfFairlyOpenResricted = len(data[(data.loc_restricted > 0)
                                    & (data.openess_affect_medium> 0)])
numOfFairlyOpenNonRestricted = len(data[(data.loc_nonrestricted_paint > 0)
                                        & (data.openess_affect_medium > 0)])
numOfFairlyOpenMediumTwo = len(data[(data.loc_medium_two > 0)
                                    & (data.openess_affect_medium > 0)])
numOfFairlyOpenDeepTwo = len(data[(data.loc_deep_two > 0)
                                  & (data.openess_affect_medium > 0)])
numOfFairlyOpenRangeThree = len(data[(data.loc_range_three> 0)
                                     & (data.openess_affect_medium > 0)])

# not open shots
numOfNotOpenCornerThree = len(data[(data.corner_three > 0)
                                   & (data.openess_affect_low > 0)])
numOfNotOpenResricted = len(data[(data.loc_restricted > 0) & (data.openess_affect_low > 0)])
numOfNotOpenNonRestricted = len(data[(data.loc_nonrestricted_paint > 0) & (data.openess_affect_low > 0)])
numOfNotOpenMediumTwo = len(data[(data.loc_medium_two > 0) & (data.openess_affect_low > 0)])
numOfNotOpenDeepTwo = len(data[(data.loc_deep_two > 0) & (data.openess_affect_low > 0)])
numOfNotOpenRangeThree = len(data[(data.loc_range_three> 0) & (data.openess_affect_low > 0)])

# ratio of very open shots to total shots of that region
ratioOfVeryOpenCornerThree = round(float(numOfVeryOpenCornerThree)/float(numOfCornerThree), 3)
ratioOfVeryOpenResricted = round(float(numOfVeryOpenResricted)/float(numOfOpenResricted), 3)
ratioOfVeryOpenNonRestricted = round(float(numOfVeryOpenNonRestricted)/float(numOfNonRestricted), 3)
ratioOfVeryOpenMediumTwo = round(float(numOfVeryOpenMediumTwo)/float
    (numOfMediumTwo), 3)
ratioOfVeryOpenDeepTwo = round(float(numOfVeryOpenDeepTwo)/float
    (numOfDeepTwo), 3)
ratioOfVeryOpenRangeThree = round(float(numOfVeryOpenRangeThree)/float(numOfRangeThree), 3)

# ratio of semi open shots to total shots of that region
ratioOfFairlyOpenCornerThree = round(float(numOfFairlyOpenCornerThree)/float(numOfCornerThree), 3)
ratioOfFairlyOpenResricted = round(float(numOfFairlyOpenResricted)/float(numOfOpenResricted), 3)
ratioOfFairlyOpenNonRestricted = round(float(numOfFairlyOpenNonRestricted)/float(numOfNonRestricted), 3)
ratioOfFairlyOpenMediumTwo = round(float(numOfFairlyOpenMediumTwo)/float(numOfMediumTwo), 3)
ratioOfFairlyOpenDeepTwo = round(float(numOfFairlyOpenDeepTwo)/float(numOfDeepTwo), 3)
ratioOfFairlyOpenRangeThree = round(float(numOfFairlyOpenRangeThree)/float(numOfRangeThree), 3)

# ration of not open shots to total shots of that region
ratioOfNotOpenCornerThree = round(float(numOfNotOpenCornerThree)/float(numOfCornerThree), 3)
ratioOfNotOpenResricted = round(float(numOfNotOpenResricted)/float(numOfOpenResricted), 3)
ratioOfNotOpenNonRestricted = round(float(numOfNotOpenNonRestricted)/float(numOfNonRestricted), 3)
ratioOfNotOpenMediumTwo = round(float(numOfNotOpenMediumTwo)/float
    (numOfMediumTwo), 3)
ratioOfNotOpenDeepTwo = round(float(numOfNotOpenDeepTwo)/float
    (numOfDeepTwo), 3)
ratioOfNotOpenRangeThree = round(float(numOfNotOpenRangeThree)/float(numOfRangeThree), 3)

# Hard code in values from STATA for ordinary least squares (OLS) linear regression
# Regression command: reg made_plus openess_affect_high openess_affect_medium ...
# loc_restricted loc_nonrestricted_paint loc_deep_two loc_medium_two
# corner_three loc_range_three
openessaffectHighCoef = .239394
openessaffectMediumCoef = .0785603
locRestrictedCoef = .3217655
locNonRestrictedPaintCoef = .2533362
locDeepTwoCoef = .1830428
locMediumTwoCoef = .206264
cornerThreeCoef = .3896118
locRangeThreeCoef = .2904125
const = .1131454

# Corner Three Shots eFG%
veryOpenCornerThree = const + openessaffectHighCoef + cornerThreeCoef
semiOpenCornerThree = const + openessaffectMediumCoef + cornerThreeCoef
notOpenCornerThree  = const + cornerThreeCoef

# Restricted Shots eFG%
veryOpenRestricted = const + openessaffectHighCoef + locRestrictedCoef
semiOpenRestricted = const + openessaffectMediumCoef + locRestrictedCoef
notOpenRestricted  = const + locRestrictedCoef

# Medium Two Shots eFG%
veryOpenMediumTwo = const + openessaffectHighCoef + locMediumTwoCoef
semiOpenMediumTwo = const + openessaffectMediumCoef + locMediumTwoCoef
notOpenMediumTwo  = const + locMediumTwoCoef

# NonRestricted Paint Shots eFG%
veryOpenNonRestrictedPaint = const + openessaffectHighCoef + locNonRestrictedPaintCoef
semiOpenNonRestrictedPaint = const + openessaffectMediumCoef + locNonRestrictedPaintCoef
notOpenNonRestrictedPaint  = const + locNonRestrictedPaintCoef

# Deep Two Shots eFG%
veryOpenDeepTwo = const + openessaffectHighCoef + locDeepTwoCoef
semiOpenDeepTwo = const + openessaffectMediumCoef + locDeepTwoCoef
notOpenDeepTwo  = const + locDeepTwoCoef

# Range Three Shots eFG%
veryOpenRangeThree = const + openessaffectHighCoef + locRangeThreeCoef
semiOpenRangeThree = const + openessaffectMediumCoef + locRangeThreeCoef
notOpenRangeThree  = const + locRangeThreeCoef


# create date frame with variable needed for ploting
efgDF = pd.DataFrame({'Shot Location': ['Very Open Corner Three',
                                        'Semi Open Corner Three',
                                        'Not Open Corner Three',
                                        'Very Open Restricted',
                                        'Semi Open Restricted',
                                        'Not Open Restricted',
                                        'Very Open Medium Two',
                                        'Semi Open Medium Two',
                                        'Not Open Medium Two',
                                        'Very Open Non Restricted Paint',
                                        'Semi Open Non Restricted Paint',
                                        'Not Open Non Restricted Paint',
                                        'Very Open Deep Two',
                                        'Semi Open Deep Two',
                                        'Not Open Deep Two',
                                        'Very Open Top Three',
                                        'Semi Open Top Three',
                                        'Not Open Top Three'],
                     
                     'efg%': [veryOpenCornerThree,
                              semiOpenCornerThree,
                              notOpenCornerThree,
                              veryOpenRestricted,
                              semiOpenRestricted,
                              notOpenRestricted,
                              veryOpenMediumTwo,
                              semiOpenMediumTwo,
                              notOpenMediumTwo,
                              veryOpenNonRestrictedPaint,
                              semiOpenNonRestrictedPaint,
                              notOpenNonRestrictedPaint,
                              veryOpenDeepTwo,
                              semiOpenDeepTwo,
                              notOpenDeepTwo,
                              veryOpenRangeThree,
                              semiOpenRangeThree,
                              notOpenRangeThree],
                     
                     'Shot Ratio': [ratioOfVeryOpenCornerThree,
                                    ratioOfFairlyOpenCornerThree,
                                    ratioOfNotOpenCornerThree,
                                    ratioOfVeryOpenResricted,
                                    ratioOfFairlyOpenResricted,
                                    ratioOfNotOpenResricted,
                                    ratioOfVeryOpenMediumTwo,
                                    ratioOfFairlyOpenMediumTwo,
                                    ratioOfNotOpenMediumTwo,
                                    ratioOfVeryOpenNonRestricted,
                                    ratioOfFairlyOpenNonRestricted,
                                    ratioOfNotOpenNonRestricted,
                                    ratioOfVeryOpenDeepTwo,
                                    ratioOfFairlyOpenDeepTwo,
                                    ratioOfNotOpenDeepTwo,
                                    ratioOfVeryOpenRangeThree,
                                    ratioOfFairlyOpenRangeThree,
                                    ratioOfNotOpenRangeThree] })

# create new varaibles within newly created data frame
efgDF['efg% Ranking'] = efgDF['efg%'].rank(ascending=False)
efgDF['egf and ratio'] = efgDF['Shot Ratio']+efgDF['efg%']

# color map for bubbles, the less the eFG%, the darker the bubble
colors=cm.hot(efgDF['efg%']-.17)

# create and intialize bubble plot, 1 column, 1 row, in position 1
ax = fig.add_subplot(1,1,1)

# plot bubbles
ax.scatter(efgDF['efg%'],efgDF['efg% Ranking'],
           s=(efgDF['Shot Ratio']*450), color = colors)
# plot and arranfe y ticks
plt.yticks(np.arange(min(efgDF['efg% Ranking']),
                     max(efgDF['efg% Ranking'])+1, 1.0))

# replace y ticks with names of shot types
plt.yticks(efgDF['efg% Ranking'], efgDF['Shot Location'])

# set x tick limits
plt.xlim(min(efgDF['efg%'])-.022, max(efgDF['efg%'])+.02)

# invert axes so high values are over on right hand side of plot
plt.gca().invert_yaxis()

# plot title and x and y label
plt.suptitle('eFG% vs Shot Type', fontsize=24, x=.64, y=.955, style='oblique' )
plt.xlabel('eFG%', fontsize=16, color = 'red')
plt.ylabel('Shot Type', fontsize=16, y=.6, color = 'red' )

# add extra text as defacto legend explaining bubble size
ax.text(.36, 18.8, 'Bubble Size = chance/ease of finding a shot of that type', style='oblique',
        bbox={'facecolor':'white', 'alpha':0.5, 'pad':10}, size=9.3)

# tighten plot and figure layout, so it fits nicely
plt.tight_layout()

# save off finished figure
plt.savefig('eFGShotBubble.png')
