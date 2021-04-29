#Kay Towner

"""I got really lost with this one and followed along with a
tutorial from:  http://people.bu.edu/andasari/courses/
stochasticmodeling/lecture5/stochasticlecture5.html"""

import random
import numpy as np
import problem2_a as p2a  #for the animation
import matplotlib.pyplot as plt
import matplotlib.animation as animation

if __name__ == "__main__":
    T = 1.0
    L = 101 #length of the lattice
    dt = 1000000 #timestep
    t = np.linspace(dt, T, L)

    dX = np.sqrt(dt) * np.random.randn(1,L)
    X = np.cumsum(dX, axis=1)
    
    dY = np.sqrt(dt) * np.random.randn(1,L)
    Y = np.cumsum(dY, axis=1)
    
#b.) plotting:
    fig, ax = plt.subplots()
    ax.plot(X[0,:], Y[0,:])
    ax.plot(X[0,0], Y[0,0], 'ro')
    ax.plot(X[0,-1], Y[0,-1], 'yo')
    ax.set_title('Random Brownian Motion')
    plt.tight_layout()
    plt.show()


#animation: (OF POSITION OF THE PARTICLE:)
#______________________________________________________

    print("c.   Plot the track of the particle over 10000 steps (3 points)")
    pos = np.array([50, 50])
    maxsize = 101
    #run for 10,000 steps
    steps1e4 = p2a.run_simulation(n_steps=10000, initial_pos=pos, maxsize=maxsize)
    steps1e4 = np.random.randint(0, 101, size = (10000, 2))
    #animate the figure
    plt.ion()
    fig, ax = plt.subplots(figsize=(10,10))
    plt.xlim((0, maxsize))
    plt.ylim(0, maxsize)
    ax.set_aspect('equal')
    scat = ax.scatter(*pos)
    plt.title("Brownian motion in a box "+str(maxsize-1)+" units on a side")
    for i in range(10000):
        scat.set_offsets([steps1e4[i,0], steps1e4[i,1]])
        plt.draw()
        plt.pause(0.01)











    
