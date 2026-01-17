# programı başlatan kod

from map import Map # map.py dosyasına git, Map class’ını buraya getir.
from robot import Robot

def main():
  world = Map(16, 16)
  world.add_resource(1,1)
  world.add_obstacle(2,0)
  world.add_obstacle(3,0)

robot = Robot(world, 0, 0, 100)

robot1.move("right") # (1,0) - boş, hareket etmeli
print(robot1.x, robot1.y, robot1.energy)
robot1.move("down") # (1,1) - engel var, hareket etmeyecek
print(robot1.x, robot1.y, robot1.energy)
robot1.move("right") # (2,1) - boş, hareket etmeli
print(robot1.x, robot1.y, robot1.energy)

if __name__ == "__main__":
  main()
# Bu dosya direkt çalıştırılıyorsa main() çalışsın. Import ediliyorsa çalışmasın.
