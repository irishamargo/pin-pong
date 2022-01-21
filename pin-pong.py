from pygame import *

#создай окно игры
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Пин-понг')

#задай фон сцены
background = transform.scale(image.load('fon.jpg'), (win_width, win_height))

#создание класса
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

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_height-110:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_height-110:
            self.rect.y += self.speed

#игроки
player1 = Player('roc.png', win_width - 80, win_height/2-20, 50, 100, 9)
player2 = Player('roc.png', 30, win_height/2-20, 50, 100, 9)

clock = time.Clock()
FPS = 60

run = True
finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
    
    if finish != True:
        window.blit(background, (0, 0))

        player1.update1()
        player2.update2()
        
        player1.reset()
        player2.reset()

    display.update()
    clock.tick(FPS)