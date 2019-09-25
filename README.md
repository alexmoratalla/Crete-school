# Crete-school

This repository contains the input files of Quantum Espresso (6.41) and Yambo (4.4) of the following tutorials:

- Basics with QE
- Ground State
- Optical Properties
- Real Time simulations

In each tutorial we have employed the following materials:

- Silicon (a bulk)
- Hexagonal Boron Nitride (a 2D material)
- SiH4 (a molecule)


To run the SiH4 yambo tutorial:
1) enter the folder tutorials tutorial-ground_state/sih4
2) run

   ``pw.x < sih4.scf > sih4.scf.out``
3) run

   ``pw.x < sih4.nscf > sih4.nscf.out``
4) enter pw.save folder

   ``cd pw.save``
5) run p2y

   ``p2y``
   
   which generates the SAVE folder
6) move the SAVE folder

   ``mv SAVE ../../../tutorial-real_time/sih4``
7) enter sih4 folder

   ``cd ../../../tutorial-real_time/sih4``
8) run yambo initialization

   ``yambo -F inputs/00-init``
9) run yambo to compute IP optical properties

   ``yambo -F inputs/01-ip-reference -C 01-ip-reference``
   
   Have a look to the input file and the output with gnuplot

Now we are ready for the real time simulations
10) remove the symmetries 
   ``ypp_rt -F inputs/02-break-sym_ypp``
   This will create a FixSymm folder with a new SAVE.
   enter it.
   ``cd FixSymm``
11) run initialization again
    ``yambo_rt -F ../inputs/03_init``
12) run yambo_rt to perform a TD-IP simulation
   ``yambo_rt -F inputs/04-ip-dynamics-delta -J delta1 -C delta1``
   This will create a delta1 folder with results from the real time simulation.
   You can plot the polarization / current / external field
13) finally you can process the polarization to get the dielectric function
    ``ypp_rt -F ../inputs/05-response_ypp -J delta1 -C delta1``
    The results to be plotted are again in delta1

The slides of the lectures and tutorials can be downloaded from:

https://www.dropbox.com/sh/z7i2z20pwvp4igz/AABIvpHuY1e0GNWyUI4QpwvWa?dl=0
