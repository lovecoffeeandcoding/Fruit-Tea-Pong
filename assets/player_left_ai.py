from random import randint
def move_player_left(player_left_y: int, ball_y: int, points: tuple) -> int:
    # points = (player_left_points, player_right_points)
    min_speed = 6 + points[1] - points[0]
    if min_speed >= 8:
        min_speed = 8
    speed = randint(min_speed, 9)
    if player_left_y  < ball_y:
        player_left_y += speed
    elif player_left_y > ball_y:
        player_left_y -= speed
    return player_left_y