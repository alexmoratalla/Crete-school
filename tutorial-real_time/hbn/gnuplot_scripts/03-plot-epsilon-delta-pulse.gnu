
set terminal x11
set xlabel 'E (eV)'
set ylabel 'chi'

p 'refs/o-ip-reference-x.eps_q1_ip' w p t 'chi-x reference', 'refs/o-ip-reference-z.eps_q1_ip' w p t 'chi-z reference', 'refs/o-delta-1e5-x.YPP-eps_along_E' w l t 'chi-x 10E5', 'refs/o-delta-1e5-z.YPP-eps_along_E' w l t 'chi-z 10E5'

pause -1 "Hit any key to continue"

