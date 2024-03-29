from numpy import loadtxt
from pylab import *

refx = loadtxt('refs/o-ip-reference-x.eps_q1_ip')
refz = loadtxt('refs/o-ip-reference-z.eps_q1_ip')

xlabel('E (eV)')
ylabel('$\chi$')
plot(refx[:,0],refx[:,1],'o',label='$\chi-x$(reference)')
plot(refz[:,0],refz[:,1],'o',label='$\chi-z$(reference)')
legend()
show()
