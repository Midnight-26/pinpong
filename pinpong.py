from pygame import *

# создание и установка окна
W = 700
H = 500
window = display.set_mode((W, H))
display.set_caption('Пинг понг')
background = (114, 185, 247)
window.fill(background)
            
clock = time.Clock()
FPS = 60

# Классы 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < H - 100:
            self.rect.y += self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < H - 100:
            self.rect.y += self.speed

ball = GameSprite("ball.png",W//2, H-80, 80, 80, 10)
ping_pong = Player("ping_pong.png", 30, H//2, 80, 110, 10)
ping_pong2 = Player("ping_pong2.png", W-120, H//2, 80, 110, 10)

speed_x = 5
speed_y = 5

# font.init()
# font = font.Font(None, 35)
# lose1 = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
# lose2 = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
# restart_game

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(background)

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        ping_pong.update_l()
        ping_pong2.update_r()

        ping_pong.reset()
        ping_pong2.reset()
        ball.reset()

        if ball.rect.y > H-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(ping_pong, ball) or sprite.collide_rect(ping_pong2, ball):
            speed_x *= -1
            speed_y *= 1

        display.update()

        ball.reset()
        ping_pong.reset()
        ping_pong.update_l()
        display.update()
        clock.tick(FPS)

