import math
import random
import matplotlib.pyplot as plt

vb = random.randint(100, 200)
vf = random.randint(200, 300)

xb, yb = 1000, 1000
xf, yf = 0, 0

def polorchord(xb, yb, xf, yf):
    r = math.sqrt((xb - xf)**2 + (yb - yf)**2)
    theta = math.atan2(yb - yf, xb - xf)
    return r, theta

def update(r, theta, dt, vb, vf):
    dr_dt = vb * math.cos(theta) - vf
    dtheta_dt = -vb * math.sin(theta) / r
    r += dr_dt * dt
    theta += dtheta_dt * dt
    return r, theta

def simulate(xb, yb, xf, yf, vb, vf):
    dt = 0.01
    time = 0
    r, theta = polorchord(xb, yb, xf, yf)
    
    prevR = []
    prevTime = []
    
    while r > 10:
        r, theta = update(r, theta, dt, vb, vf)
        time += dt
        prevR.append(r)
        prevTime.append(time)
    
    print(f"Target hit at time: {time:.2f} seconds")
    
    plt.plot(prevTime, prevR)
    plt.title('Distance r between Fighter and Bomber over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Distance r (units)')
    plt.show()

simulate(xb, yb, xf, yf, vb, vf)
