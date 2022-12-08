Configuration-Setting Instructions
==================================

vsetvli
-------

Set the vtype and vl CSRs based on given AVL and vtype, and write the new value of vl into rd. 
AVL is encoded in the rs1 and rd fields to update vl as follows:

  1. rs1 != x0:              AVL is equal to value in x[rs1], vl is updated accordingly.
  #. rs1 == x0 and rd != x0: AVL is equal to ~0, vl is set to VLMAX.
  #. res == x0 and rd == x0: AVL is equal to value in vl register, vl remains unchanged.

The new vtype setting is encoded in the immediate fields where SEW and LMUL can be assigned.

::

  vsetvli rd, rs1, vtypei       # rd = new vl, rs1 = AVL, vtypei = new vtype setting

+--+----------+----------+-----+----+-------+
|31|30-20     |19-15     |14-12|11-7|6-0    |
+--+----------+----------+-----+----+-------+
|0 |zimm[10:0]|rs1       |111  |rd  |1010111|
+--+----------+----------+-----+----+-------+


vsetivli
--------

Set the vtype and vl CSRs based on given AVL and vtype, and write the new value of vl into rd. 
AVL is encoded as a 5-bit zero-extended immediate (0—31). 
The new vtype setting is encoded in the immediate fields where SEW and LMUL can be assigned.

::

  vsetivli rd, uimm, vtypei       # rd = new vl, uimm = AVL, vtypei = new vtype setting

+--+--+----------+----------+-----+----+-------+
|31|30|29-20     |19-15     |14-12|11-7|6-0    |
+--+--+----------+----------+-----+----+-------+
|1 |1 |zimm[9:0] |uimm[4:0] |111  |rd  |1010111|
+--+--+----------+----------+-----+----+-------+


vsetvl
------

Set the vtype and vl CSRs based on given AVL and vtype, and write the new value of vl into rd. 
AVL is encoded in the rs1 and rd fields to update vl as follows:

  1. rs1 != x0:              AVL is equal to value in x[rs1], vl is updated accordingly.
  #. rs1 == x0 and rd != x0: AVL is equal to ~0, vl is set to VLMAX.
  #. res == x0 and rd == x0: AVL is equal to value in vl register, vl remains unchanged.
  
The new vtype setting is encoded in the rs2 register where SEW and LMUL can be assigned.

::

  vsetvl  rd, rs1, rs2       # rd = new vl, rs1 = AVL, rs2 = new vtype value

+--+------+----------+----------+-----+----+-------+
|31|30-25 |24-20     |19-15     |14-12|11-7|6-0    |
+--+------+----------+----------+-----+----+-------+
|1 |000000|rs2       |rs1       |111  |rd  |1010111|
+--+------+----------+----------+-----+----+-------+

