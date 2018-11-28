from random import randint
from math import inf

def build_maze(m,n):
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
  end_i,end_j = explore_maze(grid,start_i,start_j)
  
  start_point = [start_i,start_j]
  end_point = [end_i,end_j] 

  return grid,start_point,end_point
  
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
  number_of_steps = 4
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

        
def explore_maze(grid,start_i,start_j):
  grid_copy = [row[:] for row in grid]
  bfs_queue = [[start_i,start_j]]
  directions = ['U','D','R','L']
  
  while bfs_queue:
    i,j = bfs_queue.pop(0)
    grid_copy[i][j] = 'visited'
    

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
  
  return (i,j)

def find_path(grid,start_point,end_point):
    directions = ['U','D','L','R']
    paths_and_distances = []
    
    for row in grid:
        row_list = []
        for cell in row:
            row_list.append([start_point])
        paths_and_distances.append(row_list)
    
    bfs_queue = [start_point]
    visited = set()
    
    
    while bfs_queue:
        current_i,current_j = bfs_queue.pop(0)
        visited.add((current_i,current_j))
        
        if [current_i,current_j] == end_point:
            return paths_and_distances[end_point[0]][end_point[1]]
        
        for direction in directions:
            explore_i = current_i
            explore_j = current_j
            
            if direction == 'U':
                explore_i = current_i - 1
            elif direction == 'D':
                explore_i = current_i + 1
            elif direction == 'L':
                explore_j = current_j - 1
            else:
                explore_j = current_j + 1
            
            if (explore_i < 0) or (explore_j < 0) or (explore_i >= len(grid)) or (explore_j >= len(grid[0])):
                continue
            elif ((explore_i,explore_j) not in visited) and (grid[explore_i][explore_j] != 'wall'):
                bfs_queue.append([explore_i,explore_j])
                current_path_copy = paths_and_distances[current_i][current_j].copy()
                current_path_copy.append([explore_i,explore_j])
                paths_and_distances[explore_i][explore_j] = current_path_copy

        
def print_solution(grid,path):
    path.pop(0)
    path.pop()
    
    for point in path:
        grid[point[0]][point[1]] = '*'

    print_maze(grid)
    
my_maze,start_point,end_point = build_maze(40,80)
print_maze(my_maze)
print('\n\n')
path = find_path(my_maze,start_point,end_point)
print_solution(my_maze,path)
print('Number of steps = {}'.format(len(path) + 1))
