import pygame
from random import randint

class sand:
    
    def __init__(self, pos, v_border, h_border):
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.v_border = v_border
        self.h_border = h_border
        self.name = 'sand'
        self.density = 2
        
    def move_down(self):
        self.rect.y = self.rect.y + 10
        
    def move_left(self):
        self.rect.x -= 10
        self.rect.y += 10
        
    def move_right(self):
        self.rect.x += 10
        self.rect.y += 10
        
    def check_down(self, sands, op = 0):
        down_me = False
        sand_x = None
        sand_y = None
        if len(sands) == 1:
            if sands[0].rect.bottom == self.v_border:
                down_me = True
        elif len(sands) >= 2:
            for sand in sands:
            #move down
                if sand != self:
                    if self.rect.bottom == sand.rect.top and self.rect.x == sand.rect.x:
                        down_me = True
                        sand_x = sand.rect.x
                        sand_y = sand.rect.y
                    elif self.rect.bottom == self.v_border:
                        down_me = True
                        sand_x = None
                        sand_y = None
                    
        if op == 1:
            return [down_me, sand_x, sand_y]
        else:
            return down_me
    
    def check_sides(self, sands):
        left_me = False
        right_me = False
        
        check_down = self.check_down(sands, 1)
        
        if check_down[0] == True and check_down[1] != None and check_down[2] != None:
            for sand in sands:
                if  sand.rect.x == check_down[1] - 10 and sand.rect.y == check_down[2]:
                    left_me = True
                elif check_down[1] == 0:
                    left_me = True
                if check_down[1] + 10 == sand.rect.x and sand.rect.y == check_down[2]:
                    right_me = True
                elif check_down[1] == self.h_border - 10:
                    right_me = True
                        
                  
        if left_me == False and right_me == False and check_down[1] != None and check_down[2] != None:
            n = randint(1,2)
            if n == 1:
                return 'r'
            if n == 2:
                return 'l'
        elif left_me == True and right_me == False:
            return 'r'
        elif left_me == False and right_me == True:
            return 'l'
                
    def gravity(self, sands):
        check_sides = self.check_sides(sands)
        check_down = self.check_down(sands)
        if check_down == False:
            self.move_down()
        elif check_sides == 'l':
            self.move_left()
        elif check_sides == 'r':
            self.move_right()            

class rock:
    
    def __init__(self, pos, v_border, h_border):
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.v_border = v_border
        self.h_border = h_border
        self.name = 'rock'
        self.density = 5
        
    def move_down(self):
        self.rect.y = self.rect.y + 10
        
    def check_down(self, sands, op = 0):
        down_me = False
        sand_x = None
        sand_y = None
        if len(sands) == 1:
            if sands[0].rect.bottom == self.v_border:
                down_me = True
        elif len(sands) >= 2:
            for sand in sands:
            #move down
                if sand != self:
                    if self.rect.bottom == sand.rect.top and self.rect.x == sand.rect.x:
                        down_me = True
                        sand_x = sand.rect.x
                        sand_y = sand.rect.y
                    elif self.rect.bottom == self.v_border:
                        down_me = True
                        sand_x = None
                        sand_y = None
                    
        if op == 1:
            return [down_me, sand_x, sand_y]
        else:
            return down_me
    
    def gravity(self, sands):
        check_down = self.check_down(sands)
        if check_down == False:
            self.move_down()           

class water:
    
    def __init__(self, pos, v_border, h_border):
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)
        self.v_border = v_border
        self.h_border = h_border
        self.name = 'water'
        self.density = 1
        
    def move_down(self):
        self.rect.y = self.rect.y + 10
        
    def move_left(self):
        self.rect.x -= 10
        self.rect.y += 10
        
    def move_right(self):
        self.rect.x += 10
        self.rect.y += 10
        
    def move_rleft(self):
        self.rect.x -= 10
        
    def move_rright(self):
        self.rect.x += 10
        
    def check_down(self, sands, op = 0):
        down_me = False
        sand_x = None
        sand_y = None
        if len(sands) == 1:
            if sands[0].rect.bottom == self.v_border:
                down_me = True
        elif len(sands) >= 2:
            for sand in sands:
            #move down
                if sand != self:
                    if self.rect.bottom == sand.rect.top and self.rect.x == sand.rect.x:
                        down_me = True
                        sand_x = sand.rect.x
                        sand_y = sand.rect.y
                    elif self.rect.bottom == self.v_border:
                        down_me = True
                        sand_x = None
                        sand_y = None
                    
        if op == 1:
            return [down_me, sand_x, sand_y]
        else:
            return down_me
    
    def check_sides(self, sands):
        left_me = False
        right_me = False
        
        check_down = self.check_down(sands, 1)
        
        if check_down[1] != None and check_down[2] != None:
            for sand in sands:
                if  sand.rect.x == check_down[1] - 10 and sand.rect.y == check_down[2]:
                    left_me = True
                elif check_down[1] == 0:
                    left_me = True
                if check_down[1] + 10 == sand.rect.x and sand.rect.y == check_down[2]:
                    right_me = True
                elif check_down[1] == self.h_border - 10:
                    right_me = True
                                   
        if left_me == False and right_me == False and check_down[1] != None and check_down[2] != None:
            n = randint(1,2)
            if n == 1:
                return 'r'
            if n == 2:
                return 'l'
        elif left_me == True and right_me == False:
            return 'r'
        elif left_me == False and right_me == True:
            return 'l'
                
    def check_rsides(self, sands):
        left_me = False
        right_me = False
        
        for sand in sands:
            if sand.rect.x == self.rect.x - 10 and sand.rect.y == self.rect.y:
                left_me = True
            if sand.rect.x == self.rect.x + 10 and sand.rect.y == self.rect.y:
                right_me = True
                
        if left_me == False and self.rect.x == 0:
            left_me = True
        if right_me == False and self.rect.x == self.h_border - 10:
            right_me = True
                
        if left_me == False and right_me == False:
            n = randint(1,2)
            if n == 1:
                return 'r'
            if n == 2:
                return 'l'
        elif left_me == True and right_me == False:
            return 'r'
        elif left_me == False and right_me == True:
            return 'l'
              
    def check_up(self, objs):
        for obj in objs:
            if obj.rect.x == self.rect.x and obj.rect.y == self.rect.y - 10 and obj.density > self.density:
                obj.rect.y += 10
                self.rect.y -= 10
                
    def gravity(self, sands):
        check_sides = self.check_sides(sands)
        check_down = self.check_down(sands)
        check_rsides = self.check_rsides(sands)
        if check_down == False:
            self.move_down()
        elif check_sides == 'l':
            self.move_left()
        elif check_sides == 'r':
            self.move_right()     
        elif check_rsides == 'l':       
            self.move_rleft()
        elif check_rsides == 'r':
            self.move_rright()
        elif self.name == 'water':
            self.check_up(sands)