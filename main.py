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
        self.cur_block_img = pygame.Rect(screen_res[0] - 30, 10, 20, 20)
        
        pygame.init()
        self.font = pygame.font.SysFont('Calibri', 40)
        self.all_game_objs = []
        
    def draw_cur_block(self):
        if self.cur_block == 'sand':
            pygame.draw.rect(self.screen, (255,200,0), self.cur_block_img)

        elif self.cur_block == 'rock':
            pygame.draw.rect(self.screen, (80,80,80), self.cur_block_img)

        elif self.cur_block == 'water':
            pygame.draw.rect(self.screen, (0,0,200), self.cur_block_img)
                
    def draw_text(self, text:str, pos:str = [0,0]):
        if pos[0] == 0 and pos[1] == 0:
            pos = [self.screen_res[0]/2, self.screen_res[1]/2]
        text_img = self.font.render(text, True, (255,255,255))
        text_rect = text_img.get_rect()
        text_rect.topleft = tuple(pos) 
        self.screen.blit(text_img, text_rect)
            
    def draw_blocks(self, game_objs):
        objs = 0
        for obj in game_objs:
            objs += 1
            if obj.name == 'sand':
                pygame.draw.rect(self.screen, (255,200,0), obj.rect)
                obj.gravity(game_objs)
            elif obj.name == 'rock':
                pygame.draw.rect(self.screen, (80,80,80), obj.rect)
                obj.gravity(game_objs)
            elif obj.name == 'water':
                pygame.draw.rect(self.screen, (0,0,200), obj.rect)
                obj.gravity(game_objs)
        self.draw_text(str(objs), (60,10))
        
    def draw_all(self):
        self.screen.fill((50,50,50))
        self.draw_blocks(self.all_game_objs)
        self.draw_cur_block()
        self.draw_text(str(self.clock.get_fps())[:2], (10,10))

    def main_loop(self):
        while self.run_game:
            for event in pygame.event.get():
                #quit properly
                if event.type == pygame.QUIT:
                    pygame.quit()   
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x_pos = event.pos[0] 
                    y_pos = event.pos[1]
                    
                    x_pos = float(x_pos) / 10
                    x_pos = int(x_pos)
                    x_pos *= 10
                    
                    y_pos = float(y_pos) / 10
                    y_pos = int(y_pos)
                    y_pos *= 10
                    
                    if self.cur_block == 'sand':
                        new_sand_obj = sand([x_pos,y_pos], self.screen_res[1], self.screen_res[0])
                        self.all_game_objs.append(new_sand_obj)
                        
                    elif self.cur_block == 'rock':
                        new_rock_obj = rock([x_pos,y_pos], self.screen_res[1], self.screen_res[0])
                        self.all_game_objs.append(new_rock_obj)
                        
                    elif self.cur_block == 'water':
                        new_water_obj = water([x_pos,y_pos], self.screen_res[1], self.screen_res[0])
                        self.all_game_objs.append(new_water_obj)
                        
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.cur_block = 'sand'
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                    self.cur_block = 'water'
                    
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    self.cur_block = 'rock'
        
            self.draw_all()
            pygame.display.flip()
            self.clock.tick(self.fps)
                        
if __name__ == '__main__':
    game = sandbox_py()
    game.main_loop()
    