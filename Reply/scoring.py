# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 11:11:57 2020

@author: Rohan
"""

"""
Function: Movement function
Inputs: 
    c -- vector/list that corresponds to a cell [x,y]
    d -- char that corresponds to direction ('U','D','L','R')
Outputs: 
    c -- cell with new position
"""
def move(c,d):
    if d == 'U':
        c[1] = c[1] - 1
    elif d == 'D':
        c[1] = c[1] + 1
    elif d == 'L':
        c[0] = c[0] - 1
    elif d == 'R':
        c[0] = c[0] + 1
        
    return c 
            
"""
Function: Return cost of a character
Inputs: 
    character -- char that represents a ASCII character of the map
Outputs: 
    cost -- cost associated to the character
"""
def cost(character):
    char_dic = {
            '#': -1,
            '~': 800, 
            '*': 200,
            '+': 150,
            'X': 120,
            '_': 100,
            'H': 70,
            'T': 50,
            }
    
    cost = char_dic[character]
    
    return cost

"""
## ----> NEEDS TO BE IMPLEMENTED!
Function: Reward function
Inputs:
    c -- vector/list that corresponds to a cell [x,y]
    XX -- vector with location of the costumer offices
    XX -- vector with rewards of each costumer office location
Return: 
    reward -- return reward associated to the costumer office location 
(and 0 if no office at that location)
"""
# def reward(c):

"""
Function: Scoring function
Inputs: 
    c -- vector/list of that corresponds to a cell [x,y] representing the location of the reply office
    d_vec -- vector/list that corresponds to the sequence of directions
Outputs:
    score -- score for the initial Reply office and sequence of directions
"""
def score(c,d_vec):
    
    cost_row = 0
    
    for i in range(0,len(d_vec)):
        # return character associated to a position in the map
        map_char = map_function(c)
        # compute cost
        cost_char = cost(map_char)
        # add cost 
        cost_row += cost_char
        # move to next position:
        c = move(c,d_vec[i])
        
    reward_row = reward(c)
    
    score_row = reward_row - cost_row
    
    return score_row

## -- TB Implemented: 
## Function that gets total score
## Reward function
## Bonus function 
## Map function that when you give a cell coordinate you obtain the character located in that position
        

