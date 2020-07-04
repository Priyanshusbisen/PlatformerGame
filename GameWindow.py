import pygame
from GameObjects import Player, Floor, bgSprites, coinSprites
import os
pygame.init()

filename = os.path.dirname('C:\\Users\\priya\\OneDrive\\Desktop\\BounceGame\\Images\\background\\game_bg.png\\')

class window():

    def __init__(self,width,height):
        global filename
        self.height = height
        self.width = width
        self.window = pygame.display.set_mode((width,height))
        self.window.fill((135,206,235))
        self.rect = self.window.get_rect()
        self.player_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()
        self.bg_sprites = pygame.sprite.Group()
        self.coinsprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

    def update(self,sun_image):

        self.window.fill((135,205,235))
        self.window.blit(sun_image.image, (800,0))

        for cloud in self.bg_sprites:
            cloud.rect.x -= 1
            if cloud.rect.x + cloud.rect.width <= 0:
                cloud.rect.x = self.width

        if self.player.move_f:

            if self.player.pos.x >= 930:

                self.player.velocity.x = 0
                self.player.pos.x += self.player.velocity.x
                for floor in self.floor_sprites:
                    floor.rect.x -= 8

                    if floor.rect.x + floor.rect.width<0:
                        self.floor_sprites.remove(floor)
                        self.add_floor(self.width-8,536,(66,664,64,64))
                for coin in self.coinsprites:
                    coin.rect.x -=8
                    if coin.rect.x + coin.rect.width<0:
                        self.coinsprites.remove(coin)

        else:
            self.player.velocity.x = 8


    def draw(self):
        self.coinsprites.draw(self.window)
        self.bg_sprites.draw(self.window)
        self.player_sprites.draw(self.window)
        self.floor_sprites.draw(self.window)


    def add_floor(self,posx,posy,rect,size = None):
        if size == None:
            self.floor = Floor(posx,posy,rect)
            self.floor_sprites.add(self.floor)
        else:
            self.floor = Floor(posx,posy,rect,size)
            self.floor_sprites.add(self.floor)

    def add_player(self,posx,posy,imgindex):

        self.player = Player(posx,posy,imgindex)
        self.player_sprites.add(self.player)

    def add_clouds(self,posx,posy,rect,resize = None):
        if resize == None:
            self.cloud = bgSprites(posx,posy,rect)
        else:
            self.cloud = bgSprites(posx,posy,rect,resize)

        self.bg_sprites.add(self.cloud)
    def add_coins(self,posx,posy,rect,resize = None):
        if resize == None:
            self.coin = coinSprites(posx,posy,rect)
        else:
            self.coin = coinSprites(posx,posy,rect,resize)

        self.coinsprites.add(self.coin)

coin_locations = [(300,300),(350,300),(400,300),(450,300),(1000,300),(1050,300),(1100,300),(1150,300),(3000,300),(3050,300),(3100,300),(3150,300)]
screen = window(1280,600)
screen.add_player(94,0,0)
for i in range(21):
    screen.add_floor(i*64,536,(66,664,64,64))
screen.add_clouds(30,430,(670,110,332,91))
screen.add_clouds(330,420,(670,220,340,71))
screen.add_clouds(550,410,(1036,201,131,101))
screen.add_clouds(850,400,(310,70,261,152))
screen.add_clouds(1000,430,(670,110,332,91))
screen.add_clouds(850,400,(310,70,261,152))
for i in coin_locations:
    screen.add_coins(i[0],i[1],(78,486,22,21),(40,40))
sun_image = bgSprites(800,400,(1025,36,137,137))
screen.player_sprites.update(screen.floor_sprites,screen.coinsprites)
screen.floor_sprites.update()
screen.bg_sprites.update()
screen.update(sun_image)
screen.draw()
pygame.display.update()
loop = True

dx_f = 1
dx_b = -1
count_x = 0
while loop:
    pygame.time.delay(30)

    for event in pygame.event.get():



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('yes')
                screen.player.move_f = True


            elif event.key == pygame.K_LEFT:
                screen.player.move_b = True

            elif event.key == pygame.K_SPACE:
                if not screen.player.move_u:
                    screen.player.velocity.y = -20
                    screen.player.gravity.y = 1
                    screen.player.move_u = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                screen.player.move_f = False
                screen.player.image = screen.player.spritesheet.get_image(0)

            elif event.key == pygame.K_LEFT:
                screen.player.move_b = False
                screen.player.image = pygame.transform.flip(screen.player.spritesheet.get_image(0),True,False)

    if screen.player.move_f:
        if not screen.player.move_u:
            screen.player.move(dx_f,int(count_x))
            count_x+= 0.5
            if int(count_x) == 7:
                count_x = 1
        else:
            screen.player.move(dx_f,int(count_x))
        pygame.display.update()

    if screen.player.move_b:
        if not screen.player.move_u:
            screen.player.move(dx_b,int(count_x))
            count_x += 0.5
            if int(count_x) == 7:
                count_x = 1
        else:
            screen.player.move(dx_b,int(count_x))

        pygame.display.update()
    if screen.player.move_u:
        if screen.player.move_f:
            screen.player.image = screen.player.spritesheet.get_image(3)
        elif screen.player.move_b:
            screen.player.image = pygame.transform.flip(screen.player.spritesheet.get_image(3),True,False)

        screen.player.player_jump()

    screen.player_sprites.update(screen.floor_sprites,screen.coinsprites)
    screen.floor_sprites.update()
    screen.bg_sprites.update()
    screen.update(sun_image)
    screen.draw()
    pygame.display.update()