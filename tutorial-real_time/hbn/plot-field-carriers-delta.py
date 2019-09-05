from numpy import loadtxt
from pylab import *


p1 = loadtxt('refs/o-delta-1e6.polarization')
p1 = loadtxt('refs/o-delta-1e12.polarization')
p1 = loadtxt('refs/o-delta-1e16.polarization')

xlabel('time (fs)')
plot(p1[:,0],p1[:,1],'b--',label='$\\bf{P},10^{10}$')
#plot(p3[:,0],p3[:,1],'b-.',label='$\\bf{P},10^{11}$')
legend(loc=1)
#twinx()               
#plot(e2[:,0],e2[:,7],'r--',label='$\\bf{E},10^{10}$')
#plot(e3[:,0],e3[:,7],'r-.',label='$\\bf{E},10^{11}$')
#legend(loc=4)

show()
