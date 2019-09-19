from numpy import loadtxt
from pylab import *

ip  = loadtxt('refs/o-ip-reference.eps_q1_ip')
ref = loadtxt('refs/o-rpa-reference.eps_q1_inv_rpa_dyson')
rpa = loadtxt('refs/o-rpa-delta-1e2.YPP-eps_along_E')

xlabel('E (eV)')
ylabel('$\chi$')
plot(ip[:,0],ip[:,1],'--',label='$\chi$ (IP reference)')
plot(ref[:,0],ref[:,1],'o',label='$\chi$ (RPA reference)')
plot(rpa[:,0],rpa[:,1],'-',label='$\chi$ (RPA delta-pulse)')

legend()
show()
