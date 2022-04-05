import pygame, sys, time
from players import Player

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ball = pygame.Rect(400, 300, 30, 30)
ball_pos_x = ball.x
ball_pos_y = ball.y
ball_speed_x = 200
ball_speed_y = 200

player1 = Player(20, HEIGHT/2 - 50)

player2 = Player(WIDTH - 40, HEIGHT/2 - 50)
player2_pos_y = player2.rect.y
player2_speed = 250

# GameLoop 
previous_time = time.time()
while True:
    dt = time.time() - previous_time
    previous_time = time.time()
    screen.fill('black') 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            sys.exit()
    
    # Game Logic 
    # Movimento da bola com deltatime
    ball_pos_x += ball_speed_x * dt # Eixo X
    ball.x = ball_pos_x
    ball_pos_y += ball_speed_y * dt # Eixo Y
    ball.y = ball_pos_y
    
    # USAR INPUTS DE TECLADO AQUI  
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_w] and player1.rect.top > 5: 
        player1.move_up = True
    else: player1.move_up = False
    if keys[pygame.K_s] and player1.rect.bottom < (HEIGHT-5):
        player1.move_down = True
    else: player1.move_down = False
    player1.update(dt)

    # Movimento do Player 2
    if player2.rect.bottom < ball.top:
        player2_pos_y += player2_speed * dt
        player2.rect.y = player2_pos_y
    if player2.rect.top > ball.bottom:
        player2_pos_y -= player2_speed * dt
        player2.rect.y = player2_pos_y

    # condição de colisão
    if ball.colliderect(player2.rect) or ball.colliderect(player1.rect):
        ball_speed_x = -ball_speed_x
    if ball.bottom >= (HEIGHT-5) or ball.top <= 5:  
        ball_speed_y = -ball_speed_y

    # Render Game
    pygame.draw.ellipse(screen, 'white', ball, 100)
    player1.render(screen, 'cyan')
    player2.render(screen, 'red')
    
    pygame.display.update()
