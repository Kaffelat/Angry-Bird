from turtle import position


class Bird:
    def __init__(self):
        self.startPosition = [2,5]
        self.direction = 1

    def moveForward():
        if Bird.direction == 1:
            Bird.startPosition[1] = Bird.startPosition[1] + 1
        elif Bird.direction == 2:
            Bird.startPosition[1] = Bird.startPosition[1] - 1
        elif Bird.direction == 3:
            Bird.direction[0] == Bird.startPosition[0] - 1
        elif Bird.direction == 4:
            Bird.direction[0] == Bird.startPosition[0] + 1
        pass

    def turnLeft():
        pass

    def turnRight():
        pass

class Pig:
    pass

class Board:
    pass

class Workspace:
    pass

class Game:
    pass

