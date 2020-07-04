import pygame
class SpriteSheet:
    def __init__(self,filename):
        self.spritesheet = pygame.image.load(filename)

        self.player_list = [(560,50,64,95),(571,173,64,95),(680,172,71,94),(772,172,78,95),(568,291,72,94),(680,290,67,94),(771,290,71,93)]

    def get_image(self,index):
        self.image = pygame.Surface((self.player_list[index][2],self.player_list[index][3]))
        self.image.set_colorkey((247,247,247))
        self.image.blit(self.spritesheet,(0,0),self.player_list[index])
        return self.image
    def get_floor(self,rect,size= None):
        if size == None:
            self.floor_image = pygame.Surface((rect[2], rect[3]))
            self.floor_image.set_colorkey((0, 0, 0))
            self.floor_image.blit(self.spritesheet, (0, 0), rect)

            return self.floor_image
        else:
            self.floor_image = pygame.Surface((rect[2], rect[3]))
            self.floor_image.set_colorkey((0, 0, 0))
            self.floor_image.blit(self.spritesheet, (0, 0), rect)
            self.floor_image = pygame.transform.scale(self.floor_image, size)

            return self.floor_image

    def get_bgsprites(self,rect,resize = None):
        if resize == None:
            self.bg_image = pygame.Surface((rect[2], rect[3]))
            self.bg_image.set_colorkey((0,0,0))
            self.bg_image.blit(self.spritesheet,(0,0),rect)
            return self.bg_image
        else:
            self.bg_image = pygame.Surface((rect[2], rect[3]))
            self.bg_image.set_colorkey((0, 0, 0))
            self.bg_image.blit(self.spritesheet, (0, 0), rect)
            self.bg_image = pygame.transform.scale(self.bg_image,resize)
            return self.bg_image
