# PURPOSE OF THE EXERCISE: 
## How to calculate and plot molecular orbitals of benzene (actually sign(psi(r))*|psi(r)|^2)
-------------------------------------------------------

**Steps to perform:**

1. `pw.x` SCF calculation as to calculate Kohn-Sham states

       pw.x < pw.SiH4.scf.in > pw.SiH4.scf.out


2. `pp.x` (post-processing) calculation of all valence and LUMO
   molecular orbitals ( actually sign(psi(r)) * |psi(r)|^2 )

       pp.x < pp.SiH4.psi2.in > pp.SiH4.psi2.out

   the resulting sign(psi(r)) * |psi(r)|^2 are written to files
   `psi2.SiH4_K001_B0*.xsf`


3. plot one of generated XSF files with `xcrysden`, e.g.:

       xcrysden --xsf psi2.SiH4_K001_B006.xsf

    and make a fancy display of molecular-orbital. 
    Then save the current displayed state via
    the xcrysden's menu *File-->Save Current State* (say that you save
    it as `MO-state.xcrysden`). Now try this with another orbital, e.g.:

       xcrysden --xsf psi2.SiH4_K001_B005.xsf --script MO-state.xcrysden
 
