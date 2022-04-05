from ast import Del
import pygame

class Player(pygame.Rect):
    def __init__(self, posx, posy):
        self.x = posx
        self.y = posy
        self.rect = pygame.Rect(self.x, self.y, 20, 100)
        self.pos_y = self.rect.y
        self.speed = 150
        self.move_up = False
        self.move_down = False

    def update(self, dt):
        # Cima
        if self.move_up:
            self.pos_y -= self.speed * dt
            self.rect.y = self.pos_y

        # Baixo
        if self.move_down:
            self.pos_y += self.speed * dt
            self.rect.y = self.pos_y


    def render(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

# p1_pos_y = player1.rect.y
# p1_speed = 150

# p1_pos_y += p1_speed * dt
# player1.rect.y = p1_pos_y
