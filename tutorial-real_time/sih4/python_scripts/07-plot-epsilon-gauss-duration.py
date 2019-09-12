from numpy import loadtxt
from pylab import *

ref = loadtxt('refs/o-ip-ref.eps_q1_ip')
chi1= loadtxt('refs/o-gauss-1e2-w20.YPP-eps_along_E')
chi2= loadtxt('refs/o-gauss-1e2-w30.YPP-eps_along_E')
pul1= loadtxt('refs/o-gauss-1e2-w20.YPP-E_frequency')
pul2= loadtxt('refs/o-gauss-1e2-w30.YPP-E_frequency')


xlabel('E (eV)')
ylabel('$\epsilon$')
plot(ref[:,0],ref[:,1],'o',label='$\chi$(reference)')
plot(chi1[:,0],chi1[:,1],'-',label='$t=20$ s')
plot(chi2[:,0],chi2[:,1],'-',label='$t=30$ s')
legend(loc=1)
twinx()               
plot(pul1[:,0],pul1[:,1]**2+pul1[:,4]**2,'--',label='$t=20$ s')
plot(pul1[:,0],pul2[:,1]**2+pul2[:,4]**2,'--',label='$t=30$ s')
legend(loc=2)
show()
