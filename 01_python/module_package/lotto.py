import random

a= 1
b = [1,2]


def pick_lotto():
    lucky = random.sample(range(1,46), 6)
    return lucky