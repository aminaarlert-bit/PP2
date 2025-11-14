import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()

screen_height = 600
screen_width = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Road Game")

pygame.mixer.music.load("background.wav")
pygame.mixer.music.set_volume(0.3)        
pygame.mixer.music.play(-1)

background = pygame.image.load("AnimatedStreet.png")
player_image = pygame.image.load("Player.png")
enemy_image = pygame.image.load("Enemy.png")
coin_image = pygame.image.load("Coin.png")
crash_sound = pygame.mixer.Sound("crash.wav")
coin_sound = pygame.mixer.Sound("bell.wav")

big_font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 20)

score = 0
coin_score = 0

clock = pygame.time.Clock()
game_over_text = big_font.render("Game Over", True, (0, 0, 0))
speed = 10


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 80)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += 5


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(40, screen_width - 40), -random.randint(100, 300))

    def update(self):
        global score
        self.rect.y += speed
        if self.rect.top > screen_height:
            self.reset_position()
            score += 1


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        self.rect.center = (random.randint(40, screen_width - 40), -random.randint(200, 600))

    def update(self):
        self.rect.y += speed
        if self.rect.top > screen_height:
            self.reset_position()

    def collect(self):
        global coin_score
        coin_score += 1
        self.reset_position()


player = Player()
enemy = Enemy()
coin = Coin()

enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)

INCREASE_SPEED_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(INCREASE_SPEED_EVENT, 10000)

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == INCREASE_SPEED_EVENT:
            speed += 1

    player.update()
    enemies.update()
    coins.update()

    screen.blit(player.image, player.rect)
    enemies.draw(screen)
    coins.draw(screen)

    score_text = small_font.render(f"Score: {score}", True, (0, 0, 0))
    coin_text = small_font.render(f"Coins: {coin_score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (screen_width - 100, 10))

    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound.play()
        time.sleep(0.5)
        screen.fill((255, 0, 0))
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()
        time.sleep(2)
        running = False

    if pygame.sprite.spritecollideany(player, coins):
        coin_sound.play()
        coin.collect()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()