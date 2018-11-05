from class_7 import *


sim=simulation(NPTS=2000,IMID=1000,XMIN=-15,XMAX=15,GAM2=1)
sim.set_harmonic_potential()#GAM2*x*x
sim.set_gaussian(X0=-2,K0=0., SIGMA=1)
sim.evolve(NSTEP=500,DT=0.01)

