Vector Permutation Instructions
===============================

vrgather
--------

Reads elements from a rst source vector register group at locations given by a second source vector register group.

::

  vrgather.vv vd, vs2, vs1, vm
  vrgather.vx vd, vs2, rs1, vm
  vrgather.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001100|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001100|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001100|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vslideup
--------

Moves elements up a vector register group.

::

  vslideup.vx vd, vs2, rs1, vm
  vslideup.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001110|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001110|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vslide1up
---------

Places the x register argument at location 0 of the destination vector register group, vd[0]=x[rs1], vd[i+1] = vs2[i].

::

  vslide1up.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001110|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfslide1up
----------

Places the x register argument at location 0 of the destination vector register group, vd[0] = f[rs1], vd[i+1] = vs2[i].

::

  vfslide1up.vf vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001110|vm|vs2  |rs1     |101  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vrgatherei16
------------

Similar to vrgather, except to use SEW/LMUL for the data in vs2 but EEW=16 and EMUL = (16/SEW)*LMUL for the indices in vs1.

::

  vrgatherei16.vv vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001110|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vslidedown
----------

Moves elements down a vector register group.

::

  vslidedown.vx vd, vs2, rs1, vm
  vslidedown.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001111|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001111|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vslide1down
-----------

Copies the rst vl-1 active elements values from index i+1 in the source vector register group to index i in the destination vector register group, vd[i] = vs2[i+1], vd[vl-1] = x[rs1].

::

  vslide1down.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001111|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfslide1down
------------

Copies the rst vl-1 active elements values from index i+1 in the source vector register group to index i in the destination vector register group,  vd[i] = vs2[i+1], vd[vl-1] = f[rs1].

::

  vfslide1down.vf vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001111|vm|vs2  |rs1     |101  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmv.x.s
-------

Copies a single SEW-wide element from index 0 of the source vector register to a destination integer register.

::

  vmv.x.s rd, vs2 # x[rd] = vs2[0] (vs1=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |00000   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfmv.f.s
--------

Copies a single SEW-wide element from index 0 of the source vector register to a destination scalar floating-point register.


::

  vfmv.f.s rd, vs2 # f[rd] = vs2[0] (rs1=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |00000   |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmv.s.x
-------

Copies the scalar integer register to element 0 of the destination vector register. 

::

  vmv.s.x vd, rs1 # vd[0] = x[rs1] (vs2=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|00000|vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfmv.s.f
--------

Copies the scalar floating-point register to element 0 of the destination vector register.

::

  vfmv.s.f vd, rs1 # vd[0] = f[rs1] (vs2=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|00000|rs1     |101  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmerge/vmv
----------

Combines two source operands based on a mask, or copies a source operand to a vector register group if unmasked.

::

  vmerge.vvm vd, vs2, vs1, v0 # vd[i] = v0.mask[i] ? vs1[i] : vs2[i]
  vmerge.vxm vd, vs2, rs1, v0 # vd[i] = v0.mask[i] ? x[rs1] : vs2[i]
  vmerge.vim vd, vs2, imm, v0 # vd[i] = v0.mask[i] ? imm : vs2[i]

  vmv.v.v vd, vs1 # vd[i] = vs1[i]
  vmv.v.x vd, rs1 # vd[i] = x[rs1]
  vmv.v.i vd, imm # vd[i] = imm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010111|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010111|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010111|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vcompress
---------

Allows elements selected by a vector mask register from a source vector register group to be packed into contiguous elements at the start of the destination vector register group.

::

  vcompress.vm vd, vs2, vs1 # Compress into vd elements of vs2 where vs1 is enabled

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010111|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfmerge/vfmv
------------

Combines two source operands based on a mask, or copies a source operand to a vector register group if unmasked.

::

  vfmerge.vfm vd, vs2, rs1, v0 # vd[i] = v0.mask[i] ? f[rs1] : vs2[i]

  vfmv.v.f vd, rs1 # vd[i] = f[rs1]

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010111|vm|vs2  |rs1     |101  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

