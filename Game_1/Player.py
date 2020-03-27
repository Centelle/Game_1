import pygame


class Player:
    def __init__(self, x, y, wid, height, colour, vel, win):
        self.x = x
        self.y = y
        self.wid = wid
        self.height = height
        self.colour = colour
        self.vel = vel
        self.win = win
        self.facingRight = False
        self.facingLeft = True  # Default value facing left
        self.isJumping = False
        self.jumpVal = 20
        self.jumpCount = self.jumpVal

    def draw(self):
        pygame.draw.rect(self.win, self.colour, (self.x, self.y, self.wid, self.height))
        pygame.display.update()

    def goUp(self):
        self.y -= self.vel

    def goDown(self):
        self.y += self.vel

    def goLeft(self):
        if self.x - self.vel > 0:
            self.x -= self.vel
            self.facingLeft = True
            self.facingRight = False

    def doJump(self):
        if self.jumpCount >= -self.jumpVal:
            amp = 1 if self.jumpCount > 0 else -1
            self.y -= (self.jumpCount ** 2) * 0.075 * amp
            self.jumpCount -= 1
        else:
            self.isJumping = False
            self.jumpCount = self.jumpVal

    def goRight(self):
        if self.x + self.wid + self.vel < 500:
            self.x += self.vel
            self.facingLeft = False
            self.facingRight = True

    def registerChange(self):
        self.draw()
