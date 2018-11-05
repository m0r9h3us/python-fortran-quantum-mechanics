from class_7 import *


sim=simulation(NPTS=2000,IMID=1000,XMIN=-15,XMAX=15,GAM2=1)
sim.set_squared_potential(MID=1000,width=80,height=100)
sim.set_gaussian(X0=-8,K0=10., SIGMA=1)
sim.evolve(NSTEP=800,DT=0.001)
