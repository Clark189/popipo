from pygame import *
from GameSprite import *
from Player import *
from Enemy import *

def main():
    mixer.init()
    mixer.music.load('space.ogg')
    mixer.music.play()
    fire_sound = mixer.Sound('fire.ogg')

    font.init()
    font1 = font.Font(None, 35)

    win = font1.render('CONGRAT!', True, (255, 255, 255))
    lose = font1.render('WASTED', True, (180, 0, 0))

    img_back = 'galaxy.jpg'
    img_ship = 'rocket.png'
    img_enemy = 'ufo.png'
    img_aster = 'asteroid.png'

    win_width = 1200
    win_height = 900
    display.set_caption("Shooter")
    window = display.set_mode((win_width, win_height))
    background = transform.scale(image.load(img_back), (win_width, win_height))

    ship = Player(img_ship, 5, win_height - 100, 80, 100, 10,  win_width, win_height, window)
    monster = sprite.Group()
    for i in range(1, 6):
        monster = Enemy( img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5), win_width, win_height, window)
        monster.add(monster)
    
    aster = sprite.Group()
    for i in range(1, 6):
        aster = Enemy(img_aster, randint(80, win_width - 80), -40, 80, 50, randint(1, 5), win_width, win_height, window)
        aster.add(aster)

    


bullets = sprite.Group()
clock = time.Clock()
lost = 0
score = 0
finish = False
run = True

old_time = 0
new_time = 0

if bullets <= 0:
    old_time = 0
    if old_time - new_time >= 1:
        bullets = 15

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                bullets.add(ship.fire())

    if not finish:
        window.blit(background, (0, 0))
        lost_text = font1.render('Lost: ' +str(lost), True, (255, 255, 255))
        window.blit(lost_text, (10, 10))
        score_text = font1.render('Score: ' +str(score), True, (255, 255, 255))
        window.blit(score_text, (10, 40))
        ship.update()
        bullets.update()

        for m in monster:
            print(lost)
            lost += m.update()

        collides = sprite.groupcollide(monster, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5), win_width, win_height, window)
            monster.add(monster)

        for a in aster:
            print(lost)
            lost += a.update()

        collides = sprite.groupcollide(aster, True, True)
        for c in collides:
            score = score + 1
            aster = Enemy(img_aster, randint(80, win_width - 80), -40, 80, 50, randint(1, 5), win_width, win_height, window)
            aster.add(aster)
        
        if sprite.groupcollide(ship, monster, aster, False) or lost >= 5:
            finish = True
            window.blit(lose, (200, 200))

        if score >= 10:
            win = True
            window.blit(win, (200, 200))

        ship.reset()
        monster.draw()
        aster.draw()
        bullets.draw()

        display.update()
    clock.tick(60)

if __name__ == '__main__':
    main()