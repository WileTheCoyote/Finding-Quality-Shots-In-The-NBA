import pandas as pd
import math
# Author ~ WileTheCoyote

# Read in csv to data frame
data = pd.read_csv('../shots.csv')

# Create Shot Distance - sqrt of (x^2 + y^2) 
data['shot_dist'] = (data['shot_x']**2 + data['shot_y']**2)**.5

# Create variable for relative shot openness
data['shot_openess'] = (data.defender_distance / data.shot_dist)

# Create dummy variable representing top 1/3rd of shot openess, most open
data['shot_openess_bool'] = 0
data.loc[(data['shot_openess'] >= .42), 'shot_openess_bool'] = (1)


# Absolute value of x and y coordinates
shot_x_abs = abs(data['shot_x'])
shot_y_abs = abs(data['shot_y'])

# variables for right side of floor, left side, and center
data['rightside'] = 0
data['leftside'] = 0
data['center'] = 0

data.loc[(data.shot_x > 8), 'rightside'] = '1'
data.loc[(data.shot_x > 4) & (data.shot_dist < 21.75), 'rightside'] = '1'
data.loc[(data.shot_x < -8), 'leftside'] = '1'
data.loc[(data.shot_x < -4) & (data.shot_dist < 21.75), 'leftside'] = '1'
data.loc[(shot_x_abs <= 4), 'center'] = '1'
data.loc[(shot_x_abs <= 8) & (data.shot_dist >= 21.75), 'center'] = '1'

# absolute value of defender angle
data['defend_angle_abs'] = abs(data.defender_angle)


# The closer to 1, the more the angle affected the shot
data['defend_angle_rating'] = 0

# categorical variable for defender angle, allowing us to run regression analysis
data.loc[(data.defender_angle >= -15) & (data.defender_angle <= 15), 'angle_rating'] = (1)
data.loc[(data.defender_angle >= -45) & (data.defender_angle < -15), 'angle_rating'] = (2)
data.loc[(data.defender_angle > 15) & (data.defender_angle <= 45), 'angle_rating'] = (2)
data.loc[(data.defender_angle >= -90) & (data.defender_angle < -45), 'angle_rating'] = (3)
data.loc[(data.defender_angle > 45) & (data.defender_angle <= 90), 'angle_rating'] = (3)
data.loc[(data.defender_angle >= -150) & (data.defender_angle < -90), 'angle_rating'] = (4)
data.loc[(data.defender_angle > 90) & (data.defender_angle <= 150), 'angle_rating'] = (4)
data.loc[(data.defender_angle < -150) | (data.defender_angle > 150), 'angle_rating'] = (5)

# hard coded coeficients from regression giving us a multiplier we will use
# openness affect
data.loc[(data.defender_angle >= -15) & (data.defender_angle <= 15), 'defend_angle_rating'] = (.3271)
data.loc[(data.defender_angle >= -45) & (data.defender_angle < -15), 'defend_angle_rating'] = (.3353)
data.loc[(data.defender_angle > 15) & (data.defender_angle <= 45), 'defend_angle_rating'] = (.3353)
data.loc[(data.defender_angle >= -90) & (data.defender_angle < -45), 'defend_angle_rating'] = (.3795)
data.loc[(data.defender_angle > 45) & (data.defender_angle <= 90), 'defend_angle_rating'] = (.3795)
data.loc[(data.defender_angle >= -150) & (data.defender_angle < -90), 'defend_angle_rating'] = (.4515)
data.loc[(data.defender_angle > 90) & (data.defender_angle <= 150), 'defend_angle_rating'] = (.4515)
data.loc[(data.defender_angle < -150) | (data.defender_angle > 150), 'defend_angle_rating'] = (.4739)

# create openess affect variable, which captures not only how open
# a shooter is but also incorporates the angle of the defender, if
# a defender is moderately close to the shooter but behind him, this should
# be accounted for differently than if the defender is directly in
# front of the shooter
data['openess_affect'] = (data.shot_openess * data.defend_angle_rating)

# top 30% of openness affect ~ generally open
data['openess_affect_bool'] = 0
data.loc[(data['openess_affect'] >= 0.148), 'openess_affect_bool'] = (1)

# top 20% of openness affect ~ very open
data['openess_affect_high'] = 0
data.loc[(data['openess_affect'] >= .22), 'openess_affect_high'] = (1)

# next 40% of openness affect ~ semi open
data['openess_affect_medium'] = 0
data.loc[(data['openess_affect'] >= .08) & (data['openess_affect'] < .22),
         'openess_affect_medium'] = (1)
# last 40% of openness affect ~ not open
data['openess_affect_low'] = 0
data.loc[(data['openess_affect'] >= 0) & (data['openess_affect'] < .08), 'openess_affect_low'] = (1)

# set groupings for defender velocity based on shot openness
data['defender_velocity_affect'] = 0
data.loc[(data['shot_openess'] > 0),
         'defender_velocity_affect'] = (data.defender_velocity_ft_sec * 1.5)
data.loc[(data['shot_openess'] > .15),
         'defender_velocity_affect'] = (data.defender_velocity_ft_sec * 1)
data.loc[(data['shot_openess'] > .3),
         'defender_velocity_affect'] = (data.defender_velocity_ft_sec * (.5))
data.loc[(data['shot_openess'] > .5),
         'defender_velocity_affect'] = (data.defender_velocity_ft_sec * (.33))
data.loc[(data['shot_openess'] > .75),
         'defender_velocity_affect'] = (data.defender_velocity_ft_sec * (.25))


data['shot_velocity_plus'] = data.shot_dist * data.shooter_velocity_ft_sec

# Find if shot was a three pointer and what type
# normalize all shots as non three 
data['three_shot'] = '0'
data['corner_three'] = '0'
data['long_three'] = '0'
data['short_three'] = '0'
data['non_corner_three'] = '0'

# Set appropriate shots as specific three point type
data.loc[(data.shot_dist >= 23.75), 'long_three'] = '1'
data.loc[(shot_x_abs >= 22) & (shot_y_abs <= 9.25), 'corner_three'] = '1'
data.loc[(data.long_three == '0') & (data.corner_three == '1'),
         'short_three'] = '1'
data.loc[(data.corner_three == '0') & (data.long_three == '1'),
         'non_corner_three'] = '1'
data.loc[(data.long_three == '1') | (data.short_three == '1'),
         'three_shot'] = '1'



# Find points given for given shot (0, 2, or 3)
# Normalize all shots to zero points 
data['shot_pts'] = '0'
# Award two points if shot is a made 2pt fg
data.loc[(data.made  == 1) & (data.three_shot == '0'), 'shot_pts'] = '2'
# Award three points if shot is a made 3pt fg
data.loc[(data.made == 1) & (data.three_shot == '1'), 'shot_pts'] = '3'

# Calculate made_plus, a variable for eFG%
data['made_plus'] = '0'
data.loc[(data.made == 1) & (data.three_shot == '0'), 'made_plus'] = '1'
data.loc[(data.made == 1) & (data.three_shot == '1'), 'made_plus'] = '1.5'

# Break down dribbles before shot into dummy categories
# zero dribbles
data['shot_spotup'] = '0'
# one dribble
data['shot_rhythm'] = '0'
# two to three dribbles
data['shot_few'] = '0'
# four to seven dribbles
data['shot_several'] = '0'
# eight or more dribbles
data['shot_many'] = '0'

# set dribbles categories
data.loc[(data.dribbles_before  == 0), 'shot_spotup'] = '1'
data.loc[(data.dribbles_before  == 1), 'shot_rhythm'] = '1'
data.loc[(data.dribbles_before  == 2) | (data.dribbles_before  == 3),
         'shot_few'] = '1'
data.loc[(data.dribbles_before  >= 4) & (data.dribbles_before  <= 7),
         'shot_several'] = '1'
data.loc[(data.dribbles_before  >= 8), 'shot_many'] = '1'

# Find shot location groups
# normalize to zero
data.loc[(data.shot_y >= -4.75), 'loc_paint'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_nonpaint_two'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_nonrestricted_paint'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_deep_two'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_medium_two'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_range_three'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_baseline_two'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_baseline_deeptwo'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_restricted'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_above_restricted'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_beside_restricted'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_beside_above_restricted'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_freethrow'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_elbow'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_topkey'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_topkey_deeptwo'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_wing'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_wing_deeptwo'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_beside_topkey'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_topkey_three'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_wing_three'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_deep_three'] = '0'
data.loc[(data.shot_y >= -4.75), 'loc_deep_deep'] = '0'

# set shot locations
data.loc[(data.shot_y <= 14.25) & (data.shot_y >= -4.75) &
         (shot_x_abs <= 8), 'loc_paint'] = '1'
data.loc[(data.shot_dist > 20.75) & (data.three_shot == '0'),
         'loc_deep_two'] = '1'
data.loc[(data.three_shot == '1') & (data.shot_dist <= 29.75)
         & (data.corner_three == '0'), 'loc_range_three'] = '1'
data.loc[(data.shot_y <= 6) & (data.shot_y >= -4.75)
         & (shot_x_abs >= 10) & (shot_x_abs <= 20), 'loc_baseline_two'] = '1'
data.loc[(data.shot_y <= 9.25) & (data.shot_y >= -4.75)
         & (shot_x_abs > 20) & (shot_x_abs < 22), 'loc_baseline_deeptwo'] = '1'
data.loc[(data.shot_dist <= 4) & (data.shot_y >= -4.75),
         'loc_restricted'] = '1'
data.loc[(data.three_shot == '0') & (data.loc_paint == '0'),
         'loc_nonpaint_two'] = '1'
data.loc[(data.loc_restricted == '0') & (data.loc_paint == '1'),
         'loc_nonrestricted_paint'] = '1'
data.loc[(data.loc_deep_two == '0') & (data.loc_nonpaint_two == '1'),
         'loc_medium_two'] = '1'
data.loc[(shot_x_abs <= 4) & (data.shot_dist > 4) & (data.shot_y <= 9)
         & (data.shot_y > 0), 'loc_above_restricted'] = '1'
data.loc[(shot_x_abs > 4) & (shot_x_abs < 10) & (data.shot_y <= 4),
         'loc_beside_restricted'] = '1'
data.loc[(shot_x_abs > 4) & (shot_x_abs < 10) & (data.shot_y > 4)
         & (data.shot_y <= 9), 'loc_beside_above_restricted'] = '1'
data.loc[(shot_x_abs <= 4) & (data.shot_y > 9) & (data.shot_y <= 16.25),
         'loc_freethrow'] = '1'
data.loc[(shot_x_abs > 4) & (shot_x_abs < 10) & (data.shot_y > 9)
         & (data.shot_y <= 16.25), 'loc_elbow'] = '1'
data.loc[(shot_x_abs <= 4) & (data.shot_y > 16.25) & (data.shot_dist < 21.75),
         'loc_topkey'] = '1'
data.loc[(shot_x_abs <= 8) & (data.shot_y > 4) & (data.shot_dist >= 21.75)
         & (data.shot_dist < 23.75), 'loc_topkey_deeptwo'] = '1'
data.loc[(data.shot_y > 9.25) & (shot_x_abs > 8) & (data.shot_dist >= 21.75)
         & (data.shot_dist < 23.75),  'loc_wing_deeptwo'] = '1'
data.loc[(shot_x_abs > 4) & (data.shot_y > 16.25) & (data.shot_dist < 21.75),
         'loc_beside_topkey'] = '1'
data.loc[(data.shot_y > 9) & (shot_x_abs >= 10) & (data.shot_y <= 16.25)
         & (data.shot_dist < 21.75), 'loc_wing'] = '1'
data.loc[(data.shot_y <= 9) & (data.shot_y > 6) & (shot_x_abs >= 10)
         & (shot_x_abs <= 20), 'loc_wing'] = '1'
data.loc[(shot_x_abs <= 8) & (data.shot_dist >= 23.75)
         & (data.shot_dist < 26.75), 'loc_topkey_three'] = '1'
data.loc[(data.shot_y > 9.25) & (shot_x_abs > 8) & (data.shot_dist >= 23.75)
         & (data.shot_dist < 26.75), 'loc_wing_three'] = '1'
data.loc[(data.shot_y > 9.25) & (data.shot_dist >= 26.75)
         & (data.shot_dist < 30.75), 'loc_deep_three'] = '1'
data.loc[(data.shot_y > 9.25) & (data.shot_dist >= 30.75),
         'loc_deep_deep'] = '1'


# save dataframe to new csv
data.to_csv('newShots.csv')
