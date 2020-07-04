import pygame
from sprites import SpriteSheet
import os
playerimagePath = os.path.dirname('C:\\Users\\priya\\OneDrive\\Desktop\\BounceGame\\Images\\playerimages\\chrspitesheet.png\\')
floorimagePath = os.path.dirname('C:\\Users\\priya\\OneDrive\\Desktop\\BounceGame\\Images\\Floor images\\sprites_Tiles.png\\')
bgimagepath = os.path.dirname('C:\\Users\\priya\\OneDrive\\Desktop\\BounceGame\\Images\\bgSprites\\2DGrassyPlatformerSprites.png\\')
coinimagepath = os.path.dirname('C:\\Users\\priya\\OneDrive\\Desktop\\BounceGame\\Images\\bgSprites\\sprites_Items.png\\')
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self,posx,posy,imgindex):
        pygame.sprite.Sprite.__init__(self)
        global playerimagePath
        self.posx = posx
        self.posy = 600 - posy
        self.pos = vec(posx,posy)
        self.velocity = vec(8,0)
        self.gravity = vec(0,1)
        self.step = 8
        self.spritesheet = SpriteSheet(playerimagePath)
        self.image = self.spritesheet.get_image(imgindex)
        self.image.set_colorkey((247,247,247))
        self.rect = self.image.get_rect()
        self.rect.center = (posx,posy)
        self.move_f = False
        self.move_b = False
        self.move_u = False
        self.grounded = False

    def update(self,spritegroup,coin_sprites):
        pygame.sprite.spritecollide(self,coin_sprites,True)
        self.gravity.y = 1
        hits = pygame.sprite.spritecollide(self,spritegroup,False)
        if hits and self.velocity.y>=0:
            self.pos.y = hits[0].rect.top + 1
            self.velocity.y = 0
            self.gravity.y = 0
            if self.move_u:
                self.move_u = False

        else:
            self.gravity.y = 1
            self.velocity.y += self.gravity.y
            self.pos.y += self.velocity.y + 0.5*self.gravity.y




        self.rect.midbottom = self.pos
    def move(self,dx,moveindex):
        if not self.move_u:
            if dx == 1:
                self.image = self.spritesheet.get_image(moveindex)
                self.pos.x += dx*self.velocity.x
            else:
                self.image = self.spritesheet.get_image(moveindex)
                self.image = pygame.transform.flip(self.image,True,False)
                self.pos.x += dx*self.velocity.x
        else:
            self.pos.x += dx*self.velocity.x

    def player_jump(self):

        if self.move_u:

            self.velocity.y += self.gravity.y
            self.pos.y += self.velocity.y + 0.5 * self.gravity.y


class Floor(pygame.sprite.Sprite):
    def __init__(self,posx,posy,rect,resize = None):
        pygame.sprite.Sprite.__init__(self)
        global floorimagePath
        self.spritesheet =  SpriteSheet(floorimagePath)
        if resize==None:
            self.image = self.spritesheet.get_floor(rect)
        else:
            self.image = self.spritesheet.get_floor(rect,resize)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy



class bgSprites(pygame.sprite.Sprite):
    def __init__(self,posx,posy,rect,resize = None):
        global bgimagepath
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = SpriteSheet(bgimagepath)
        if resize == None:
            self.image = self.spritesheet.get_bgsprites(rect)
        else:
            self.image = self.spritesheet.get_bgsprites(rect,resize)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = 600 - posy - self.rect.height

class coinSprites(pygame.sprite.Sprite):
    def __init__(self,posx,posy,rect,resize = None):
        global coinimagepath
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = SpriteSheet(coinimagepath)
        if resize == None:
            self.image = self.spritesheet.get_bgsprites(rect)
        else:
            self.image = self.spritesheet.get_bgsprites(rect,resize)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
