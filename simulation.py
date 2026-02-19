# while loop
def simulate(world, robot, steps = 20):
  step = 0
  while step < steps and robot.energy > 0 :
    print(f"Step {step} Pos: ({robot.x}{robot.y}) Energy: ({robot.energy}")

    right = robot.look_cell("right")
    left = robot.look_cell("left")
    up = robot.look_cell("up")
    down = robot.look_cell("down")

    if right == "source":
      robot.move("right")
    elif left == "source":
      robot.move("left")
    elif up == "source":
      robot.move("up")
    elif down == "source":
      robot.move("down")
    elif right == "empty":
      robot.move("right")
    elif left == "empty":
      robot.move("left")
    elif up == "empty":
      robot.move("up")
    elif down == "empty":
      robot.move("down")

    step += 1
      
    


    
  
