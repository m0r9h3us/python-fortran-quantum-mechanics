from class_7 import *


sim=simulation(NPTS=1000,IMID=500,XMIN=-10,XMAX=10,GAM2=1)
sim.set_anharmonic_potential(epsilon=0.1)#
sim.set_gaussian(X0=1.,K0=0., SIGMA=1)
sim.evolve(NSTEP=1000,DT=0.005)

