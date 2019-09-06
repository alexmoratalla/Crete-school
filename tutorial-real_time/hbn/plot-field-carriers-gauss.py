from numpy import loadtxt
from pylab import *

e2 = loadtxt('refs/o-gauss-int1e10-2fs.external_field')
e3 = loadtxt('refs/o-gauss-int1e11-2fs.external_field')

p2 = loadtxt('refs/o-gauss-int1e10-2fs.polarization')
p3 = loadtxt('refs/o-gauss-int1e11-2fs.polarization')

xlabel('time (fs)')
plot(p2[:,0],p2[:,1],'b--',label='$\\bf{P},10^{10}$')
plot(p3[:,0],p3[:,1],'b-.',label='$\\bf{P},10^{11}$')
legend(loc=1)
twinx()               
plot(e2[:,0],e2[:,7],'r--',label='$\\bf{E},10^{10}$')
plot(e3[:,0],e3[:,7],'r-.',label='$\\bf{E},10^{11}$')
legend(loc=4)

show()
