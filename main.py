import pygame
import sys
import time
from blocks import *

run_game = True

class sandbox_py:
    def __init__(self, fps:int = 30, screen_res:list = [400,300], cur_block:str = 'sand', run_game:bool = True):
        self.run_game = run_game
        self.fps = fps
        self.screen_res = screen_res
        self.cur_block = cur_block
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_res[0], screen_res[1]))
        self.pixelar_sur = pygame.Surface((screen_res[0] / 10, screen_res[1] / 10))
        self.pixel_array = pygame.PixelArray(self.pixelar_sur)
        self.cur_block_img = pygame.Rect(screen_res[0] - 30, 10, 20, 20)
        self.game_objs = []
        
        self.SAND = pygame.Color(255,200,0)
        self.ROCK = pygame.Color(80,80,80)
        self.AIR = pygame.Color(50,50,50)
        
        self.pixel_array.replace((0,0,0), self.AIR)
        self.AIR = 3289650
        
        pygame.init()
        pygame.display.set_caption('sandbox.py')
        self.font = pygame.font.SysFont('Calibri', 40)
        self.all_game_objs = []
        
    def draw_cur_block(self):
        if self.cur_block == 'sand':
            pygame.draw.rect(self.screen, self.SAND, self.cur_block_img)

        elif self.cur_block == 'rock':
            pygame.draw.rect(self.screen, self.ROCK, self.cur_block_img)

        elif self.cur_block == 'water':
            pygame.draw.rect(self.screen, (0,0,200), self.cur_block_img)
                
    def draw_text(self, text:str, pos:str = [0,0]):
        if pos[0] == 0 and pos[1] == 0:
            pos = [self.screen_res[0]/2, self.screen_res[1]/2]
        text_img = self.font.render(text, True, (255,255,255))
        text_rect = text_img.get_rect()
        text_rect.topleft = tuple(pos) 
        self.screen.blit(text_img, text_rect)
            
    def draw_blocks(self):
        pygame.transform.scale(self.pixelar_sur, (self.screen_res[0], self.screen_res[1]), self.screen)
        
    def draw_all(self):
        self.draw_blocks()
        self.draw_cur_block()
        self.draw_text(str(self.clock.get_fps())[:2], (10,10))
        
    def mouse_to_grid(self, event_pos:list):
        x_pos = event_pos[0] 
        y_pos = event_pos[1]
        
        x_pos = float(x_pos) / 10
        x_pos = int(x_pos)
        x_pos *= 10
        
        y_pos = float(y_pos) / 10
        y_pos = int(y_pos)
        y_pos *= 10
        
        y_pos = int(y_pos/10)
        x_pos = int(x_pos/10)
        res = [x_pos, y_pos]
        return res

    def main_loop(self):
        while self.run_game:
            for event in pygame.event.get():
            #quit properly
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    sys.exit()
            #gets mouse coordinates and create block on it
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.mouse_to_grid(event.pos)

                    if self.cur_block == 'sand':
                        if self.pixel_array[pos[0], pos[1]] == self.AIR:
                            new_sand_obj = sand(pos)
                            self.game_objs.append(new_sand_obj)
                        
                    elif self.cur_block == 'rock':
                        if self.pixel_array[pos[0], pos[1]] == self.AIR:
                            new_rock_obj = rock(pos)
                            self.game_objs.append(new_rock_obj)
                        
                    elif self.cur_block == 'water':
                        if self.pixel_array[pos[0], pos[1]] == self.AIR:
                            new_water_obj = water(pos)
                            self.game_objs.append(new_water_obj)
                    
            #change current block    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.cur_block = 'sand'
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.cur_block = 'water'
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.cur_block = 'rock'
        #draw, flip and limit fps of the screen
            objs = 0
            for obj in self.game_objs:
                obj.gravity(self.pixel_array, self.game_objs)
                objs += 1
        
            self.draw_all()
            self.draw_text(str(objs), [60, 10])
            pygame.display.flip()
            self.clock.tick(self.fps)
                        
if __name__ == '__main__':
    game = sandbox_py()
    game.main_loop()
    