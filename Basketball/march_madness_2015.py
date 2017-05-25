'''
Find best march madness expected wins

2015
'''

#A list of the teams with the greatest number of expected wins for each seed according to the 538 blog
bracket = {'Villanova': [1,3.3662], 'Arizona': [2,3.2369], 'IowaState': [3, 2.1003], 'NorthCarolina': [4,1.8549],
            'Utah': [5,1.9178], 'Southern Methodist': [6, 1.0233], 'Wichita State': [7, 1.2706],
            'North Carolina St': [8, .7704], 'Oklahoma St': [9,.7343], 'Ohio St': [10, .8765], 
            'Texas': [11, .9065], 'Buffalo': [12, .4780], 'Valparaiso': [13, .3722], 
            'Georgia St': [14, .345], 'New Mexico State': [15, .1159], 'Robert Morris': [16, .0248]}

import itertools

optimum = [0,'', 0]

for x in itertools.combinations(bracket, 8):
    l = sum(bracket[x[i]][0] for i in xrange(8))
    if l >= 62:
        k = sum(bracket[x[i]][1] for i in xrange(8))
        if k > optimum[0]:
            optimum[0] = k
            optimum[1] = x
            optimum[2] = l

print optimum

#[12.774, ('Villanova', 'Ohio St', 'Utah', 'Arizona', 'Texas', 'Georgia St', 'IowaState', 'Robert Morris')]