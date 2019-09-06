from numpy import loadtxt
from pylab import *


p1 = loadtxt('refs/o-delta-1e2.polarization')
p2 = loadtxt('refs/o-delta-1e5.polarization')

xlabel('time (fs)')
plot(p1[:,0],p1[:,1],'b-',label='$\\bf{P},10^{2}$')
legend(loc=1)
twinx()               
plot(p2[:,0],p2[:,1],'r--',label='$\\bf{P},10^{5}$')
legend(loc=2)

show()
