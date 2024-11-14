import math
import random
import matplotlib.pyplot as plt

mouses = 8 * 1000 / 3600                   
snakes = 12 * 1000 / 3600
mongooses = 18 * 1000 / 3600
dogs = 30 * 1000 / 3600

fieldsize = 500

def distance(x1, y1, x2, y2):                              
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def updateposition(chaser_x, chaser_y, target_x, target_y, speed, time_delta):     
    distance_between = distance(chaser_x, chaser_y, target_x, target_y)
    
    if distance_between == 0:
        return chaser_x, chaser_y
    
    move_x = (target_x - chaser_x) / distance_between * speed * time_delta
    move_y = (target_y - chaser_y) / distance_between * speed * time_delta
    
    return chaser_x + move_x, chaser_y + move_y



mousep = [random.randint(0, fieldsize), random.randint(0, fieldsize)]   
snakep = [random.randint(0, fieldsize), random.randint(0, fieldsize)]
mongoosep = [random.randint(0, fieldsize), random.randint(0, fieldsize)]
dogp = [random.randint(0, fieldsize), random.randint(0, fieldsize)]

dt = 0.1

mouset = [mousep[:]]  
snaket = [snakep[:]]
mongooset = [mongoosep[:]]
dogt = [dogp[:]]

def simulate():
    time = 0
    while True:
        time += dt
        dogp[0], dogp[1] = updateposition(dogp[0], dogp[1], mongoosep[0], mongoosep[1], dogs, dt)   # xcoordinate and ycoordinate
        mongoosep[0], mongoosep[1] = updateposition(mongoosep[0], mongoosep[1], snakep[0], snakep[1], mongooses, dt)
        snakep[0], snakep[1] = updateposition(snakep[0], snakep[1], mousep[0], mousep[1], snakes, dt)
        mousep[0], mousep[1] = updateposition(mousep[0], mousep[1], 0, 0, mouses, dt)

        mouset.append(mousep[:])
        snaket.append(snakep[:])
        mongooset.append(mongoosep[:])
        dogt.append(dogp[:])

        if distance(dogp[0], dogp[1], mongoosep[0], mongoosep[1]) < 1:
            print(f"Dog caught the mongoose after {time:.2f} seconds!")
            break
        if distance(mongoosep[0], mongoosep[1], snakep[0], snakep[1]) < 1:
            print(f"Mongoose caught the snake after {time:.2f} seconds!")
            break
        if distance(snakep[0], snakep[1], mousep[0], mousep[1]) < 1:
            print(f"Snake caught the mouse after {time:.2f} seconds!")
            break

simulate()

plt.figure(figsize=(10, 10))
plt.xlim(0, fieldsize)
plt.ylim(0, fieldsize)

mousex, mousey = zip(*mouset)
snakex, snakey = zip(*snaket)
mongoosex, mongoosey = zip(*mongooset)
dogx, dogy = zip(*dogt)

plt.plot(mousex, mousey, label='Mouse T', color='blue')
plt.plot(snakex, snakey, label='Snake T', color='green')
plt.plot(mongoosex, mongoosey, label='Mongoose T', color='orange')
plt.plot(dogx, dogy, label='Dog T', color='red')

plt.scatter(mouset[0][0], mouset[0][1], color='blue', marker='o', s=100, label='Mouse Start')
plt.scatter(snaket[0][0], snaket[0][1], color='green', marker='o', s=100, label='Snake Start')
plt.scatter(mongooset[0][0], mongooset[0][1], color='orange', marker='o', s=100, label='Mongoose Start')
plt.scatter(dogt[0][0], dogt[0][1], color='red', marker='o', s=100, label='Dog Start')

plt.scatter(mouset[-1][0], mouset[-1][1], color='blue', marker='x', s=100, label='Mouse End')
plt.scatter(snaket[-1][0], snaket[-1][1], color='green', marker='x', s=100, label='Snake End')
plt.scatter(mongooset[-1][0], mongooset[-1][1], color='orange', marker='x', s=100, label='Mongoose End')
plt.scatter(dogt[-1][0], dogt[-1][1], color='red', marker='x', s=100, label='Dog End')

plt.title("Animal Chase Simulation in 500x500 Meter Field")
plt.xlabel("X Position (meters)")
plt.ylabel("Y Position (meters)")
plt.legend()
plt.grid(True)
plt.show()
