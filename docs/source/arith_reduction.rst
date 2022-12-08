Vector Reduction Instructions
=============================

vredsum
-------

Vector single-width integer reduction instruction, vd[0] = sum( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredsum.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000000|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vredand
-------

Vector single-width integer reduction instruction, vd[0] = and( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredand.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000001|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfredusum
---------

Vector single-width floating-point reduction instruction with unordered sum.

::

  vfredusum.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000001|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vredor
------

Vector single-width integer reduction instruction, vd[0] = or( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredor.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000010|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vredxor
-------

Vector single-width integer reduction instruction, vd[0] = xor( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredxor.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000011|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfredosum
---------

Vector single-width floating-point reduction instruction with ordered sum.

::

  vfredosum.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000011|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vredminu
--------

Vector single-width integer reduction instruction, vd[0] = minu( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredminu.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000100|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vredmin
-------

Vector single-width integer reduction instruction, vd[0] = min( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredmin.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000101|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfredmin
--------

Vector single-width floating-point reduction instruction with minimum value.

::

  vfredmin.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000101|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vredmaxu
--------

Vector single-width integer reduction instruction, vd[0] = maxu( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredmaxu.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000110|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vredmax
-------

Vector single-width integer reduction instruction, vd[0] = max( vs1[0] , vs2[*] ) where [*] denotes all active elements.

::

  vredmax.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000111|vm|vs2  |vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfredmax
--------

Vector single-width floating-point reduction instruction with maximum value.

::

  vfredmax.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|000111|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vwredsumu
---------

Unsigned sum reduction into double-width accumulator.

::

  vwredsumu.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110000|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vwredsum
--------

Signed sum reduction into double-width accumulator.

::

  vwredsum.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110001|vm|vs2  |vs1     |000  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

vfwredusum
----------

Vector widening floating-point reduction instruction with unordered sum.

::

  vfwredusum.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110001|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfwredosum
----------

Vector widening floating-point reduction instruction with ordered sum.

::

  vfwredosum.vs vd, vs2, vs1, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|110011|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

