Vector Integer Instructions
===========================

vadd
----

Vector single-width integer add.

::

  vadd.vv vd, vs2, vs1, vm
  vadd.vx vd, vs2, rs1, vm
  vadd.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000000|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000000|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000000|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vsub
----

Vector single-width integer subtract.

::

  vsub.vv vd, vs2, vs1, vm
  vsub.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000010|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000010|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vrsub
-----

Integer reverse subtract, vd[i] = x[rs1](imm) - vs2[i].

::

  vrsub.vx vd, vs2, rs1, vm
  vrsub.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000011|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000011|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vminu
-----

Unsigned minimum.

::

  vminu.vv vd, vs2, vs1, vm
  vminu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000100|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000100|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmin
----

Signed minimum.

::

  vmin.vv vd, vs2, vs1, vm
  vmin.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000101|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000101|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmaxu
-----

Unsigned maximum.

::

  vmaxu.vv vd, vs2, vs1, vm
  vmaxu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000110|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000110|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmax
----

Signed maximum.

::

  vmax.vv vd, vs2, vs1, vm
  vmax.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000111|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000111|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vand
----

Bitwise logical and.

::

  vand.vv vd, vs2, vs1, vm
  vand.vx vd, vs2, rs1, vm
  vand.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001001|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001001|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001001|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vor
---

Bitwise logical or.

::

  vor.vv vd, vs2, vs1, vm
  vor.vx vd, vs2, rs1, vm
  vor.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001010|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001010|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001010|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vxor
----

Bitwise logical xor.

::

  vxor.vv vd, vs2, vs1, vm
  vxor.vx vd, vs2, rs1, vm
  vxor.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001011|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001011|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|001011|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vadc
----

Vector integer add-with-carry instruction to produce sum with carry.

::

  # vd[i] = vs2[i] + vs1[i] + v0.mask[i]
  vadc.vvm vd, vs2, vs1, v0
  # vd[i] = vs2[i] + x[rs1] + v0.mask[i]
  vadc.vxm vd, vs2, rs1, v0
  # vd[i] = vs2[i] + imm + v0.mask[i]
  vadc.vim vd, vs2, imm, v0

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmadc
-----

Vector integer add-with-carry instruction to produce carry out in mask register format.

::

  # vd.mask[i] = carry_out(vs2[i] + vs1[i] + v0.mask[i])
  vmadc.vvm vd, vs2, vs1, v0 # Vector-vector
  # vd.mask[i] = carry_out(vs2[i] + x[rs1] + v0.mask[i])
  vmadc.vxm vd, vs2, rs1, v0 # Vector-scalar
  # vd.mask[i] = carry_out(vs2[i] + imm + v0.mask[i])
  vmadc.vim vd, vs2, imm, v0 # Vector-immediate
  # vd.mask[i] = carry_out(vs2[i] + vs1[i])
  vmadc.vv vd, vs2, vs1 # Vector-vector, no carry-in
  # vd.mask[i] = carry_out(vs2[i] + x[rs1])
  vmadc.vx vd, vs2, rs1 # Vector-scalar, no carry-in
  # vd.mask[i] = carry_out(vs2[i] + imm)
  vmadc.vi vd, vs2, imm # Vector-immediate, no carry-in

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010001|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010001|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010001|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vsbc
----

Vector integer subtract-with-borrow instruction to produce difference with borrow.

::

  # vd[i] = vs2[i] - vs1[i] - v0.mask[i]
  vsbc.vvm vd, vs2, vs1, v0 # Vector-vector
  # vd[i] = vs2[i] - x[rs1] - v0.mask[i]
  vsbc.vxm vd, vs2, rs1, v0 # Vector-scalar

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vzext/vsext
-----------

Vector integer extension to zero- or sign- extend a source vector integer operand with EEW less than SEW to fill SEW-sized elements in the destination.

::

  vzext.vf2 vd, vs2, vm # Zero-extend SEW/2 source to SEW destination, with vs1 = '00110'.
  vsext.vf2 vd, vs2, vm # Sign-extend SEW/2 source to SEW destination, with vs1 = '00111'.
  vzext.vf4 vd, vs2, vm # Zero-extend SEW/4 source to SEW destination, with vs1 = '00100'.
  vsext.vf4 vd, vs2, vm # Sign-extend SEW/4 source to SEW destination, with vs1 = '00101'.
  vzext.vf8 vd, vs2, vm # Zero-extend SEW/8 source to SEW destination, with vs1 = '00010'.
  vsext.vf8 vd, vs2, vm # Sign-extend SEW/8 source to SEW destination, with vs1 = '00011'.

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmsbc
-----

Vector integer subtract-with-borrow instruction to borrow out in mask register format.

::

  # vd.mask[i] = borrow_out(vs2[i] - vs1[i] - v0.mask[i])
 vmsbc.vvm vd, vs2, vs1, v0 # Vector-vector
 # vd.mask[i] = borrow_out(vs2[i] - x[rs1] - v0.mask[i])
 vmsbc.vxm vd, vs2, rs1, v0 # Vector-scalar
 # vd.mask[i] = borrow_out(vs2[i] - vs1[i])
 vmsbc.vv vd, vs2, vs1 # Vector-vector, no borrow-in
 # vd.mask[i] = borrow_out(vs2[i] - x[rs1])
 vmsbc.vx vd, vs2, rs1 # Vector-scalar, no borrow-in

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010011|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010011|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmseq
-----

Integer compare instruction to set bit if equal.

::

  vmseq.vv vd, vs2, vs1, vm
  vmseq.vx vd, vs2, rs1, vm
  vmseq.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011000|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011000|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011000|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmsne
-----

Integer compare instruction to set bit if not equal.

::

  vmsne.vv vd, vs2, vs1, vm
  vmsne.vx vd, vs2, rs1, vm
  vmsne.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011001|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011001|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011001|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmsltu
------

Integer compare instruction to set bit if less than, unsigned.

::

  vmsltu.vv vd, vs2, vs1, vm
  vmsltu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011010|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011010|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmslt
-----

Integer compare instruction to set bit if less than, signed.

::

  vmslt.vv vd, vs2, vs1, vm
  vmslt.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011011|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011011|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmsleu
------

Integer compare instruction to set bit if less than or equal, unsigned.

::

  vmsleu.vv vd, vs2, vs1, vm
  vmsleu.vx vd, vs2, rs1, vm
  vmsleu.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011100|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011100|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011100|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmsle
-----

Integer compare instruction to set bit if less than or equal, signed.

::

  vmsle.vv vd, vs2, vs1, vm
  vmsle.vx vd, vs2, rs1, vm
  vmsle.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011101|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011101|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011101|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmsgtu
------

Integer compare instruction to set bit if greater than, unsigned.

::

  vmsgtu.vx vd, vs2, rs1, vm
  vmsgtu.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011110|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011110|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmsgt
-----

Integer compare instruction to set bit if greater than, signed.

::

  vmsgt.vx vd, vs2, rs1, vm
  vmsgt.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011111|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011111|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vdivu
-----

Unsigned divide.

::

  vdivu.vv vd, vs2, vs1, vm
  vdivu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100000|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100000|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vdiv
----

Signed divide.

::

  vdiv.vv vd, vs2, vs1, vm
  vdiv.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100001|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100001|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vremu
-----

Unsigned remainder.

::

  vremu.vv vd, vs2, vs1, vm
  vremu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100010|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100010|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vrem
----

Signed remainder.

::

  vrem.vv vd, vs2, vs1, vm
  vrem.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100011|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100011|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmulhu
------

Unsigned multiply, returning low bits of product.

::

  vmulhu.vv vd, vs2, vs1, vm
  vmulhu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100100|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100100|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vsll
----

Logical shift left.

::

  vsll.vv vd, vs2, vs1, vm
  vsll.vx vd, vs2, rs1, vm
  vsll.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100101|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100101|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100101|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmul
----

Signed multiply, returning low bits of product.

::

  vmul.vv vd, vs2, vs1, vm
  vmul.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100101|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100101|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmulhsu
-------

Signed(vs2)-Unsigned multiply, returning high bits of product.

::

  vmulhsu.vv vd, vs2, vs1, vm
  vmulhsu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100110|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100110|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmulh
-----

Signed multiply, returning high bits of product.

::

  vmulh.vv vd, vs2, vs1, vm
  vmulh.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100111|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|100111|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vsrl
----

Logical shift right.

::

  vsrl.vv vd, vs2, vs1, vm
  vsrl.vx vd, vs2, rs1, vm
  vsrl.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101000|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101000|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101000|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vsra
----

Arithmetic shift right.

::

  vsra.vv vd, vs2, vs1, vm
  vsra.vx vd, vs2, rs1, vm
  vsra.vi vd, vs2, imm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101001|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101001|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101001|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmadd
-----

Integer multiply-add, overwrite multiplicand.

::

  vmadd.vv vd, vs2, vs1, vm
  vmadd.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101001|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101001|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vnmsub
------

Integer multiply-sub, overwrite multiplicand.

::

  vnmsub.vv vd, vs2, vs1, vm
  vnmsub.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101011|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101011|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vnsrl
-----

Narrowing shift right logical, SEW = (2*SEW) >> SEW.

::

  vnsrl.wv vd, vs2, vs1, vm
  vnsrl.wx vd, vs2, rs1, vm
  vnsrl.wi vd, vs2, uimm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101100|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101100|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101100|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vnsra
-----

Narrowing shift right arithmetic, SEW = (2*SEW) >> SEW.

::

  vnsra.wv vd, vs2, vs1, vm
  vnsra.wx vd, vs2, rs1, vm
  vnsra.wi vd, vs2, uimm, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101101|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101101|vm|vs2  |rs1     |100  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101101|vm|vs2  |imm[4:0]|011  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vmacc
-----

Integer multiply-add, overwrite addend.

::

  vmacc.vv vd, vs2, vs1, vm
  vmacc.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101101|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101101|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vnmsac
------

Integer multiply-sub, overwrite minuend.

::

  vnmsac.vv vd, vs2, vs1, vm
  vnmsac.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101111|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|101111|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwaddu
------

Widening unsigned integer add, 2*SEW = SEW + SEW.

::

  vwaddu.vv vd, vs2, vs1, vm
  vwaddu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110000|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110000|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwadd
-----

Widening signed integer add, 2*SEW = SEW + SEW.

::

  vwadd.vv vd, vs2, vs1, vm
  vwadd.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110001|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110001|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwsubu
------

Widening unsigned integer subtract, 2*SEW = SEW - SEW.

::

  vwsubu.vv vd, vs2, vs1, vm
  vwsubu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110010|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110010|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwsub
-----

Widening signed integer subtract, 2*SEW = SEW - SEW.

::

  vwsub.vv vd, vs2, vs1, vm
  vwsub.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110011|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110011|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwaddu.w
--------

Widening unsigned integer add, 2*SEW = 2*SEW + SEW.

::

  vwaddu.wv vd, vs2, vs1, vm
  vwaddu.wx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110100|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110100|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwadd.w
-------

Widening signed integer add, 2*SEW = 2*SEW + SEW.

::

  vwadd.wv vd, vs2, vs1, vm
  vwadd.wx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110101|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110101|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwsubu.w
--------

Widening unsigned integer subtract, 2*SEW = 2*SEW - SEW.

::

  vwsubu.wv vd, vs2, vs1, vm
  vwsubu.wx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110110|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110110|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwsub.w
-------

Widening signed integer subtract, 2*SEW = 2*SEW - SEW.

::

  vwsub.wv vd, vs2, vs1, vm
  vwsub.wx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110111|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110111|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwmulu
------

Widening unsigned-integer multiply.

::

  vwmulu.vv vd, vs2, vs1, vm
  vwmulu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111000|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111000|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwmulsu
-------

Widening signed(vs2)-unsigned integer multiply.

::

  vwmulsu.vv vd, vs2, vs1, vm
  vwmulsu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111010|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111010|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwmul
-----

Widening signed-integer multiply.

::

  vwmul.vv vd, vs2, vs1, vm
  vwmul.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111011|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111011|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwmaccu
-------

Widening unsigned-integer multiply-add, overwrite addend.

::

  vwmaccu.vv vd, vs2, vs1, vm
  vwmaccu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111100|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111100|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwmacc
------

 Widening signed-integer multiply-add, overwrite addend.

::

  vwmacc.vv vd, vs2, vs1, vm
  vwmacc.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111101|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111101|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwmaccus
--------

Widening unsigned-signed-integer multiply-add, overwrite addend.

::

  vwmaccus.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111110|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwmaccsu
--------

Widening signed-unsigned-integer multiply-add, overwrite addend.

::

  vwmaccsu.vv vd, vs2, vs1, vm
  vwmaccsu.vx vd, vs2, rs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111111|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|111111|vm|vs2  |rs1     |110  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

