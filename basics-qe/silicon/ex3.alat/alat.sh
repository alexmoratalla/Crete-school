#!/bin/sh
# reminder: from now on, what follows the character # is a comment
# the ecuwfc value has to be set to the converged value of ex1.ecutwfc
# the kpoint mesh has to be set to the converged value of ex2.kpoints

# delete the Etot-vs-kpoint.dat if it exists
rm -f Etot-vs-alat.dat

# loop over alat values
for alat in 9.7 9.8 9.9 10.0 10.1 10.2 10.3 10.4 10.5 10.6 10.7
do
    echo "Running for alat = $alat..."

    # self-consistent calculation
    cat > pw.si.scf.in << EOF
 &CONTROL
    prefix='silicon',
    pseudo_dir="./"
 /
 &SYSTEM    
    ibrav =  2, 
    celldm(1) = $alat, 
    nat =  2, 
    ntyp = 1,
    ecutwfc = 20, 
 /
 &ELECTRONS
 /
ATOMIC_SPECIES
   Si  28.086  Si.pz-vbc.UPF
ATOMIC_POSITIONS
   Si 0.00 0.00 0.00 
   Si 0.25 0.25 0.25 
K_POINTS automatic
   4 4 4 1 1 1
EOF

    # run the pw.x calculation
    pw.x -in pw.si.scf.in > pw.si.scf.out

    # collect the total-energy from the pw.si.scf.out output-file
    
    grep -e 'celldm(1)' -e ! pw.si.scf.out | \
        awk '/celldm(1)/ {alat=$(NF)}
             /!/              {print alat, $(NF-1)}' >> Etot-vs-alat.dat

done

# plot the result

gnuplot plot.gp
