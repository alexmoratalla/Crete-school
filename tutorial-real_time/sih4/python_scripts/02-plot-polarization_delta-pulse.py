from numpy import loadtxt
from pylab import *


p1 = loadtxt('refs/o-delta-1e5.polarization')
p2 = loadtxt('refs/o-delta-1e6.polarization')
p3 = loadtxt('refs/o-delta-1e7.polarization')
p4 = loadtxt('refs/o-delta-1e8.polarization')

xlabel('time (fs)')
plot(p4[:,0],p4[:,1],'g-.',label='$\\bf{P},10^{8}$')
plot(p3[:,0],p3[:,1],'r--',label='$\\bf{P},10^{7}$')
plot(p1[:,0],p1[:,1],'b-' ,label='$\\bf{P},10^{6}$')
legend(loc=1)

show()
