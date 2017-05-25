"""
march_madness_2016.py

Jon and Sam's March Madness Predictions for 2016

"""

#A list of the teams with the greatest number of expected wins for each seed according to the 538 blog
bracket = {'Kansas': [1,3.48377791], 'Michigan State': [2,2.92073713], 'West Virginia': [3, 2.14677581], 'Kentucky': [4,2.07633746],
            'Purdue': [5,1.81956998], 'Texas': [6, 1.24258193], 'Wisconsin': [7, 1.05294172],
            'St. Josephs': [8, 0.5369509], 'Cincinnati': [9,0.91713515], 'Virginia Commonwealth': [10, 0.9603781], 
            'Wichita State': [11, 1.09511885], 'Yale': [12, 0.57571189], 'North Carolina-Wilmington': [13, 0.21373146], 
            'Stephen F. Austin': [14, 0.24006316], 'Middle Tennessee': [15, 0.0682793], 'Southern/Holy Cross': [16, 0.02258841789]}

#Might want to redo if probabilities are updated after play-in games

import itertools

optimum = [0,'', 0]

for x in itertools.combinations(bracket, 8):
    seed_total = sum(bracket[x[i]][0] for i in xrange(8))
    if seed_total >= 62:
        expected_wins = sum(bracket[x[i]][1] for i in xrange(8))
        if expected_wins > optimum[0]:
            optimum[0] = expected_wins
            optimum[1] = x
            optimum[2] = seed_total

print optimum

#[12.77399297789, ('Michigan State', 'Kansas', 'Middle Tennessee', 'Kentucky', 'Wichita State', 'Virginia Commonwealth', 'Southern/Holy Cross', 'West Virginia'), 62]



