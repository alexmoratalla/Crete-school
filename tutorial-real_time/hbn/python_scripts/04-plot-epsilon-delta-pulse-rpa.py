from numpy import loadtxt
from pylab import *

refx = loadtxt('refs/o-rpa-reference-x.eps_q1_inv_rpa_dyson')
refz = loadtxt('refs/o-rpa-reference-z.eps_q1_inv_rpa_dyson')
chix = loadtxt('refs/o-rpa-delta-1e5-x.YPP-eps_along_E')
chiz = loadtxt('refs/o-rpa-delta-1e5-z.YPP-eps_along_E')

xlabel('E (eV)')
ylabel('$\chi$')
plot(refx[:,0],refx[:,1],'o',label='$\chi-x$(reference)')
plot(refz[:,0],refz[:,1],'o',label='$\chi-z$(reference)')
plot(chix[:,0],chix[:,1],'-',label='$10^{5}-x$')
plot(chiz[:,0],chiz[:,1],'-',label='$10^{5}-z$')
legend()
show()
