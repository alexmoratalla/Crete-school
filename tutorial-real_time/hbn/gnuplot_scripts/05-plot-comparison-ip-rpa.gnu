set terminal x11

p 'refs/o-rpa-reference-x.eps_q1_inv_rpa_dyson' w l t 'IP-x', 'refs/o-rpa-reference-z.eps_q1_inv_rpa_dyson' w l t 'IP-z', 'refs/o-ip-reference-x.eps_q1_ip' w l t 'RPA-x', 'refs/o-ip-reference-z.eps_q1_ip' w l t 'RPA-z'

set xlabel 'E (eV)' 
set ylabel 'chi'
 
pause -1 "Hit any key to continue"
