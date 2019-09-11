from numpy import loadtxt
from pylab import *

ref = loadtxt('refs/o-ip-ref.eps_q1_ip')
chi1= loadtxt('gauss-1e2-w20/o-gauss-1e2-w20.YPP-eps_along_E')
chi2= loadtxt('gauss-1e2-w30/o-gauss-1e2-w30.YPP-eps_along_E')


xlabel('E (eV)')
ylabel('$\epsilon$')
plot(ref[:,0],ref[:,1],'o',label='$\chi$(reference)')
plot(chi1[:,0],chi1[:,1],'-',label='$t=20$ s')
plot(chi2[:,0],chi2[:,1],'-',label='$t=30$ s')
#plot(chi3[:,0],chi3[:,1],'-',label='$I=5 \\times 10^{3}$')
legend()
show()
