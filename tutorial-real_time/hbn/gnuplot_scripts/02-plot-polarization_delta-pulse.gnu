set terminal x11
set xlabel 'time (fs)'
p 'refs/o-delta-1e5-x.polarization' w l t 'P-x 10E5', 'refs/o-delta-1e5-z.polarization' w l t 'P-z 10E5' axes x1y2
pause -1 "Hit any key to continue"
