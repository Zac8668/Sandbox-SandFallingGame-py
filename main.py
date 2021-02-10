import pygame
import sys
import time
from blocks import *
import random

run_game = True

def main():
    #start pygame
    pygame.init()
    #variables
    fps = 30
    screen_res = (400,300)
    cur_block = 'sand'

    #setting window
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_res[0], screen_res[1]))
    pygame.display.set_caption('sand')
    
    sand_ = pygame.Rect(screen_res[1] + 70, 10, 20, 20)
    rock_ = pygame.Rect(screen_res[1] + 70, 10, 20, 20)
    water_ = pygame.Rect(screen_res[1] + 70, 10, 20, 20)
    font = pygame.font.SysFont('Calibri', 40)
    
    game_objs = []
    
    def draw_cur_block():
        if cur_block == 'sand':
            pygame.draw.rect(screen, (255,200,0), sand_)

        elif cur_block == 'rock':
            pygame.draw.rect(screen, (80,80,80), rock_)

        elif cur_block == 'water':
            pygame.draw.rect(screen, (0,0,200), water_)
              
    def draw_text(text:str, pos:list = (screen_res[0]/2, screen_res[1]/2)):
        text_img = font.render(text, True, (255,255,255))
        text_rect = text_img.get_rect()
        text_rect.center = (pos) 
        screen.blit(text_img, text_rect)
        
    def draw_sands(game_objs):
        objs = 0
        for obj in game_objs:
            objs += 1
            if obj.name == 'sand':
                pygame.draw.rect(screen, (255,200,0), obj.rect)
                obj.gravity(game_objs)
            elif obj.name == 'rock':
                pygame.draw.rect(screen, (80,80,80), obj.rect)
                obj.gravity(game_objs)
            elif obj.name == 'water':
                pygame.draw.rect(screen, (0,0,200), obj.rect)
                obj.gravity(game_objs)
        draw_text(str(objs), (30,30))

    test = None
    while run_game:
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
                
                if cur_block == 'sand':
                    new_sand_obj = sand([x_pos,y_pos], screen_res[1], screen_res[0])
                    game_objs.append(new_sand_obj)
                elif cur_block == 'rock':
                    new_rock_obj = rock([x_pos,y_pos], screen_res[1], screen_res[0])
                    game_objs.append(new_rock_obj)
                elif cur_block == 'water':
                    new_water_obj = water([x_pos,y_pos], screen_res[1], screen_res[0])
                    game_objs.append(new_water_obj)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                cur_block = 'sand'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                cur_block = 'water'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                cur_block = 'rock'
        
        screen.fill((50,50,50))
        draw_sands(game_objs)
        draw_cur_block()
        draw_text(str(clock.get_fps())[:2], (100,30))
        pygame.display.flip()
        test = clock.tick(fps)
                        
if __name__ == '__main__':
    main()
    