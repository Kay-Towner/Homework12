#finished by Kay Towner

import math
import numpy as np
import matplotlib.pyplot as plt

def probability(t=None, tau=None):
    return 1- 2**(-t/tau)

if __name__ == "__main__":
    NBi = 10000 #number of atoms of Bi
    NPb = 0
    NTl = 0
    tau_Bi = 1 #half life in seconds
    timestep = 1 #second
    tmax = 1000
    p_decay = probability(t=timestep, tau=tau_Bi)#decay probability in one second
    print("Probability of Decay:", p_decay)

    ts = np.arange(0, tmax, timestep)

    Bi = []
    Pb = []
    Tl = []
    for t in ts:
        #log number of remaning Bi, Tl and Pb
        Bi.append(NBi)
        Pb.append(NPb)
        Tl.append(NTl)
        #step through # of Bi atoms remaining
        for i in range(NBi):
            #if atom decays, one
            if np.random.random() < p_decay: #if each atom decays:
                NBi = NBi-1
                NPb = NPb+1
            if np.random.random() < p_decay:
                NTl = NTl-1
                NPb = NPb+1
    plt.plot(ts, Bi, 'k.', label = 'Bl')
    plt.plot(ts, Pb, 'r.', label = 'Pb')
    plt.plot(ts, Tl, 'g.', label = 'Tl')
    plt.xlabel('Time [s]')
    plt.ylabel('Number of atoms')
    plt.legend()
    plt.show()












    
