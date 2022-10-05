
from re import L


class Bird:
    def __init__(self, start, dir):
        self.pos = start
        
        self.dir = dir

        self.methods = {'f':self.moveForward,'l':self.turnLeft,'r':self.turnRight}

    def moveForward(self):
        if self.dir == 1:
            self.pos[1] = self.pos[1] + 1
        elif self.dir == 2:
            self.pos[0] = self.pos[1] + 1
        elif self.dir == 3:
            self.pos[1] == self.pos[1] - 1
        elif self.dir == 4:
            self.pos[0] == self.pos[0] - 1
        

    def turnLeft(self):
        if self.dir == 1:
            self.dir = 4
        else:
            self.dir -= 1
            

    def turnRight(self):
        if self.dir == 4:
            self.dir = 1
        else:
            self.dir += 1

    def loseGame(self):
        return 'you lost'



class Pig:
    def __init__(self, pos):
        self.pos = pos
        self.is_alive = True
    
    def die(self):
        return 'Uff the pig is dead'
    

class Board:
    def __init__(self):
        self.bird = Bird([2,5],1)
        self.c = Bird.__dict__
        self.pig = Pig([2,7])
    
    def run(self, cmd):
        for i in cmd:
            self.bird.methods[i]()

    def display(self):
            for i in range(1, 11):
                for j in range(1, 11):
                    if (i,j) == tuple(self.bird.pos):
                        print('B', end=' ')
                    elif (i,j) == tuple(self.pig.pos):
                        print('P', end=' ')
                    else:    
                        print('*', end=' ')
                print()

class Workspace:
    def __init__(self):
        self.moves = None

    def instructions(self):
        print('\nwhat steps do you want to perform?')
        print('Options: move forward (f), turn left (l), turn right (r)')
        print('Type "q" when finnished')
    def commands(self):
        l = []
        q = True

        while q:
            x = input('Move: ')
            if x == 'q':
                q = False
            else:
                l.append(x)
            
        return l


class Game:
    def main(self):
        b = Board()
        b.display()

        w = Workspace()
        w.instructions()

        l = w.commands()
        b.run(l)

        print(self.win(b))
        print(f'Birds position: {b.bird.pos}')
        print(f'Pigs position: {b.pig.pos}')

    def win(self, b):
        if b.bird.pos == b.pig.pos:
            return b.pig.die()
        else:
            return b.bird.loseGame()

g = Game()
g.main()

