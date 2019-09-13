from numpy import loadtxt
from pylab import *

p1 = loadtxt('refs/o-gauss-int1e8-2fs.polarization')
p2 = loadtxt('refs/o-gauss-int1e8-deph5meV.polarization')

xlabel('time (fs)')
plot(p2[:,0],p2[:,1],'-',label='$\\bf{P}$,  5 meV')
plot(p1[:,0],p1[:,1],'-',label='$\\bf{P}$, 50 meV')
legend(loc=1)
show()
