from numpy import loadtxt
from pylab import *

ref = loadtxt('refs/o-ip-reference.eps_q1_ip')

xlabel('E (eV)')
ylabel('$\chi$')
plot(ref[:,0],ref[:,1],'o',label='$\chi$(reference)')
legend()
show()
