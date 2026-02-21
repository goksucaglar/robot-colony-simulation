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

  # kontrol
  
  def is_within_bounds(self, x, y):
    return 0 <= x < self.width and 0 <= y < self.height
    
  def is_obstacle(self, x, y): # engel varsa gitmesini engeller
    return self.cells[y][x] == 1

  def is_resource(self, x, y): # kaynak varsa toplamasını sağlar
    return self.cells[y][x] == 2

def get_neighbours(self, x, y): # bu hücreden yürünebilecek komşular hangileri? robotun yürüyebileceği hücreleri listeler
  directions = [(1,0), (-1,0), (0,1), (0,-1)]
  neighbours = []

  for dx, dy in directions: 
    nx, ny = x + dx, y + dy # (nx, ny) → komşu hücrenin koordinatı
    if self.is_within_bounds(nx, ny) and not self.is_obstacle(nx, ny):
      neighbours.append((nx, ny))
      
  return neighbours

# Böylece BFS veya A* algoritması hangi hücreye gidebileceğini kolayca öğrenir.








    
