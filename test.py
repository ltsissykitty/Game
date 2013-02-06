import os, sys, pygame

pygame.init()

tile = 'grass'

path = "tiles/" + tile + "/" + tile + ".txt"

tiledata = [line.strip() for line in open(path, "r")]

print(tiledata)

