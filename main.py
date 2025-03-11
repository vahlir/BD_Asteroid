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

    # Set Player's containers BEFORE creating any Player instances
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable) # set the containers for the Player class
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create a player object

    #asteroid_group = pygame.sprite.Group()  # create a group to hold the asteroids



    '''
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
        #player1.update(dt)  # update the player object
        #player1.draw(screen) # draw the player object on the screen
        updatable.update(dt)  # Updates all objects in the 'updatable' group

        for obj in drawable:  # Loops over 'drawable' objects and draws them
            obj.draw(screen)
        
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # limit the frame rate to 60 frames per second

        #clock.tick(FPS)  # limit the frame rate to 60 frames per second
        # dt = clock.get_time() / 1000  # convert milliseconds to seconds store in dt

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

