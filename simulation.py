# while loop
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
    elif right == "boş":
      robot.move("right")
    elif left == "boş":
      robot.move("left")
    elif up == "boş":
      robot.move("up")
    elif down == "boş":
      robot.move("down")

    step += 1
      
    


    
  
