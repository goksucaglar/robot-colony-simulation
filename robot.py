# Robot class

class Robot:
  def __init__(self, world, x, y, energy):
    self.world = world
    self.x = x
    self.y = y
    self.energy = energy
    self.visited = set()
    self.dx = 0 
    self.dy = 0

  def check_cell(self):
    value = self.world.cells[self.y][self.x]
    if value == 2:
      print("Kaynak bulundu, toplanıyor.")
      self.world.cells[self.y][self.x] = 0
      self.energy += 5
  
  def _move_dxdy(self, dx, dy): # _ Bu fonksiyon sınıfın iç işi, dışarıdan kullanma. __ daha gizli 
    self.energy -= 1

    new_x = self.x + dx
    new_y = self.y + dy
     
    if not (0 <= new_y < self.world.height and 0 <= new_x < self.world.width):
      print("Sınır dışı!")
      return

    if self.world.cells[new_y][new_x] == 1:
      print("Engel var.")
      return

    self.x = new_x
    self.y = new_y

    self.visited.add((self.x,self.y))

    self.check_cell()

  def look_cell(self, direction):
    dx = 0
    dy = 0
    
    if direction  == "right":
      dx = 1
    elif direction == "left":
      dx = -1
    elif direction == "up":
      dy = -1
    elif direction == "down":
      dy = 1

    # liste[0] → üst
    # liste[1] → orta
    # liste[2] → alt
    # bu yüzden yukarı cıktıkca azalır -1 

    new_x = self.x + dx
    new_y = self.y + dy
 
    if (0 <= new_y < self.world.height and 0 <= new_x < self.world.width): 
      value = self.world.cells[new_y][new_x]
      if value == 0:
        return "boş"
      elif value == 1:
        return "engel"
      elif value == 2:
        return "kaynak"
    else:
      return "sınır dışı"

  def move(self, direction):
    result = self.look_cell(direction)

    if result == "engel" or result == "sınır dışı":
      print("Hareket Edemem: ", result)
      return

    dx = 0
    dy = 0

    if direction == "right":
      dx = 1
    elif direction == "left":
      dx = -1
    elif direction == "up":
      dy = -1
    elif direction == "down":
      dy = 1

    self._move_dxdy(dx,dy)

  """
  def follow_path(self, path): # sadece 1 adıma bakıyor biz bunu gelişteceğiz 
    if not path or len(path) < 2:
      return

    next_x, next_y = path[1] # path[0] robotun mevcut yeri
    dx = next_x - self.x
    dy = next_y - self.y
    self._move_dxdy(dx, dy) # robotun konumunu günceller, enerji düşürür ve kaynak varsa toplar.
  """

  def follow_full_path(self, path): 
    if not path or len(path) < 2:
      print("Takip edilecek yol yok.")
      return
      
    # path[0] robotun mevcut yeri, path[1:] üzerinden döneceğiz
    for next_x, next_y in path[1:]:
      dx = next_x - self.x
      dy = next_y - self.y

      # Hareket et
      self._move_dxdy(self,dx, dy)
      
      print(f"Hareket → Yeni Pozisyon: ({self.x},{self.y}) | Enerji: {self.energy}")

      if self.energy <= 0 :
        print("Enerji bitti.")
        break
        







    
