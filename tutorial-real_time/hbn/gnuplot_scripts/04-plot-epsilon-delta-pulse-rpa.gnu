set terminal x11

p 'refs/o-rpa-reference-x.eps_q1_inv_rpa_dyson' w p t 'chi-x RPA reference', 'refs/o-rpa-reference-z.eps_q1_inv_rpa_dyson' w p t 'chi-z RPA reference', 'refs/o-rpa-delta-1e5-x.YPP-eps_along_E' w l t 'chi-x RPA 10E5', 'refs/o-rpa-delta-1e5-z.YPP-eps_along_E' w l t 'chi-z RPA 10E5'

set xlabel 'E (eV)' 
set ylabel 'chi'

pause -1 "Hit any key to continue"

