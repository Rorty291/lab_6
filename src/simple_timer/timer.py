from time import sleep
import math

def start_timer(wait_time: float | int, display_function=None):
    """
        Розпочинає таймер від wait_time до 0
    """
    multi = 0
    while wait_time % math.floor(wait_time) != 0:
        multi += 1
        wait_time *= 10

    while wait_time > 0:
        if display_function:
            display_function(wait_time / (10 ** multi))

        time_left = min((10 ** multi), wait_time)
        wait_time = max(0, wait_time - (10 ** multi))
        sleep(time_left / 10 ** multi)

    if display_function:
        display_function(wait_time)

    return True