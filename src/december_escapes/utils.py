def detect_collision(player, obstacles):
    for obstacle in obstacles:
        if (
            player.x + player.radius > obstacle.x
            and player.x - player.radius < obstacle.x + obstacle.width
            and player.y + player.radius > obstacle.y
            and player.y - player.radius < obstacle.y + obstacle.height
        ):
            return True
    return False

def detect_goal(player, star):
    return (
        player.x + player.radius > star.x
        and player.x - player.radius < star.x + star.size
        and player.y + player.radius > star.y
        and player.y - player.radius < star.y + star.size
    )
