from pygame import *
from random import randrange


class Cubes:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def color(self, color):
        draw.rect(window, color, (row_rect * self.x, col_rect * self.y, row_rect-10, col_rect))


class Rain_Drop:
    def __init__(self, x):
        self.length = 1
        self.positions = [[x, 0]]
        cubes[x][0].color(BLUE)
        self.head = 1

    def initial(self):
        self.head += 1
        temp1 = list(self.positions[0])
        temp1[1] += 1
        self.positions.insert(0, [temp1[0], temp1[1]])
        cubes[temp1[0]][temp1[1]].color(BLUE)


    def drop(self):
        if len(self.positions) == 0:
            return True
        elif self.positions[0][1] < 2:
            self.initial()
        elif self.positions[0][1] >= number_of_rect-1:
            self.final()
        else:
            self.final()
            self.initial()

    def final(self):
        z = self.positions.pop()
        cubes[z[0]][z[1]].color(BLACK)


height = 1900
width = 950
all_drops = []
number_of_rect = 190
row_rect = height // number_of_rect
col_rect = width // number_of_rect
window = display.set_mode((height, width))
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
cubes = []
for i in range(number_of_rect):
    cubes.append([])
for i in range(number_of_rect):
    for j in range(number_of_rect):
        cubes[i].append(Cubes(i, j))
running = True
cubes[0][0].color(GREEN)
drops = []
while running:
    should_remove = []
    for i in range(len(drops)):
        if drops[i].drop():
            should_remove.append(i)
    for i in range(len(should_remove)):
        drops.pop(should_remove[i] - i)
    temp2 = randrange(0, 2)
    for i in range(temp2):
        temp = randrange(0, number_of_rect)
        drops.append(Rain_Drop(temp))
    for even in event.get():
        if even.type == QUIT:
            running = False
            quit()
    display.update()
    time.delay(0)
