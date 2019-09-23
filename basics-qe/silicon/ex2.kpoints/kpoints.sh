#!/bin/sh
# reminder: from now on, what follows the character # is a comment
# the ecuwfc value has to be set to the converged value of ex1.ecutwfc

# delete the Etot-vs-kpoint.dat if it exists
rm -f Etot-vs-kpoint.dat

# loop over number of k points along each crystal direction
for nk in 2 4 6 8
do
    echo "Running for k grid = $nk, $nk, $nk ..."

    # self-consistent calculation
    cat > pw.si.scf.in << EOF
 &CONTROL
    prefix='silicon',
    pseudo_dir="./"
 /
 &SYSTEM    
    ibrav =  2, 
    celldm(1) = 10.2, 
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
   $nk $nk $nk 1 1 1
EOF

    # run the pw.x calculation
    pw.x -in pw.si.scf.in > pw.si.scf.out

    # collect the total-energy from the pw.si.scf.out output-file
    
    grep -e 'number of k points=' -e ! pw.si.scf.out | \
        awk '/number of k points=/ {nktot=$(NF)}
             /!/              {print nktot, $(NF-1)}' >> Etot-vs-kpoint.dat

done

# plot the result

gnuplot plot.gp
