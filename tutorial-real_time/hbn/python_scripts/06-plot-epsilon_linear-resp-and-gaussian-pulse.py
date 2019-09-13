from numpy import loadtxt
from pylab import *

ref = loadtxt('refs/o-ip-ref.eps_q1_ip')
chi1= loadtxt('refs/o-gauss-int1e8-2fs.YPP-eps_along_E')
chi2= loadtxt('refs/o-gauss-int1e10-2fs.YPP-eps_along_E')
chi3= loadtxt('refs/o-gauss-int1e11-2fs.YPP-eps_along_E')


xlabel('E (eV)')
ylabel('$\epsilon$')
plot(ref[:,0],ref[:,1],'o',label='$\chi$(reference)')
plot(chi1[:,0],chi1[:,1],'-',label='$10^{8}$')
plot(chi2[:,0],chi2[:,1],'-',label='$10^{10}$')
plot(chi3[:,0],chi3[:,1],'-',label='$10^{11}$')
legend()
show()
