#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 15:37:47 2018

@author: nam
"""

from random import randint

def build_maze(m,n,swag):
  grid = []
  
  # num rows
  for x in range(m):
    row = []
    for y in range(n):
      row.append('wall')
    grid.append(row)
      
  start_i = randint(0,m-1)
  start_j = randint(0,n-1)

  grid[start_i][start_j] = 'Start'
  
  mow(grid,start_i,start_j)
  #explore_maze(grid,start_i,start_j,swag)

  return grid
  
def print_maze(grid):
  for row in grid:
    printable_row = ""
    for cell in row:
      if cell == 'wall':
        printable_row += '|'
      elif cell == 'empty':
        printable_row += ' '
      else:
        printable_row += cell[0]
        
    print (printable_row)

def mow(grid,i,j):
  directions = ['U','D','R','L']
  
  number_of_steps = 7
  steps = range(1,number_of_steps + 1)
  
  while directions:

    directions_index = randint(0,len(directions) - 1)
    direction = directions.pop(directions_index)
    
    
    if direction == 'U':
      if i - number_of_steps < 0:
        continue
      elif grid[i-number_of_steps][j] == 'wall':
        for step in steps:
            grid[i-step][j] = 'empty'
      mow(grid,i-number_of_steps,j)
      
      
    elif direction == 'D':
        
      if i + number_of_steps >= len(grid):
        continue
      elif grid[i+number_of_steps][j] == 'wall':
        for step in steps:
          grid[i+step][j] = 'empty'
        mow(grid,i+number_of_steps,j)
      
  
    elif direction == 'L':
      if j - number_of_steps < 0:
        continue
      elif grid[i][j - number_of_steps] == 'wall':
        for step in steps:
          grid[i][j-step] = 'empty'
        mow(grid,i,j-number_of_steps)
        
        
    else:
      if j + number_of_steps >= len(grid[0]):
        continue
      elif grid[i][j + number_of_steps] == 'wall':
        for step in steps:
          grid[i][j+step] = 'empty'
        mow(grid,i,j+number_of_steps)
        

def explore_maze(grid,start_i,start_j,swag):
  grid_copy = [row[:] for row in grid]
  bfs_queue = [[start_i,start_j]]
  directions = ['U','D','R','L']
  
  while bfs_queue:
    i,j = bfs_queue.pop(0)
    grid_copy[i][j] = 'visited'
    
    if (randint(0,9) == 0) and (grid[i][j] != 'start'):
      grid[i][j] = swag[randint(0,len(swag) - 1)]

    for direction in directions:
      explore_i = i
      explore_j = j
      
      if direction == 'U':
        explore_i = i - 1

      elif direction == 'D':
        explore_i = i + 1

      elif direction == 'L':
        explore_j = j - 1

      else:
        explore_j = j + 1
      
      if (explore_i < 0) or (explore_j < 0) or (explore_i >= len(grid)) or (explore_j >= len(grid[0])):
        continue
      elif (grid_copy[explore_i][explore_j] != 'visited') and (grid_copy[explore_i][explore_j] != 'wall'):
        bfs_queue.append([explore_i,explore_j])

  grid[i][j] = 'End'

 
print_maze(build_maze(40,100,['*']))