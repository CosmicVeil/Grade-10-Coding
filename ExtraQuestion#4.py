#Name: Mohan, Steven
# Purpose: Modules

import random
import time

time_period = int(input("How long do you want to view the particles(seconds): "))

prev_velocity = 0

for i in range(time_period):
    time.sleep(1)
    velocity = random.randint(1,1000)

    print("The current velocity is", velocity, "kilometers per hour")

    print("The velocity has changed by", velocity-prev_velocity, "since the last second")

    prev_velocity = velocity

    



