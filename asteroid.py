import pygame
import random
from constants import *
from circleshape import CircleShape  # import the CircleShape class from circleshape.py file




# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):   
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)  # Default velocity (won't move unless set)

    def update(self, dt):
        self.position += self.velocity * dt  #  Move in a straight line   
        
    def draw(self, screen):
        #pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)  incorrect
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def split(self):
        #  Always remove the current asteroid
        self.kill()

        #  If it's already small, don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  

        #  Generate new random split angle (between 20 and 50 degrees)
        random_angle = random.uniform(20, 50)

        #  Create new velocities for the two smaller asteroids
        velocity1 = self.velocity.rotate(random_angle) * 1.2
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        #  Compute the new smaller radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        #  Create two new asteroids at the same position
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        #  Assign the new velocities
        asteroid1.velocity = velocity1
        asteroid2.velocity = velocity2


'''
    def rotate(self, dt):
        pass

    def move(self, dt):
       pass
'''   

       



