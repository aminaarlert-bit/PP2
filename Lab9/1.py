import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()

# Настройка экрана
screen_height = 600
screen_width = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Road Game")

# Звук и музыка
pygame.mixer.music.load("background.wav")
pygame.mixer.music.set_volume(0.3)      
pygame.mixer.music.play(-1)

# Загрузка ресурсов
background = pygame.image.load("AnimatedStreet.png")
player_image = pygame.image.load("Player.png")
enemy_image = pygame.image.load("Enemy.png")
# Для разных весов нужны разные изображения или способ их отличить
# Для простоты, оставим одно изображение, но добавим разные веса.
coin_image = pygame.image.load("Coin.png") 
crash_sound = pygame.mixer.Sound("crash.wav")
coin_sound = pygame.mixer.Sound("bell.wav")

# Шрифты
big_font = pygame.font.SysFont("Verdana", 60)
small_font = pygame.font.SysFont("Verdana", 20)

# Глобальные переменные для счета и скорости
score = 0
coin_score = 0 # Общее количество набранных очков монетами
coins_for_speed_boost = 0 # ***Ключевое изменение 2: Счетчик для увеличения скорости***
N_SPEED_THRESHOLD = 5 # ***Ключевое изменение 2: Увеличение скорости каждые N_SPEED_THRESHOLD очков***

clock = pygame.time.Clock()
game_over_text = big_font.render("Game Over", True, (0, 0, 0))
speed = 10


# Класс Игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 80)

    def update(self):
        # Обработка ввода для перемещения
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += 5


# Класс Врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.reset_position()

    def reset_position(self):
        # Случайное появление выше экрана
        self.rect.center = (random.randint(40, screen_width - 40), -random.randint(100, 300))

    def update(self):
        global score
        # Движение вниз со скоростью 'speed'
        self.rect.y += speed
        # Сброс позиции, если выехал за экран
        if self.rect.top > screen_height:
            self.reset_position()
            score += 1 # Увеличение счета за пропущенного врага


# Класс Монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.rect = self.image.get_rect()
        self.weight = 1 # Изначальный вес
        self.reset_position()

    def reset_position(self):
        # ***Ключевое изменение 1: Случайный вес для монеты***
        # Монеты могут давать 1, 2 или 3 очка
        self.weight = random.choice([1, 2, 3]) 
        # Если бы были разные изображения, тут бы меняли self.image в зависимости от self.weight
        
        # Случайное появление выше экрана
        self.rect.center = (random.randint(40, screen_width - 40), -random.randint(200, 600))

    def update(self):
        # Движение вниз со скоростью 'speed'
        self.rect.y += speed
        # Сброс позиции, если выехал за экран
        if self.rect.top > screen_height:
            self.reset_position()

    def collect(self):
        global coin_score
        global coins_for_speed_boost
        
        # ***Ключевое изменение 1: Добавление веса монеты к счету***
        coin_score += self.weight 
        
        # ***Ключевое изменение 2: Добавление веса к счетчику скорости***
        coins_for_speed_boost += self.weight
        
        self.reset_position()


player = Player()
enemy = Enemy()
coin = Coin()

enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)

# ***Удаляем старый таймер для скорости, теперь скорость зависит от монет***
# INCREASE_SPEED_EVENT = pygame.USEREVENT + 1
# pygame.time.set_timer(INCREASE_SPEED_EVENT, 10000)

running = True
while running:
    # Отрисовка фона
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # ***Удалена обработка события INCREASE_SPEED_EVENT***
        # if event.type == INCREASE_SPEED_EVENT:
        #    speed += 1

    # Обновление позиций
    player.update()
    enemies.update()
    coins.update()

    # Отрисовка спрайтов
    screen.blit(player.image, player.rect)
    enemies.draw(screen)
    coins.draw(screen)

    # Отрисовка счета
    score_text = small_font.render(f"Score: {score}", True, (0, 0, 0))
    coin_text = small_font.render(f"Coins: {coin_score}", True, (0, 0, 0)) # Теперь отображает общее количество очков
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (screen_width - 100, 10))

    # ***Проверка на столкновение с монетой***
    if pygame.sprite.spritecollideany(player, coins):
        coin_sound.play()
        coin.collect()
        
        # ***Ключевое изменение 2: Проверка на увеличение скорости***
        if coins_for_speed_boost >= N_SPEED_THRESHOLD:
            speed += 1  # Увеличение скорости врагов
            coins_for_speed_boost = 0 # Сброс счетчика для следующего ускорения

    # ***Проверка на столкновение с врагом (Game Over)***
    if pygame.sprite.spritecollideany(player, enemies):
        crash_sound.play()
        time.sleep(0.5)
        # Экран Game Over
        screen.fill((255, 0, 0))
        screen.blit(game_over_text, (30, 250))
        pygame.display.update()
        time.sleep(2)
        running = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()