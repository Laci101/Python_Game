import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats["health"]:
                player.health = player.stats["health"]
            self.animation_player.create_particles('heal',player.rect.center,groups)

    def flame(self,player,cost,groups):
        if player.energy >= cost:
            player.energy -= cost
            temp = randint(0,10)

            if temp == 1:
                if player.status.split("_")[0] == "right":
                    direction = pygame.math.Vector2(1,1)
                elif player.status.split("_")[0] == "left":
                    direction = pygame.math.Vector2(1,1)
                elif player.status.split("_")[0] == "up":
                    direction = pygame.math.Vector2(1,1)
                else:
                    direction = pygame.math.Vector2(1,1)

                for i in range(1,6):
                        offset_x = (direction.x * i) * TILESIZE
                        x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                        y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x,y),groups)

                        offset_x3 = (direction.x * (-i)) * TILESIZE
                        x3 = player.rect.centerx + offset_x3 + randint(-TILESIZE // 3, TILESIZE // 3)
                        y3 = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x3,y3),groups)

                        offset_y= (direction.y * i) * TILESIZE
                        x = player.rect.centerx +  randint(-TILESIZE // 3, TILESIZE // 3)
                        y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x,y),groups)

                        offset_y1= (direction.y * -i) * TILESIZE
                        x1 = player.rect.centerx +  randint(-TILESIZE // 3, TILESIZE // 3)
                        y1 = player.rect.centery + offset_y1 + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x1,y1),groups)

                        offset_x11 = (direction.x * i) * TILESIZE
                        offset_y11= (direction.y * i) * TILESIZE
                        x11 = player.rect.centerx + offset_x11 + randint(-TILESIZE // 3, TILESIZE // 3)
                        y11 = player.rect.centery + offset_y11 + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x11,y11),groups)

                        offset_x12 = (direction.x * (i)) * TILESIZE
                        offset_y12= (direction.y * (-i)) * TILESIZE
                        x12 = player.rect.centerx + offset_x12 + randint(-TILESIZE // 3, TILESIZE // 3)
                        y12 = player.rect.centery + offset_y12 + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x12,y12),groups)

                        offset_y13= (direction.y * i) * TILESIZE
                        offset_x13 = (direction.x * (-i)) * TILESIZE
                        x13 = player.rect.centerx + offset_x13 + randint(-TILESIZE // 3, TILESIZE // 3)
                        y13 = player.rect.centery + offset_y13 + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x13,y13),groups)

                        offset_y14= (direction.y * -i) * TILESIZE
                        offset_x14 = (direction.x * (-i)) * TILESIZE
                        x14 = player.rect.centerx + offset_x14 + randint(-TILESIZE // 3, TILESIZE // 3)
                        y14 = player.rect.centery + offset_y14 + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x14,y14),groups)
            else:
                if player.status.split("_")[0] == "right":
                    direction = pygame.math.Vector2(1,0)
                elif player.status.split("_")[0] == "left":
                    direction = pygame.math.Vector2(-1,0)
                elif player.status.split("_")[0] == "up":
                    direction = pygame.math.Vector2(0,-1)
                else:
                    direction = pygame.math.Vector2(0,1)
                for i in range(1,6):
                    if direction.x:
                        offset_x = (direction.x * i) * TILESIZE
                        x = player.rect.centerx + offset_x + randint(-TILESIZE // 3, TILESIZE // 3)
                        y = player.rect.centery + randint(-TILESIZE // 3, TILESIZE // 3)
                        self.animation_player.create_particles("flame",(x,y),groups)
                    else:
                        offset_y= (direction.y * i) * TILESIZE
                        x = player.rect.centerx +  randint(-TILESIZE // 3, TILESIZE // 3)
                        y = player.rect.centery + offset_y + randint(-TILESIZE // 3, TILESIZE // 3)
                    self.animation_player.create_particles("flame",(x,y),groups)
            