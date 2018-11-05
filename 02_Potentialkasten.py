from class_7 import *


sim=simulation(NPTS=2000,IMID=1000,XMIN=-3,XMAX=3,GAM2=1)
#sim.set_double_squared_potential(MID=1000,width=30,distance=10,height=100000.)
sim.set_gaussian(X0=0,K0=0., SIGMA=1)
sim.evolve(NSTEP=800,DT=0.01)
