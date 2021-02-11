import pygame
from random import randint

class sand:
    def __init__(self, pos):
        self.pos =  [pos[0], pos[1]]
        self.name = 'sand'
        self.density = 2
        self.SAND = pygame.Color(255,200,0)
        self.AIR = 3289650
        
    def move_down(self, pixel_array):
        try:
            self.pos[1] += 1
            pixel_array[self.pos[0], self.pos[1]-1] = self.AIR
        except IndexError:
            pass
        
    def move_down_left(self, pixel_array):
        try:
            self.pos[0] -= 1
            self.pos[1] += 1
            pixel_array[self.pos[0]+ 1, self.pos[1]-1] = self.AIR
        except IndexError:
            pass
        
    def move_down_right(self, pixel_array):
        try:
            self.pos[0] += 1
            self.pos[1] += 1
            pixel_array[self.pos[0]- 1, self.pos[1]-1] = self.AIR
        except IndexError:
            pass
        
    def check_down(self, pixel_array):
        down_me = False
            #move down
        try:
            if pixel_array[self.pos[0], (self.pos[1])+1] != self.AIR:
                down_me = True
        except IndexError:
            down_me = True
            
        return down_me
    
    def check_down_left(self, pixel_array):
        down_left_me = False
            #move down
        try:
            if pixel_array[self.pos[0]- 1, (self.pos[1])+ 1] != self.AIR and self.check_down(pixel_array) == True and self.pos[1]+1 <= 30:
                down_left_me = True
        except IndexError:
            down_left_me = True
            
        if self.pos[0] <= 0:
            down_left_me = True
            
        return down_left_me
    
    def check_down_right(self, pixel_array):
        down_right_me = False
            #move down
        try:
            if pixel_array[self.pos[0]+ 1, (self.pos[1])+ 1] != self.AIR and self.check_down(pixel_array) == True and self.pos[1]+ 1 <= 30:
                down_right_me = True
        except IndexError:
            down_right_me = True
            
        return down_right_me
                
    def draw_self(self, pixel_array):
        try:
            pixel_array[self.pos[0], self.pos[1]] = self.SAND
        except IndexError:
            pass
    
    def gravity(self, pixel_array, *args, **kwargs):
        check_down = self.check_down(pixel_array)
        check_down_left = self.check_down_left(pixel_array)
        check_down_right = self.check_down_right(pixel_array)

        if check_down == False:
            self.move_down(pixel_array)
            
        elif check_down_left == False and check_down_right == True:
            self.move_down_left(pixel_array)
            
        elif check_down_left == True and check_down_right == False:
            self.move_down_right(pixel_array)
            
        elif check_down_left == False and check_down_right == False:
            n = randint(1,2)
            if n == 1:
                self.move_down_left(pixel_array)
            if n == 2:
                self.move_down_right(pixel_array)

        self.draw_self(pixel_array)            

class rock:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]
        self.name = 'rock'
        self.density = 5
        self.ROCK = pygame.Color(80,80,80)
        self.AIR = 3289650
        
    def move_down(self, pixel_array):
        try:
            self.pos[1] += 1
            pixel_array[self.pos[0], self.pos[1]-1] = self.AIR
        except IndexError:
            pass
        
    def check_down(self, pixel_array):
        down_me = False
            #move down
        try:
            if pixel_array[self.pos[0], (self.pos[1])+1] != self.AIR:
                down_me = True
        except IndexError:
            down_me = True
            
        return down_me
    
    def draw_self(self, pixel_array):
        try:
            pixel_array[self.pos[0], self.pos[1]] = self.ROCK
        except IndexError:
            pass
    
    def gravity(self, pixel_array, *args, **kwargs):
        check_down = self.check_down(pixel_array)
        if check_down == False:
            self.move_down(pixel_array)
        self.draw_self(pixel_array)      

class water:
    
    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]
        self.name = 'water'
        self.density = 1
        self.WATER = pygame.Color(0,0,200)
        self.AIR = 3289650
        
    def move_down(self, pixel_array):
        try:
            self.pos[1] += 1
            pixel_array[self.pos[0], self.pos[1]-1] = self.AIR
        except IndexError:
            pass
        
    def move_left(self, pixel_array):
        try:
            self.pos[0] -= 1
            pixel_array[self.pos[0]+ 1, self.pos[1]] = self.AIR
        except IndexError:
            pass
        
    def move_right(self, pixel_array):
        try:
            self.pos[0] += 1
            pixel_array[self.pos[0]- 1, self.pos[1]] = self.AIR
        except IndexError:
            pass
        
    def move_down_left(self, pixel_array):
        try:
            self.pos[0] -= 1
            self.pos[1] += 1
            pixel_array[self.pos[0]+ 1, self.pos[1]-1] = self.AIR
        except IndexError:
            pass
        
    def move_down_right(self, pixel_array):
        try:
            self.pos[0] += 1
            self.pos[1] += 1
            pixel_array[self.pos[0]- 1, self.pos[1]-1] = self.AIR
        except IndexError:
            pass
        
    def check_down(self, pixel_array):
        down_me = False
            #move down
        try:
            if pixel_array[self.pos[0], (self.pos[1])+1] != self.AIR:
                down_me = True
        except IndexError:
            down_me = True
            
        return down_me
    
    def check_down_left(self, pixel_array):
        down_left_me = False
            #move down
        try:
            if pixel_array[self.pos[0]- 1, (self.pos[1])+ 1] != self.AIR and self.check_down(pixel_array) == True and self.pos[1]+1 <= 30:
                down_left_me = True
        except IndexError:
            down_left_me = True
            
        if self.pos[0] <= 0:
            down_left_me = True
            
        return down_left_me
    
    def check_down_right(self, pixel_array):
        down_right_me = False
            #move down
        try:
            if pixel_array[self.pos[0]+ 1, (self.pos[1])+ 1] != self.AIR and self.check_down(pixel_array) == True and self.pos[1]+ 1 <= 30:
                down_right_me = True
        except IndexError:
            down_right_me = True
            
        return down_right_me
                
    def check_left(self, pixel_array):
        left_me = False
            #move left
        try:
            if pixel_array[self.pos[0]- 1, self.pos[1]] != self.AIR:
                left_me = True
        except IndexError:
            left_me = True
            
        if self.pos[0] <= 0:
            left_me = True
            
        return left_me
            
    def check_right(self, pixel_array):
        right_me = False
            #move right
        try:
            if pixel_array[self.pos[0]+ 1, (self.pos[1])] != self.AIR:
                right_me = True
        except IndexError:
            right_me = True
            
        return right_me
              
    def check_up(self, pixel_array):
        up_me = False
            #move up

        if pixel_array[self.pos[0], self.pos[1]-1] != self.AIR and pixel_array[self.pos[0], self.pos[1]-1] != 200:
            up_me = True

        return up_me
            
    def move_up(self, pixel_array, game_objs):
        for obj in game_objs:
            if obj.pos == [self.pos[0], self.pos[1]- 1]:
                the_one = obj
        try:
            the_one.pos[1] += 1
            self.pos[1] -= 1
        except UnboundLocalError:
            pass
            
    def draw_self(self, pixel_array):
        try:
            pixel_array[self.pos[0], self.pos[1]] = self.WATER
        except IndexError:
            pass
                
    def gravity(self, pixel_array, game_objs):
        check_down = self.check_down(pixel_array)
        check_down_left = self.check_down_left(pixel_array)
        check_down_right = self.check_down_right(pixel_array)
        check_left = self.check_left(pixel_array)
        check_right = self.check_right(pixel_array)

        if check_down == False:
            self.move_down(pixel_array)
            
        elif check_down_left == False and check_down_right == True:
            self.move_down_left(pixel_array)
            
        elif check_down_left == True and check_down_right == False:
            self.move_down_right(pixel_array)
            
        elif check_down_left == False and check_down_right == False:
            n = randint(1,2)
            if n == 1:
                self.move_down_left(pixel_array)
            if n == 2:
                self.move_down_right(pixel_array)
                
        elif check_left == False and check_right == True:
            self.move_left(pixel_array)
            
        elif check_left == True and check_right == False:
            self.move_right(pixel_array)
            
        elif check_left == False and check_right == False:
            n = randint(1,2)
            if n == 1:
                self.move_left(pixel_array)
            if n == 2:
                self.move_right(pixel_array)
                
        if self.name == 'water':
            if self.check_up(pixel_array):
                self.move_up(pixel_array, game_objs)
        
        self.draw_self(pixel_array) 