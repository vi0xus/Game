#!/usr/bin/python

import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Engine:
    def __init__(self, world):
        self.world = world

    def loop():
        pass

class World:
    units = set()
    def __init__(self, width, height):
        self.width = width
        self.height = height
        #self.earth = [['#' for w in range(width)] for h in range(height)]

    def drawWorld(self):
        for w in range(world.width):
            for h in range(world.height):
                print self.earth[w][h],
            print ""
    def addUnit(self, unit):
        self.units.add(unit)

class Barracks:
    def __init__(self):
        pass

class Unit:
    def __init__(self, x, y, health, name, symbol):
        self.x = x
        self.y = y
        self.health = health
        self.name = name
        self.symbol = symbol

    def move(self, x, y):
        self.x = x
        self.y = y

    def findClosestTarget(self):
    	pass

    def isAlive(self):
   		return self.health > 0

    def isInRange(self, target):
   		return self.getDistance(target) >= 1
   		
    def getDistance(self, target):
   		return math.sqrt((target.x - self.x) + (target.y - self.y))

    def attack(self, unit):
    	pass

    def damage(self, damage):
        self.health = self.health - damage 

if __name__ == "__main__":
    world = World(10, 10)
    enemy = Unit(2, 2, 100, "Enemy", "%")
    hero = Unit(3, 3, 100, "Hero", "&")
    world.addUnit(enemy)
    world.addUnit(hero)

    print hero.isAlive

    hero.move(2, 3)

    #print hero.getDistance(enemy)

    hero.attack(enemy)

    for unit in world.units:
        print unit.name
