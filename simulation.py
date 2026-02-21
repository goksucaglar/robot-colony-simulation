# while loop
import random
from collections import deque

def simulate(world, robot, steps = 20):
  step = 0

  start = (robot.x, robot.y)
  goal = None
  
  while step < steps and robot.energy > 0 :
    print(f"Step {step} Pos: ({robot.x},{robot.y}) Energy: ({robot.energy}"))

    right = robot.look_cell("right")
    left = robot.look_cell("left")
    up = robot.look_cell("up")
    down = robot.look_cell("down")

    if right == "kaynak": robot.move("right")
    elif left == "kaynak": robot.move("left")
    elif up == "kaynak": robot.move("up")
    elif down == "kaynak": robot.move("down")
    else:
      empty_directions = []
      if right == "boş" and (robot.x+1, robot.y) not in robot.visited: empty_directions.append("right")
      if left == "boş" and (robot.x-1, robot.y) not in robot.visited: empty_directions.append("left")
      if up == "boş" and (robot.x, robot.y-1) not in robot.visited: empty_directions.append("up")
      if down == "boş" and (robot.x, robot.y+1) not in robot.visited: empty_directions.append("down")

      if empty_directions:
        direction = random.choice(empty_directions)
        print(f"Boş Yönler: {empty_directions} → Seçilen: {direction}")
        # print(f"Hareket denemesi → {direction}") # print("Hareket denemesi → " + direction)
        robot.move(direction)
      else:
        print("Robot hareket edemez.")
        break

    step += 1
     
  def bfs(world, start, goal):
    queue = deque() # double-ended queue    appendleft / append      popleft / pop
    visited = set()
    
    queue.append( (start, [start]) ) # (current_position, path_so_far)
    visited.add(start)

    while queue:
      current, path = queue.popleft()
      if current == goal:
        return path


      x, y = current
      neighbours = [ (x+1, y), (x-1, y), (x, y+1), (x, y-1) ]
        
      for nx, ny in neighbours:  # Tuple unpacking again
        if not ( 0 <= nx < world.width and 0 <= ny < world.height ):
          continue 
        if world.cells[ny][nx] == 1:
          continue
        if (nx, ny) in visited:
          continue
          
        visited.add((nx. ny))
        queue.append(((nx, ny), path + ([nx, ny]))
        




        
        
