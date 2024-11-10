import math
import pygame

# Инициализация Pygame и создание экрана
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((618, 358))
icon = pygame.image.load("icons/icon.png")
pygame.display.set_caption("platformer atom 1")
pygame.display.set_icon(icon)
bg_color = (24, 199, 222)
running = True
font = pygame.font.Font("PixelifySans-Regular.ttf", 20)

# Создаем спрайты платформ
plat1_img = pygame.image.load("icons/plat1.png")
plat2_img = pygame.image.load("icons/plat2.png")

class Platform(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

# Создаем платформы
plat1 = Platform(plat1_img, 100, 250)
plat2 = Platform(plat2_img, 300, 200)
plat3 = Platform(plat1_img, 400, 150)
plat4 = Platform(plat2_img, 200, 100)
plat5 = Platform(plat1_img, 500, 250)

# Группируем платформы
platforms = pygame.sprite.Group()
platforms.add(plat1, plat2, plat3, plat4, plat5)

# Класс камеры
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.camera_rect = pygame.Rect(0, 0, width, height)
        self.camera_speed = 0.5

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(screen.get_width() / 2)
        y = -target.rect.centery + int(screen.get_height() / 2)

        self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)

# Класс солнца
class Sun(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("icons/sun.png")
        self.rect = self.image.get_rect(topleft=(x, y))

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.player_left = [
            pygame.image.load("icons/player left/left1.png"),
            pygame.image.load("icons/player left/left2.png"),
            pygame.image.load("icons/player left/left3.png"),
            pygame.image.load("icons/player left/left4.png")]
        self.player_right = [
            pygame.image.load("icons/player right/right1.png"),
            pygame.image.load("icons/player right/right2.png"),
            pygame.image.load("icons/player right/right3.png"),
            pygame.image.load("icons/player right/right4.png")]
        self.image = self.player_right[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = 618 / 2
        self.rect.bottom = 0
        self.player_anim_count = 0
        self.player_speed = 5
        self.speed_y = 0
        self.jump_boost = 15
        self.player_walk = ""
        self.gravity_strength = 0.5
        self.speed_x = 0
        self.on_ground = False

    def update(self):
        self.rect.x += self.speed_x
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player_walk = "left"
            self.speed_x = -self.player_speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player_walk = "right"
            self.speed_x = self.player_speed
        else:
            self.speed_x = 0

        if self.player_walk == "right":
            self.image = self.player_right[math.floor(self.player_anim_count)]
        elif self.player_walk == "left":
            self.image = self.player_left[math.floor(self.player_anim_count)]
        else:
            if self.player_walk == "left2":
                self.image = self.player_left[0]
            else:
                self.image = self.player_right[0]

        if self.player_anim_count >= 3:
            self.player_anim_count = 0
        else:
            self.player_anim_count += 0.5

# Проверка коллизии с платформами
def check_collisions(player, platforms):
    player.on_ground = False
    for platform in platforms:
        # Проверка коллизии по вертикали
        if player.rect.colliderect(platform.rect):
            # Игрок сверху платформы
            if player.speed_y > 0 and player.rect.bottom <= platform.rect.top + 10:
                player.rect.bottom = platform.rect.top
                player.speed_y = 0
                player.on_ground = True
            # Игрок снизу платформы (ударяется головой)
            elif player.speed_y < 0 and player.rect.top >= platform.rect.bottom - 10:
                player.rect.top = platform.rect.bottom
                player.speed_y = 0
            # Проверка коллизии по горизонтали
            if player.rect.right > platform.rect.left and player.rect.left < platform.rect.left:
                player.rect.right = platform.rect.left
                player.speed_x /= 2  # Замедление при касании боковой стороны
            elif player.rect.left < platform.rect.right and player.rect.right > platform.rect.right:
                player.rect.left = platform.rect.right
                player.speed_x /= 2  # Замедление при касании боковой стороны

# Создаем игрока
player = Player()

# Создаем объект солнца
sun = Sun(500, 50)  # Позиция солнца (x, y)

# Создаем объект камеры
camera = Camera(1000, 1000)  # Задайте размеры камеры, соответствующие вашему миру

while running:
    # Обновляем дисплей
    clock.tick(30)
    pygame.display.flip()
    screen.fill(bg_color)

    # Применение гравитации к игроку
    player.speed_y += player.gravity_strength
    if not player.on_ground:
        player.rect.y += player.speed_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_w]:
        if player.on_ground:
            player.speed_y = -player.jump_boost

    # Проверка коллизии
    check_collisions(player, platforms)

    # Остановка игры, если игрок падает слишком низко
    if player.rect.y > 350:
        running = False
        pygame.quit()
        exit(0)

    # Обновление и отрисовка игрока и платформ
    player.update()
    camera.update(player)  # Обновляем позицию камеры

    # Отображаем платформы и игрока
    for plat in platforms:
        screen.blit(plat.image, camera.apply(plat))

    screen.blit(player.image, camera.apply(player))

    # Отображаем солнце
    screen.blit(sun.image, sun.rect.topleft)

    # Отображение FPS
    screen.blit(font.render("fps : " + str(math.floor(clock.get_fps())), 1, (255, 255, 255)), (50, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit(0)

    pygame.display.update()