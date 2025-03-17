import pygame
from constants import *
from circleshape import CircleShape  # import the CircleShape class from circleshape.py file




# Shot class
class Shot(CircleShape):
    def __init__(self, x, y):   
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)  # Default velocity (won't move unless set)
        print(f"Shot created at {x}, {y}")  # ✅ Debugging

    def update(self, dt):
        self.position += self.velocity * dt  # ✅ Move in a straight line   
        #print(f"Shot moving to {self.position.x}, {self.position.y}")  # ✅ Debugging

    def draw(self, screen):
        #print(f"Drawing shot at {self.position.x}, {self.position.y}")  # ✅ Debugging
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def rotate(self, dt):
        pass

    def move(self, dt):
       pass
   

       



