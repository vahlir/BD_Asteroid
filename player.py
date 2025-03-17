import pygame
from constants import *
from circleshape import CircleShape  # import the CircleShape class from circleshape.py file
from shot import Shot  # import the Shot class from shot.py file



# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        
        '''
        self.thrust = 0
        self.max_speed = 300
        self.acceleration = 200
        self.drag = 0.9
        self.shoot_delay = 0.2
        self.last_shot = 0 # time of the last shot 
        '''


        

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

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # self.position += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt 
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def update(self, dt):

        self.shot_timer -= dt # decrement the shot timer
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        #if keys[pygame.K_SPACE]:
        #    self.shoot()

        # Inside your main loop or the Player's update method
        if keys[pygame.K_SPACE]:    
            #print("Spacebar pressed!")  # ✅ Debugging
            if self.shot_timer <= 0:
                self.shoot()    




    def shoot(self):
        print("Shooting!")  # ✅ Debugging
        shot = Shot(self.position.x, self.position.y)  # create a shot object
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED  # set the velocity of the shot
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        



        #shot_group.add(shot)  # add the shot to the shot group
        #self.last_shot = pygame.time.get_ticks()  # set the time of the last shot
        #self.shoot_sound.play()  # play the shoot sound 