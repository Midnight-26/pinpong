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

ball = GameSprite("ball.png",W//2, H-80, 80, 80, 10)
ping_pong = GameSprite("ping_pong.png",W//3, H-90, 80, 110, 10)
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    ball.reset()
    ping_pong.reset()
    display.update()
    clock.tick(FPS)

