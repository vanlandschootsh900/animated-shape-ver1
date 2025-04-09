#Shay VanLandschoot
#--DATE--#
# Pygame game template

import pygame
import sys
import config # Import the config module

def init_game ():

    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) 
   
    
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_rect(screen,x,y,width,height):
    pygame.draw.rect(screen,config.PURPLE,(x,y, width, height))


def draw_text(screen, text, font, font_color, position, anti_aliased=True, italic=False, bold=False):
     img = font.render(text, True, font_color)
     screen.blit(img, position,)


def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():
    
    screen = init_game()
    clock = pygame.time.Clock()

    x=400
    y=300
    new_y=5
    new_x=5
    airal = pygame.font.SysFont('airal',55)
    running = True
    while running:
        running = handle_events()
        screen.fill(config.BLACK) # Use color from config
        
        # Add code to draw stuff (for example) below this comment

        draw_text(screen,'Shay VanLandschoot',airal,config.WHITE,(300,300))

        draw_rect(screen,x,y,50,60)
        x += new_x
        y += new_y
        if x >749 or x <0:
            new_x = new_x*-1
        if y >539 or y<0:
            new_y = new_y*-1
        

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
