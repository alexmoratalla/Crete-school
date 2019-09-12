import matplotlib.pyplot as plt
from numpy import loadtxt
from pylab import *

f1= loadtxt('refs/o-gauss-1e2-w20.external_field')
f2= loadtxt('refs/o-gauss-1e2-w30.external_field')
f3= loadtxt('refs/o-gauss-1e2-w5.external_field')
pul1= loadtxt('refs/o-gauss-1e2-w20.YPP-E_frequency')
pul2= loadtxt('refs/o-gauss-1e2-w30.YPP-E_frequency')
pul3= loadtxt('refs/o-gauss-1e2-w5.YPP-E_frequency')


fig, axs = plt.subplots(2)

axs[0].plot(f1[:,0],f1[:,1],'-',label='$t=20$ s')
axs[0].plot(f2[:,0],f2[:,1],'-',label='$t=30$ s')
axs[0].plot(f3[:,0],f3[:,1],'-',label='$t= 5$ s')
axs[0].set_xlabel('time (fs)')
#legend(loc=1)
#twinx()               
axs[1].plot(pul1[:,0],pul1[:,1]**2+pul1[:,4]**2,'-',label='$t=20$ s')
axs[1].plot(pul2[:,0],pul2[:,1]**2+pul2[:,4]**2,'-',label='$t=30$ s')
axs[1].plot(pul3[:,0],pul3[:,1]**2+pul3[:,4]**2,'-',label='$t= 5$ s')
plt.xlabel('E (eV)')

legend(loc=2)
show()
