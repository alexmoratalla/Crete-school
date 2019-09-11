from numpy import loadtxt
from pylab import *

ref = loadtxt('refs/o-ip-ref.eps_q1_ip')
chi1= loadtxt('refs/o-gauss-1e2-w10.YPP-eps_along_E')
chi2= loadtxt('refs/o-gauss-1e3-w10.YPP-eps_along_E')
chi3= loadtxt('refs/o-gauss-5e3-w10.YPP-eps_along_E')


xlabel('E (eV)')
ylabel('$\epsilon$')
plot(ref[:,0],ref[:,1],'o',label='$\chi$(reference)')
plot(chi1[:,0],chi1[:,1],'-',label='$I=10^{2}$')
plot(chi2[:,0],chi2[:,1],'-',label='$I=10^{3}$')
plot(chi3[:,0],chi3[:,1],'-',label='$I=5 \\times 10^{3}$')
legend()
show()
