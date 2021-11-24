GRAVITY = 1
ELASTICITY = 0.8


def gravity(ball):
    ball.speed.y += GRAVITY

    
def reflect(ball, wall):
    ball.speed = ball.speed.reflect(wall)

    new_length = round(ball.speed.length() * ELASTICITY, 2)
    if new_length < 4.5:
        new_length = 0
    ball.speed.scale_to_length(new_length)

    ball.x += ball.speed.x
    ball.y += ball.speed.y

    return ball.speed, ball.x, ball.y


def push_ball(ball):
    ball.frozen = False
