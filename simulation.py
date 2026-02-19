# while loop
import random

def simulate(world, robot, steps = 20):
  step = 0
  while step < steps and robot.energy > 0 :
    print(f"Step {step} Pos: ({robot.x},{robot.y}) Energy: ({robot.energy}"))

    right = robot.look_cell("right")
    left = robot.look_cell("left")
    up = robot.look_cell("up")
    down = robot.look_cell("down")

    if right == "kaynak":
      robot.move("right")
    elif left == "kaynak":
      robot.move("left")
    elif up == "kaynak":
      robot.move("up")
    elif down == "kaynak":
      robot.move("down")
    else:
      empty_directions = []

      if right == "boş":
        empty.directions.append("right")
      elif left == "boş":
        empty.directions.append("left")
      elif up == "boş":
        empty.directions.append("up")
      elif down == "boş":
        empty.directions.append("down")

      if empty_directions:
        direction = random.choice(empty_directions)
        robot.move(direction)
      else:
        print("Robot hareket edemez.")
        break

    step += 1
      
    


    
  
