from numpy import loadtxt
from pylab import *

ref = loadtxt('refs/o-ip-ref.eps_q1_ip')
chi1= loadtxt('refs/o-delta-1e5.YPP-eps_along_E')
chi2= loadtxt('refs/o-delta-1e6.YPP-eps_along_E')
chi3= loadtxt('refs/o-delta-1e7.YPP-eps_along_E')
chi4= loadtxt('refs/o-delta-1e8.YPP-eps_along_E')

xlabel('E (eV)')
ylabel('$\chi$')
plot(ref[:,0],ref[:,1],'o',label='$\chi$(reference)')
plot(chi1[:,0],chi1[:,1],'-',label='$I=10^{5}$')
plot(chi2[:,0],chi2[:,1],'-',label='$I=10^{6}$')
plot(chi3[:,0],chi3[:,1],'-',label='$I=10^{7}$')
plot(chi4[:,0],chi4[:,1],'-',label='$I=10^{8}$')
legend(loc=1)
show()
