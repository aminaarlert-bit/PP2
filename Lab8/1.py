import pygame
import random
import time
import os

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCORE = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

image_background = pygame.image.load('AnimatedStreet.png')
image_player = pygame.image.load('Player.png')
image_enemy = pygame.image.load('Enemy.png')
image_coin = pygame.image.load("Coin.png")

pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound('crash.wav')
sound_coin = pygame.mixer.Sound('coin_hit.wav')

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

image_game_over = font.render("Game Over", True, "black")
image_game_over_rect = image_game_over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT
        self.speed = 3

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 7
        self.generate_random_rect()
        
    def generate_random_rect(self):
        self.rect.left = random.randint(0, SCREEN_WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.generate_random_rect()

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(image_coin, (30, 30))
        self.rect = self.image.get_rect()
        self.generate_random_position()

    def generate_random_position(self):
        self.rect.left = random.randint(50, SCREEN_WIDTH - 50)
        self.rect.top = random.randint(100, SCREEN_HEIGHT - 200)

    def move(self):
        pass

clock = pygame.time.Clock()
FPS = 60

P1 = Player()
E1 = Enemy()
C1 = Coin()

all_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()
coin_sprites = pygame.sprite.Group()

all_sprites.add(P1, E1, C1)
enemy_sprites.add(E1)
coin_sprites.add(C1)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    P1.move()

    screen.blit(image_background, (0, 0))
    coin_text = font_small.render(f"Coins: {SCORE}", True, "black")
    screen.blit(coin_text, (SCREEN_WIDTH - coin_text.get_width() - 10, 10))

    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, coin_sprites):
        sound_coin.play()
        SCORE += 1
        C1.generate_random_position()

    if pygame.sprite.spritecollideany(P1, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        screen.fill("red")
        screen.blit(image_game_over, image_game_over_rect)
        pygame.display.flip()
        time.sleep(2)
        running = False
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
