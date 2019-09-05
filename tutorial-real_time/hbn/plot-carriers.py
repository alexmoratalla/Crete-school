from numpy import loadtxt
from pylab import *

c = loadtxt('references/o-int-1000.carriers')
p = loadtxt('references/o-int-1000.polarization')
xlabel('time (fs)')
plot(c[:,0],c[:,2],'-',label='N electrons')
legend()
twinx()               
plot(p[:,0],p[:,1],'r-', label='Polarization')
legend()
savefig('carriers-polarization-1E3.png')
#show()
