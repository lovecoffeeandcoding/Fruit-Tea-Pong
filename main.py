import pygame
import winsound

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range (pygame.joystick.get_count())]

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH,HEIGHT))
background_image = pygame.image.load("tea.png")

ball = pygame.image.load("ball.png")
player1_image = pygame.image.load("player1.jpg")
player2_image = pygame.image.load("player2.jpg")

raspberry_image = pygame.image.load("raspberry.png")
peach_image = pygame.image.load("peach.png")
trophaeA = pygame.image.load("trophae1.png")
trophaeB = pygame.image.load("trophae2.png")

# start position of player 1 (raspberry)
raspberry_x = 80
raspberry_y = 300

# start position of player 2 (peach)
peach_x = 1200
peach_y = 300

# position of score from player 1 (raspberry)
raspberry_x_score = 520
raspberry_y_score = 35

# position of score from player 2 (peach)
peach_x_score = 740
peach_y_score = 38

textx = 630
texty = 60

font = pygame.font.Font('freesansbold.ttf', 37)

# start position of score from player 2 (peach)
ball_x = 650
ball_y = 300

# speed of the ball
movement_x = 9
movement_y = 9

#both games (fruits) start with 0 points
score_raspberry = 0
score_peach = 0


running = True

# Main loop of the game
while (running):

    # Check whether events are in the event queue
    for event in pygame.event.get():

        # if "x" is clicked, the program is terminated
        if event.type == pygame.QUIT:
            running = False

    # All keys on the keyboard are packed into a dictionary. The value is either True if the
    # key is currently pressed or False if the key is not currently pressed.
    keys = pygame.key.get_pressed()

    # Query the buttons for the control (Keyboard and Gamepad). When the "s" key is pressed,
    # Player 1 (raspberry) moves up by 3 pixels and so on.
    if keys[pygame.K_w]:
        raspberry_y = raspberry_y - 9
    if keys[pygame.K_s]:
        raspberry_y = raspberry_y + 9

    if keys[pygame.K_DOWN]:
        peach_y = peach_y + 9
    if keys[pygame.K_UP]:
        peach_y = peach_y - 9

    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 2:
            raspberry_y = raspberry_y + 9
        elif event.button == 3:
            raspberry_y = raspberry_y - 9

    if event.type == pygame.JOYBUTTONDOWN:
        if event.button == 1:
            peach_y = peach_y + 9
        elif event.button == 0:
            peach_y = peach_y - 9

    # movement of ball
    ball_x = ball_x + movement_x
    ball_y = ball_y + movement_y

    # Check whether the ball touches the edges (top/bottom) of the court.
    if ball_y > 694 or ball_y < 4:
        movement_y = movement_y * -1

    """ Checking whether there is a collision between player 1 or 2 and the ball. 
    Game graphics of player 1 and 2 as well as the graphics of the ball must first be converted into rectangles. 
    The system therefore checks whether there is a collision with the rectangles. 
    If so, the ball should bounce/rebound"""

    image_ball = ball
    rect = image_ball.get_rect(center=(ball_x, ball_y))
    image_ball_center = rect.center

    image_player1 = player1_image
    rect2 = image_player1.get_rect(center=(raspberry_x, raspberry_y))
    image_player1_center = rect2.center

    image_player2 = player2_image
    rect3 = image_player2.get_rect(center=(peach_x, peach_y))
    image_player2_center = rect3.center

    if rect.colliderect(rect2):
        movement_x = movement_x * -1
        #movement_x = movement_x * random.randint(1, 5)
        winsound.Beep(330, 20)

    elif rect.colliderect(rect3):
        movement_x = movement_x * -1
        #movement_x = movement_x * random.randint(1, 5)
        winsound.Beep(330, 20)

    # If a player does not reach the ball, the opponent gets a point
    if ball_x < 0:
        ball_x = 500
        score_peach = score_peach + 1
        winsound.Beep(130, 2000)

    if ball_x > 1256:
        ball_x = 500
        score_raspberry = score_raspberry + 1
        winsound.Beep(130, 2000)

    # Preventing a player from reaching the edge of the playing area
    if raspberry_y < 0:
        raspberry_y = 0

    if peach_y < 0:
        peach_y = 0

    if raspberry_y > 619:
        raspberry_y = 619

    if peach_y > 619:
        peach_y = 619

    # Draw playing field and game graphics
    screen.blit(background_image, (0,0))

    screen.blit(ball,(ball_x,ball_y))
    screen.blit(player1_image, (raspberry_x,raspberry_y))
    screen.blit(player2_image, (peach_x, peach_y))
    screen.blit(raspberry_image, (raspberry_x_score, raspberry_y_score))
    screen.blit(peach_image, (peach_x_score, peach_y_score))

    font = pygame.font.Font(None, 74)
    text = font.render(str(score_raspberry), 1, (255, 255, 255))
    screen.blit(text, (610,55))
    text = font.render(str(score_peach), 1, (255, 255, 255))
    screen.blit(text, (700,55))

    text_ = font.render(("-"), 1, (255, 255, 255))
    screen.blit(text_, (660, 55))

    # Whoever reaches 4 points first wins the game and receives a trophy
    if score_raspberry == 4:
        screen.blit(trophaeA, (550, 300))
        pygame.time.delay(100)

    if score_peach == 4:
        screen.blit(trophaeB, (550, 300))
        pygame.time.delay(100)

    pygame.display.update()
pygame.quit()