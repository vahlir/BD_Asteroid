# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame 
from constants import *
from player import Player



pygame.init()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()  # create a clock object to help track time 
    dt = 0  # initialize the time delta variable
    FPS = 60  # frames per second
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create a player object at the center of the screen
    
    '''
    player_group = pygame.sprite.Group(player1)  # create a group to hold the player object
    asteroid_group = pygame.sprite.Group()  # create a group to hold the asteroids
    bullet_group = pygame.sprite.Group()  # create a group to hold the bullets
    score = 0  # initialize the score variable
    font = pygame.font.Font(None, 36)  # create a font object to render text
    spawn_time = 0  # initialize the spawn time variable
    game_over = False  # initialize the game over variable'''

    while True: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 

                
        ## screen.fill(color=(0, 0, 0))  alternate way of filling the screen with black
        screen.fill("black")
        player1.draw(screen) # draw the player object on the screen
        pygame.display.flip()
        clock.tick(FPS)  # limit the frame rate to 60 frames per second
        dt = clock.get_time() / 1000  # convert milliseconds to seconds store in dt

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

