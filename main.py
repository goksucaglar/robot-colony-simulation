# programı başlatan kod

from map import Map # map.py dosyasına git, Map class’ını buraya getir.
from robot import Robot

def main():
  world = Map(16, 16)
  world.add_resource(1,1)
  world.add_obstacle(2,0)
  world.add_obstacle(3,0)

robot = Robot(world, 0, 0, 100)
