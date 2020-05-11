from pygame import *
from random import randrange


def color(color, x, y, width):
    draw.rect(window, color, (row_rect * x, col_rect * y, width, col_rect))


class Rain_Drop:
    def __init__(self, x):
        self.length = 1
        self.positions = [[x, 0]]
        self.head = 1
        self.speed = randrange(1, 5)
        color(BLUE, x, 0, self.speed)
        print(self.speed)

    def initial(self):
        self.head += 1
        temp1 = list(self.positions[0])
        temp1[1] += 1
        self.positions.insert(0, [temp1[0], temp1[1]])
        color(BLUE, temp1[0], temp1[1], self.speed)

    def drop(self):
        if len(self.positions) == 0:
            return True
        elif self.positions[0][1] < self.speed:
            for i in range(self.speed):
                self.initial()
        elif self.positions[0][1] >= number_of_rect - 1:
            for i in range(self.speed):
                if len(self.positions) != 0:
                    self.final()
        else:
            for i in range(self.speed):
                self.final()
                self.initial()

    def final(self):
        z = self.positions.pop()
        color(BLACK, z[0], z[1], self.speed)


height = 1000
width = 1000
all_drops = []
number_of_rect = 100
row_rect = height // number_of_rect
col_rect = width // number_of_rect
window = display.set_mode((height, width))
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
window.fill(BLACK)
running = True
drops = []
while running:
    should_remove = []
    for i in range(len(drops)):
        if drops[i].drop():
            should_remove.append(i)
    for i in range(len(should_remove)):
        drops.pop(should_remove[i] - i)
    temp2 = randrange(0, 3)
    for i in range(temp2):
        temp = randrange(0, number_of_rect)
        drops.append(Rain_Drop(temp))
    for even in event.get():
        if even.type == QUIT:
            running = False
    display.update()
    time.delay(10)
quit()
