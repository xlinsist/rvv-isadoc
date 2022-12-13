Vector Mask Instructions
========================

vpopc
-----------

Vector count population in mask. Counts the number of mask elements of the active elements of the vector source mask register.
'vpopc' is an alias of 'vcpop'.

::

  vcpop.m rd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |10000   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+


vfirst
------

Find-rst-set mask bit. Finds the lowest-numbered active element of the source mask vector that has the value 1 and writes that element's index to a GPR. If no active element has the value 1, -1 is written to the GPR.

::

  vfirst.m rd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |10001   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+
vmsbf
-----

Set-before-rst mask bit. Takes a mask register as input and writes results to a mask register.

::

  vmsbf.m vd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010100|vm|vs2  |00001   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+


vmsof
-----

Set-only-rst mask bit. It is similar to 'vmsbf', except it only sets the rst element with a bit set, if any.

::

  vmsof.m vd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010100|vm|vs2  |00010   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmsif
-----

Set-including-rst mask bit. It is similar to 'vmsbf', except it also includes the element with a set bit.

::

  vmsif.m vd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010100|vm|vs2  |00011   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

viota
-----

Reads a source vector mask register and writes to each element of the destination vector register 

::

   viota.m vd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010100|vm|vs2  |10000   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vid
---

Vector element index instruction. Writes each element's index to the destination vector register group, from 0 to vl-1.

::

  vid.v vd, vm # Write element ID to destination.

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010100|vm|vs2  |10001   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+


vmandnot
--------

Vector mask-register logical operation,  vd.mask[i] = vs2.mask[i] && !vs1.mask[i].
The previous assembler mnemonic 'vmandnot' have been changed to 'vmandn' to be consistent with the equivalent scalar instructions. The old mnemonic can be retained as assembler aliases for compatibility.

::

  vmandnot.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011000|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmand
-----

Vector mask-register logical operation,  vd.mask[i] = vs2.mask[i] && vs1.mask[i].

::

  vmand.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011001|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmor
----

Vector mask-register logical operation,  vd.mask[i] = vs2.mask[i] || vs1.mask[i].

::

  vmor.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011010|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmxor
-----

Vector mask-register logical operation,  vd.mask[i] = vs2.mask[i] ^^ vs1.mask[i].

::

  vmxor.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011011|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmornot
-------

Vector mask-register logical operation,  vd.mask[i] = vs2.mask[i] || !vs1.mask[i].
The previous assembler mnemonic 'vmornot' have been changed to 'vmorn' to be consistent with the equivalent scalar instructions. The old mnemonic can be retained as assembler aliases for compatibility.

::

  vmornot.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011100|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmnand
------

Vector mask-register logical operation,  vd.mask[i] = !(vs2.mask[i] && vs1.mask[i]).

::

  vmnand.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011101|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmnor
-----

Vector mask-register logical operation,  vd.mask[i] = !(vs2.mask[i] || vs1.mask[i]).

::

  vmnor.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011110|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vmxnor
------

Vector mask-register logical operation,  vd.mask[i] = !(vs2.mask[i] ^^ vs1.mask[i]).

::

  vmxnor.mm vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|011111|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

