from numpy import loadtxt
from pylab import *

rpax = loadtxt('refs/o-rpa-reference-x.eps_q1_inv_rpa_dyson')
rpaz = loadtxt('refs/o-rpa-reference-z.eps_q1_inv_rpa_dyson')
ipx  = loadtxt('refs/o-ip-reference-x.eps_q1_ip')
ipz  = loadtxt('refs/o-ip-reference-z.eps_q1_ip')

xlabel('E (eV)')
ylabel('$\chi$')
plot(ipx[:,0],ipx[:,1],'--',label='$IP-x$')
plot(ipz[:,0],ipz[:,1],'--',label='$IP-z$')
plot(rpax[:,0],rpax[:,1],'-',label='$RPA-x$')
plot(rpaz[:,0],rpaz[:,1],'-',label='$RPA-z$')
legend()
show()
