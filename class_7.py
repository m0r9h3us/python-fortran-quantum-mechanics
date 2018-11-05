import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation
import ex_7
import time


class simulation(object):
    def __init__(self, NPTS=2000, IMID=500, XMIN=-9., XMAX=9., GAM2=1.):
        # grid
        self.NPTS = NPTS
        self.IMID = IMID
        self.XMIN = XMIN  # Left border x_min / a ?
        self.XMAX = XMAX  # Right border x_max / a
        self.GAM2 = GAM2  # Scaling factor gamma^2
        self.X = np.linspace(self.XMIN, self.XMAX, self.NPTS, dtype=np.float64)
        self.DX = np.float64(self.X[2] - self.X[1])

        self.V = np.zeros(NPTS, dtype=np.float64)
        self.PSI = np.zeros(self.NPTS, dtype=np.complex128)
        self.PSI2 = np.zeros(self.NPTS, dtype=np.float64)

        self.E = np.complex(0 + 0j)

        self.time = 0
        self.gamma = None

        # self.set_potential()
        self.set_gaussian()
        self.fig1 = plt.figure(figsize=(15, 10))

    def set_harmonic_potential(self):
        self.V = np.zeros(self.NPTS)
        self.V = self.GAM2 * self.X * self.X

    def set_anharmonic_potential(self, epsilon):
        self.V = np.zeros(self.NPTS)
        self.V = self.GAM2 * self.X * self.X + epsilon * self.X * self.X * self.X * self.X

    def set_squared_potential(self, MID=500, width=30, height=100):
        self.V = np.zeros(self.NPTS)
        for i in np.arange(self.NPTS):
            if i >= (MID - width) and i < (MID + width):
                self.V[i] = height * self.GAM2

    def set_double_squared_potential(self, MID=500, width=30, distance=10, height=100.):
        self.V = np.zeros(self.NPTS)
        for i in np.arange(self.NPTS):
            if i >= (MID - distance - width) and i < (MID - distance):
                self.V[i] = height * self.GAM2
            if i >= (MID + distance) and i < (MID + distance + width):
                self.V[i] = height * self.GAM2

    def set_gaussian(self, X0=0., K0=0., SIGMA=1.):
        self.PSI[1:-1] = np.exp(1j * K0 * self.X[1:-1]) * np.exp(-(self.X[1:-1] - X0) ** 2 / 2.0 / SIGMA ** 2)
        self.PSI2[1:-1] = np.abs(self.PSI[1:-1]) ** 2
        # normalize it
        LPROB, RPROB, TPROB, LX, RX, TX = ex_7.normlz(self.DX, self.X, self.PSI, self.PSI2)
        SNORM = TPROB
        SQRTN = np.sqrt(SNORM)
        self.PSI = self.PSI / SQRTN
        self.PSI2 = self.PSI2 / SNORM

    def evolve(self, NSTEP=1000, DT=0.01):
        self.fig1.clf()
        GAMMA = ex_7.trdiag(self.DX, DT, self.V)

        # fig1=plt.figure(figsize=(15,10))
        ax = self.fig1.add_subplot(111)
        ax.set_ylim(-1, 1)
        ax.set_xlabel('x')
        ax.plot(self.X, self.V)
        self.fig1.show(False)
        plt.draw()
        plot1 = ax.plot(self.X, self.PSI2, label=r"$\Psi^2$")[0]
        # plot2=ax.plot(self.X, self.PSI.real,label=r"Re($\Psi$)")[0]
        plt.legend()
        i = 0
        while (i <= NSTEP):
            print i

            # time.sleep(0.005)
            ex_7.evolve(self.DX, DT, self.PSI, self.PSI2, GAMMA)
            # abs^2
            plot1.set_data(self.X, self.PSI2)
            # plot2.set_data(self.X,self.PSI.real)
            self.fig1.canvas.draw()
            LPROB, RPROB, TPROB, LX, RX, TX = ex_7.normlz(self.DX, self.X, self.PSI, self.PSI2)
            E = ex_7.energy(self.DX, self.PSI, self.PSI2, self.V)
            print "P:%.8e, TX:%.4e, E:%.8e" % (TPROB, TX, E)
            # abs
            # plot2.set_data(X,PSI.real)
            # fig2.canvas.draw()
            # pics.append(plot)
            i += 1

        self.time += DT * NSTEP

    def reset(self):
        self.time = 0
        self.V = np.zeros(self.NPTS)
        self.PSI = np.zeros(self.NPTS, dtype=np.complex)
        self.PSI2 = np.zeros(self.NPTS)

        self.time = 0
        self.gamma = None

        # self.set_potential()
        self.set_gaussian()

# if __name__ == "__main__":
# sim=simulation(NPTS=1000,IMID=500,XMIN=-7,XMAX=20,GAM2=1)

# sim.set_squared_potential(MID=500,width=20,height=100)
# sim.set_harmonic_potential()

# sim.set_gaussian(X0=0,K0=10., SIGMA=1)
# sim.evolve(NSTEP=100,DT=0.001)
