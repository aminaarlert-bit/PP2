import pygame 
import sys 
import copy 
import random 
import time 

# Инициализация Pygame
pygame.init() 

# --- Глобальные Настройки Игры ---
scale = 15          # Размер одного сегмента змейки/еды (в пикселях)
score = 0         # Текущий счет игрока
level = 0         # Текущий уровень игры
SPEED = 10          # Скорость игры (кадры в секунду)

food_x = 10         # Начальная X-координата еды
food_y = 10         # Начальная Y-координата еды

# --- Настройки Таймера Еды и Веса ---
FOOD_TIMER_MAX = 7000  # ***ИЗМЕНЕНО: 7000 миллисекунд = 7 секунд***
food_timer = FOOD_TIMER_MAX # Текущий таймер еды
food_weight = 1     # Вес текущей еды (на сколько увеличится счет)
last_time = pygame.time.get_ticks() # Время последнего обновления для таймера

# Создание игрового окна
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game") 
clock = pygame.time.Clock() 

# --- Определение Цветов (в формате RGB) ---
background_top = (0, 0, 50) 
background_bottom = (0, 0, 0) 
snake_colour = (255, 137, 0) 
food_colour = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)) # Случайный цвет еды
snake_head = (255, 247, 0) 
font_colour = (255, 255, 255) 
defeat_colour = (255, 0, 0) 

# --- Определение Класса Snake ---
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 15
        self.h = 15
        self.x_dir = 1  # Направление движения по X
        self.y_dir = 0  # Направление движения по Y
        self.history = [[self.x, self.y]] # Список координат сегментов змейки
        self.length = 1 
        
    def reset(self):
        # Сброс змейки в начальное состояние
        self.x = 500 / 2 - scale
        self.y = 500 / 2 - scale
        self.w = 15
        self.h = 15
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):
        # Отображение змейки
        for i in range(self.length):
            if not i == 0:
                # Тело змейки
                pygame.draw.rect(display, snake_colour, (self.history[i][0], self.history[i][1], self.w, self.h))
            else:
                # Голова змейки
                pygame.draw.rect(display, snake_head, (self.history[i][0], self.history[i][1], self.w, self.h))

    def check_eaten(self):
        # Проверка столкновения головы змейки с едой
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True

    def check_level(self):
        # Проверка, достигнут ли порог для повышения уровня (каждые 5 сегментов)
        global level
        if self.length % 5 == 0 and self.length > 1:
            return True

    def grow(self):
        # Увеличение длины змейки
        self.length += 1
        # Добавление нового сегмента в конец (копируем предпоследний)
        self.history.append(self.history[self.length - 2])

    def death(self):
        # Проверка столкновения головы змейки с телом
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1

    def update(self):
        # Обновление позиций сегментов змейки
        i = self.length - 1
        while i > 0:
            # Сдвиг всех сегментов на позицию предыдущего
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        # Перемещение головы в новом направлении
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

# --- Определение Класса Food ---
class Food:
    def new_location(self):
        # Генерация новой случайной локации для еды
        global food_x, food_y, food_weight, food_timer, food_colour, last_time
        
        food_x = random.randrange(1, int(500 / scale) - 1) * scale
        food_y = random.randrange(1, int(500 / scale) - 1) * scale
        
        # Случайное генерирование веса еды (1-5 очков)
        food_weight = random.randint(1, 5) 
        
        # Сброс таймера еды
        food_timer = FOOD_TIMER_MAX
        last_time = pygame.time.get_ticks()

        # Случайный цвет еды
        food_colour = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


    def show(self):
        # Отображение еды (рисуется только если таймер не истёк)
        if food_timer > 0:
             pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))

# --- Вспомогательные Функции Отображения ---

# Функция для отображения счета игрока
def show_score():
    font = pygame.font.SysFont(None, 20)
    # Добавление веса еды в отображение для информации
    text = font.render(f"Score: {score} (Next Food Weight: {food_weight})", True, font_colour)
    display.blit(text, (scale, scale))

# Функция для отображения игрового уровня
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, font_colour)
    display.blit(text, (300 - scale, scale)) # Скорректировано местоположение для лучшего выравнивания

# Функция для отображения оставшегося времени до исчезновения еды
def show_food_timer():
    global food_timer
    if food_timer > 0:
        font = pygame.font.SysFont(None, 20)
        # Цвет таймера становится краснее, когда время истекает
        color = (255, 255 * (food_timer / FOOD_TIMER_MAX), 255 * (food_timer / FOOD_TIMER_MAX))
        text = font.render(f"Time: {food_timer / 1000:.1f}s", True, color)
        display.blit(text, (400 - scale, scale))

# --- Основной Игровой Цикл ---
def gameLoop():
    global score
    global level
    global SPEED
    global food_timer
    global food_weight
    global last_time

    snake = Snake(500 / 2, 500 / 2)
    food = Food()
    food.new_location()

    while True:
        # Обновление таймера еды
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_time
        last_time = current_time
        
        if food_timer > 0:
            food_timer -= delta_time
        else:
            # Если таймер истек, еда исчезает и появляется в новой локации
            food.new_location()


        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                # Управление змейкой (запрет движения в обратном направлении)
                if snake.y_dir == 0: # Если движется по горизонтали
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1
                if snake.x_dir == 0: # Если движется по вертикали
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0

        # Фон (градиент)
        for y in range(500):
            color = (
                background_top[0] + (background_bottom[0] - background_top[0]) * y / 500,
                background_top[1] + (background_bottom[1] - background_top[1]) * y / 500,
                background_top[2] + (background_bottom[2] - background_top[2]) * y / 500
            )
            pygame.draw.line(display, color, (0, y), (500, y))

        # Отображение элементов
        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()
        show_food_timer() # Отображение таймера

        # Проверка на поедание еды
        if food_timer > 0 and snake.check_eaten():
            # Счет увеличивается на вес еды
            score += food_weight
            snake.grow()
            food.new_location() # Генерируем новую еду

        # Проверка на повышение уровня
        if snake.check_level():
            # Если уровень повышен, даем бонусное очко длины и ускоряем игру
            food.new_location() 
            level += 1
            SPEED += 1
            snake.grow()

        # Проверка на столкновение с собой
        if snake.death():
            score = 0
            level = 0
            SPEED = 10 # Сброс скорости
            
            # Экран "Game Over"
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, defeat_colour)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)
            
            snake.reset()
            food.new_location() # Сброс еды

        # Проверка границ (стен) и перенос змейки на противоположную сторону
        if snake.history[0][0] >= 500: 
            snake.history[0][0] = 0 
        
        if snake.history[0][0] < 0: 
            snake.history[0][0] = 500 
            
        if snake.history[0][1] >= 500:
            snake.history[0][1] = 0
            
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500

        # Обновление экрана и ограничение скорости
        pygame.display.update()
        clock.tick(SPEED)

gameLoop()