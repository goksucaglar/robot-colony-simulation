# Map class

class Map:
  def __init__(self, width, height):
    self.width = width 
    self.height = height
  
    self.cells = []
    
    for y in range(height):  
      row = []                     
      for x in range(width): 
        row.append(0)             
      self.cells.append(row)         

  def add_obstacle(self, x, y):
    if 0 <= y < self.height and 0 <= x < self.width:
      self.cells[y][x] = 1

  def add_resource(self, x, y):
    if 0 <= y < self.height and 0 <= x < self.width:
      self.cells[y][x] = 2

  def is_within_bounds(self, x, y):
    return 0 <= x < self.width and 0 <= y < self.height
    
  def is_obstacle(self, x, y):
    return self.cells[y][x] == 1

  def is_resource(self, x, y):
    return self.cells[y][x] == 2

