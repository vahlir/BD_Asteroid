import pygame
from constants import *
from circleshape import CircleShape  # import the CircleShape class from circleshape.py file




# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
        '''
        self.thrust = 0
        self.max_speed = 300
        self.acceleration = 200
        self.drag = 0.9
        self.shoot_delay = 0.2
        self.last_shot = 0 # time of the last shot 
        '''

    def update(self, dt):
        pass

    # in the player class
    def triangle(self): 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
