import pygame
from Game_1.Player import Player
from Game_1.Projectiles import Bullet
from Game_1.Colours import *


def main():
    size = (500, 500)
    win = pygame.display.set_mode(size)
    pygame.display.set_caption("Game 1 !")

    clock = pygame.time.Clock()

    player = Player(400, 400, 40, 40, GREEN, 5, win)
    bullets = []

    run = True
    while run:
        clock.tick(60)  # Set FPS of 60

        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if len(bullets) < 5:
                        bullets.append(
                            Bullet(player.x + (player.wid * 0.25), player.y + (player.height * 0.25), player, win))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            player.goLeft()
        if keys[pygame.K_d]:
            player.goRight()
        if keys[pygame.K_SPACE]:
            player.isJumping = True

        if player.isJumping:
            player.doJump()

        win.fill(WHITE)

        for bullet in bullets:
            if 500 > bullet.x > 0:
                bullet.move()
            else:
                bullets.remove(bullet)

        player.registerChange()
        # pygame.display.update()


if __name__ == "__main__":
    main()
