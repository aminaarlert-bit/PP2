import pygame
import random
import psycopg2
from color_palette import * # Импорт цветовой палитры (предполагается, что это ваш файл)

# (PostgreSQL)\

def init_db():
    """
    Инициализирует базу данных: устанавливает соединение, удаляет старые таблицы
    (для чистого старта) и создает новые таблицы: snake_users и snake_scores.
    """
    # Установление соединения с БД
    conn = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='amina007',
        host='localhost',
        port='5432'
    )
    cur = conn.cursor()
    
    # Удаление таблиц, если они существуют. CASCADE удаляет связанные записи.
    cur.execute("DROP TABLE IF EXISTS snake_scores CASCADE")
    cur.execute("DROP TABLE IF EXISTS snake_users CASCADE")
    
    # Создание таблицы пользователей (snake_users)
    cur.execute("""
    CREATE TABLE snake_users (
        user_id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL, -- Имя пользователя должно быть уникальным
        high_score INTEGER DEFAULT 0,         -- Лучший счет пользователя
        current_level INTEGER DEFAULT 1,      -- Уровень, с которого пользователь начнет игру
        last_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Время последнего входа
    )""")
    
    # Создание таблицы результатов/сохранений (snake_scores)
    cur.execute("""
    CREATE TABLE snake_scores (
        score_id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES snake_users(user_id), -- Ссылка на пользователя
        score INTEGER NOT NULL,
        level INTEGER NOT NULL,
        game_data TEXT, -- Строка для хранения состояния змейки (для сохранения/загрузки)
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    
    conn.commit() # Фиксация изменений в БД
    cur.close()
    conn.close()

def get_db_connection():
    """
    Вспомогательная функция для получения нового соединения с БД.
    """
    return psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='amina007',
        host='localhost',
        port='5432'
    )


def get_or_create_user(username):
    """
    Ищет пользователя по имени. Если находит, возвращает его ID и текущий уровень.
    Если не находит, создает нового пользователя.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # 1. Поиск существующего пользователя
        cur.execute("""
        SELECT user_id, current_level, high_score 
        FROM snake_users 
        WHERE username = %s
        """, (username,))
        user = cur.fetchone()
        
        if user:
            # Пользователь найден
            user_id, level, high_score = user
            print(f"Welcome back, {username}! Level: {level}, High Score: {high_score}")
        else:
            # Пользователь не найден, создаем нового
            cur.execute("""
            INSERT INTO snake_users (username) 
            VALUES (%s) 
            RETURNING user_id, current_level, high_score -- Возвращаем созданные значения
            """, (username,))
            user_id, level, high_score = cur.fetchone()
            print(f"New user created! Starting at level {level}")
        
        # Обновляем время последнего входа
        cur.execute("""
        UPDATE snake_users 
        SET last_played = CURRENT_TIMESTAMP 
        WHERE user_id = %s
        """, (user_id,))
        
        conn.commit()
        return user_id, level
        
    except Exception as e:
        # Обработка ошибок БД
        print(f"Database error: {e}")
        conn.rollback() # Откат транзакции при ошибке
        return None, 1  # Возвращаем None ID и уровень 1 по умолчанию
        
    finally:
        cur.close()
        conn.close()

def save_game_state(user_id, score, level, snake_body):
    """
    Сохраняет текущий счет и состояние игры в таблицу snake_scores.
    Обновляет рекорд пользователя в таблице snake_users.
    """
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        # Формирование строки данных для сохранения состояния змейки (game_data)
        # Формат: 'score,level,x1,y1;x2,y2;...'
        # Преобразуем список объектов Point в строку координат
        game_data = f"{score},{level},{';'.join(f'{p.x},{p.y}' for p in snake_body)}"
        
        # 1. Вставка текущего состояния игры в таблицу сохранений
        cur.execute("""
        INSERT INTO snake_scores (user_id, score, level, game_data) 
        VALUES (%s, %s, %s, %s)
        """, (user_id, score, level, game_data))
        
        # 2. Обновление high_score (наивысшего счета) пользователя
        cur.execute("""
        UPDATE snake_users 
        SET high_score = GREATEST(high_score, %s), -- GREATEST выбирает максимальное значение
            current_level = %s # Сохраняем текущий уровень
        WHERE user_id = %s
        """, (score, level, user_id))
        
        conn.commit()
    except Exception as e:
        print(f"Error saving game: {e}")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

# --- ИНИЦИАЛИЗАЦИЯ ПОЛЬЗОВАТЕЛЯ И ЗАПУСК БД ---

# Инициализируем БД (создаем/пересоздаем таблицы)
init_db()

# Запрашиваем имя пользователя перед началом игры
username = input("Enter your username: ")
# Получаем ID пользователя и его стартовый уровень
user_id, current_level = get_or_create_user(username)

# Обработка ошибки: если не удалось получить ID, используем уровень 1
if user_id is None:
    print("Using default values due to error")
    current_level = 1

# --- НАСТРОЙКИ PYGAME И ИГРОВЫХ ПАРАМЕТРОВ ---

pygame.init()
WIDTH, HEIGHT = 600, 600 # Размеры игрового окна
CELL = 30 # Размер одной клетки (сегмента змейки)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 20)

# Словарь с конфигурацией уровней (скорость, стены)
LEVELS = {
    1: {'speed': 7, 'walls': []}, # Уровень 1: Скорость 7, стен нет
    2: {'speed': 10, 'walls': [[100,100,200,20], [400,300,200,20]]}, # Уровень 2: Скорость 10, две стены
    3: {'speed': 13, 'walls': [[50,50,20,300], [300,150,300,20], [200,350,200,20]]} # Уровень 3: Скорость 13, больше стен
}

# --- КЛАССЫ ИГРОВЫХ ОБЪЕКТОВ ---

class Point:
    """Простой класс для хранения координат (x, y) на сетке."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Wall:
    """Класс стены (препятствия)."""
    def __init__(self, x, y, width, height):
        # Создаем прямоугольник Pygame, который используется для отрисовки и коллизии
        self.rect = pygame.Rect(x, y, width, height) 
    
    def draw(self):
        pygame.draw.rect(screen, colorBLUE, self.rect)

class Snake:
    """Класс Змейки."""
    def __init__(self):
        self.reset()
    
    def reset(self):
        """Сброс состояния змейки (начальное положение, счет, уровень)."""
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)] # Начальное тело змейки
        self.dx = 1 # Начальное направление движения по X
        self.dy = 0 # Начальное направление движения по Y
        self.score = 0
        self.level = current_level # Уровень берется из БД
    
    def move(self):
        """Передвижение змейки."""
        # Передвигаем все сегменты тела на позицию предыдущего сегмента
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        # Передвигаем голову в новом направлении
        self.body[0].x += self.dx
        self.body[0].y += self.dy
    
    def draw(self):
        """Отрисовка змейки."""
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW # Голова красная, тело желтое
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))
    
    def check_collision(self, food):
        """Проверка столкновения с едой."""
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.body.append(Point(head.x, head.y)) # Добавляем сегмент
            self.score += food.weight             # Увеличиваем счет
            
            # Проверка повышения уровня
            if self.score >= self.level * 10:  # Повышение уровня каждые 10 очков
                self.level = min(self.level + 1, 3) # Максимальный уровень - 3
            return True
        return False
    
    def check_wall_collision(self, walls):
        """Проверка столкновения со стенами, границами и самой собой."""
        head = self.body[0]
        # Коллизия с границами экрана
        if head.x < 0 or head.x >= WIDTH//CELL or head.y < 0 or head.y >= HEIGHT//CELL:
            return True
        
        # Коллизия с объектами Wall
        head_rect = pygame.Rect(head.x * CELL, head.y * CELL, CELL, CELL)
        for wall in walls:
            if head_rect.colliderect(wall.rect):
                return True
        
        # Коллизия с собственным телом
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

class Food:
    """Класс Еды."""
    def __init__(self):
        self.pos = Point(9, 9)
        self.weight = random.randint(1, 3) # Еда может давать разное количество очков
        self.color = colorGREEN if self.weight == 1 else (colorBLUE if self.weight == 2 else colorPURPLE)
    
    def generate(self, snake, walls):
        """Генерация новой позиции для еды, исключая змейку и стены."""
        while True:
            x = random.randint(0, WIDTH//CELL - 1)
            y = random.randint(0, HEIGHT//CELL - 1)
            
            valid = True
            # Проверка коллизии с телом змейки
            for segment in snake.body:
                if x == segment.x and y == segment.y:
                    valid = False
                    break
            
            if valid:
                # Проверка коллизии со стенами
                food_rect = pygame.Rect(x * CELL, y * CELL, CELL, CELL)
                for wall in walls:
                    if food_rect.colliderect(wall.rect):
                        valid = False
                        break
            
            if valid:
                self.pos = Point(x, y)
                self.weight = random.randint(1, 3)
                self.color = colorGREEN if self.weight == 1 else (colorBLUE if self.weight == 2 else colorPURPLE)
                break
    
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def draw_grid():
    """Отрисовка шахматной сетки."""
    colors = [colorWHITE, colorGRAY]
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# --- ИГРОВОЙ ЦИКЛ ---

# Создание игровых объектов
snake = Snake()
food = Food()
# Создание объектов стен для начального уровня
walls = [Wall(*wall) for wall in LEVELS[snake.level]['walls']] 
food.generate(snake, walls)

# Состояние игры
running = True
game_over = False
paused = False
FPS = LEVELS[snake.level]['speed'] # Начальная скорость берется из настроек уровня

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Горячая клавиша P для паузы и сохранения
                paused = not paused
                if paused:
                    # Сохраняем состояние игры в БД при постановке на паузу
                    save_game_state(user_id, snake.score, snake.level, snake.body)
            
            if not paused and not game_over:
                # Управление змейкой, предотвращая движение назад
                if event.key == pygame.K_RIGHT and snake.dx != -1:
                    snake.dx = 1; snake.dy = 0
                elif event.key == pygame.K_LEFT and snake.dx != 1:
                    snake.dx = -1; snake.dy = 0
                elif event.key == pygame.K_DOWN and snake.dy != -1:
                    snake.dx = 0; snake.dy = 1
                elif event.key == pygame.K_UP and snake.dy != 1:
                    snake.dx = 0; snake.dy = -1
    
    if not game_over and not paused:
        snake.move()
        
        # Проверка коллизий
        if snake.check_wall_collision(walls):
            game_over = True
            # Сохраняем финальный счет и состояние при проигрыше
            save_game_state(user_id, snake.score, snake.level, snake.body)
        
        if snake.check_collision(food):
            food.generate(snake, walls)
        
        # Обновление уровня, если счет достиг нужного порога
        if snake.level != current_level:
            current_level = snake.level
            # Перезагрузка стен и скорости для нового уровня
            walls = [Wall(*wall) for wall in LEVELS[snake.level]['walls']]
            FPS = LEVELS[snake.level]['speed']
    
    # --- Отрисовка ---
    screen.fill(colorBLACK)
    draw_grid()
    
    # Отрисовка стен
    for wall in walls:
        wall.draw()
    
    snake.draw()
    food.draw()
    
    # Отображение счета и уровня
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    # Отображение сообщения о паузе
    if paused:
        pause_text = font.render("PAUSED (Press P to resume)", True, colorRED)
        screen.blit(pause_text, (WIDTH//2 - 150, HEIGHT//2))
    
    # Отображение сообщения о проигрыше
    if game_over:
        game_over_text = font.render("GAME OVER - Press R to restart", True, colorRED)
        screen.blit(game_over_text, (WIDTH//2 - 150, HEIGHT//2))
        
        # Обработка перезапуска игры
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            # Сброс игры и повторная инициализация стен/еды
            snake.reset()
            walls = [Wall(*wall) for wall in LEVELS[snake.level]['walls']]
            food.generate(snake, walls)
            game_over = False
    
    pygame.display.flip() # Обновление экрана
    clock.tick(FPS) # Ограничение частоты кадров (скорости игры)

pygame.quit()