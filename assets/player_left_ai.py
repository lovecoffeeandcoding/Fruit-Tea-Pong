def move_player_left(player_left_y: int, ball_y: int, points: tuple) -> int:
    # points = (player_left_points, player_right_points)
    speed_modifier = 6 + points[1] - points[0]
    if speed_modifier >= 8:
        speed_modifier = 8
    speed = (speed_modifier + 9) / 2
    if player_left_y  < ball_y:
        player_left_y += speed
    elif player_left_y > ball_y:
        player_left_y -= speed
    return player_left_y