import pygame_menu
import pygame
import random 
from time import sleep
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_f,
    K_d
)

SCREEN_WIDTH=1000
SCREEN_HEIGHT=800

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf=pygame.image.load("images/faust.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
    

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-3)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)
        if self.rect.left < 0:
            self.rect.left=0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right= SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top=0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom= SCREEN_HEIGHT
        
class bullet(pygame.sprite.Sprite):
    def __init__(self):
        super(bullet, self).__init__()
        self.surf = pygame.image.load("images/vaccine.png")
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect=self.surf.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-3)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)
        if self.rect.left < 0:
            self.rect.left=0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right= SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top=0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom= SCREEN_HEIGHT
        if pressed_keys[K_f]:
            self.rect.move_ip(5,0)
            self.speed= 5
        

        
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("images/AFD.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect( center= (
            random.randint(SCREEN_WIDTH+20, SCREEN_WIDTH+100),
            random.randint(0, SCREEN_HEIGHT),
            )    
        )
        self.speed = random.randint(0,3)

    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("images/hildmann.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect( 
            center=(
                random.randint(SCREEN_WIDTH+10, SCREEN_WIDTH +80),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        
    
    def update(self):
        self.rect.move_ip(-1,0)
        if self.rect.right < 0:
            self.kill()


pygame.mixer.init()
pygame.init()




clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))




ADDENEMY= pygame.USEREVENT + 1 
pygame.time.set_timer(ADDENEMY, 600)

ADDCLOUD= pygame.USEREVENT + 2 
pygame.time.set_timer(ADDCLOUD, 2000)



player = Player()
bullet = bullet()


enemies = pygame.sprite.Group()
cloud= pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(bullet)




pygame.mixer.music.load("sounds/E2-new.ogg")
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.9)

move_up_sound = pygame.mixer.Sound("sounds/highend.ogg")
move_down_sound = pygame.mixer.Sound("sounds/lowend.ogg")
collission_sound = pygame.mixer.Sound("sounds/injectionSnd.ogg")
afd_hits_you_sound= pygame.mixer.Sound("sounds/explosion.wav")

move_up_sound.set_volume(0.1)
move_down_sound.set_volume(0.1)
collission_sound.set_volume(0.9)
afd_hits_you_sound.set_volume(1.0)

start= True

while start:    
    
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key== K_ESCAPE:
                start = False
        elif event.type == QUIT:
            start = False       
        elif event.type == ADDENEMY:
            new_enemy= Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            cloud.add(new_cloud)
            all_sprites.add(new_cloud)
            #clouds.play()   

    pressed_keys= pygame.key.get_pressed()
    print('pressed keys')
    player.update(pressed_keys)
    print('update')

    enemies.update()
    cloud.update()
    
    bullet.update(pressed_keys)


    screen.fill((255,0,0))
    print('screenfill')

    

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
        print('draw entitys to the screen')
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        start = False
        move_down_sound.stop()
        move_up_sound.stop()
        pygame.mixer.music.stop()
        pygame.time.delay(50)
        afd_hits_you_sound.play()
        pygame.time.delay(500)

        
    
    
    for enemy in enemies:
        if pygame.sprite.spritecollideany(bullet, enemies):
            collission_sound.play()
            enemy.kill()
            

    


  
    clock.tick(200)
                
    pygame.display.flip()
pygame.mixer.quit()
print('finish')

