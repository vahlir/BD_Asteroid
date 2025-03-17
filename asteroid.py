import pygame
from constants import *
from circleshape import CircleShape  # import the CircleShape class from circleshape.py file




# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):   
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)  # Default velocity (won't move unless set)

    def update(self, dt):
        self.position += self.velocity * dt  # ✅ Move in a straight line   
        

    

    def draw(self, screen):
        #pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, 2)  incorrect
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def rotate(self, dt):
        pass

    def move(self, dt):
       pass
   

       



