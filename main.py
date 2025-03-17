import pygame 
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




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
    asteroids = pygame.sprite.Group()  #  Group for all asteroids
    shots_group = pygame.sprite.Group()   #  Group for all shots

    Player.containers = (updatable, drawable) # set the containers for the Player class
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots_group, updatable, drawable)
    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # create a player object
    asteroid_field = AsteroidField() # create an asteroid field object

    #asteroid_group = pygame.sprite.Group()  # create a group to hold the asteroids
    running = True
    while running: 

     
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                running = False  #  Exit the game loop

        screen.fill("black")

        updatable.update(dt)  # Updates all objects in the 'updatable' group

        for asteroid in asteroids:
            if player1.check_collisions(asteroid):  #  Check collision
                print("Game over!") 
                pygame.quit()
                exit()  #  Exit the game immediately
            for shot in shots_group:
                if asteroid.check_collisions(shot):   #  Collision detected
                    #print("Asteroid hit!")  #  Debugging
                    #asteroid.kill()  #  Remove asteroid (before split() was added)
                    asteroid.split()  #  Now calls .split() instead of .kill()
                    shot.kill()  #  Remove bullet
        
        for obj in drawable:  # Loops over 'drawable' objects and draws them
            obj.draw(screen)
        
        
        pygame.display.flip()
        dt = clock.tick(FPS) / 1000  # limit the frame rate to 60 frames per second

         

    
    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

