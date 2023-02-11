Vector Load and Store Instructions
==================================

vle<eew>
--------

Vector unit-stride loads instructions.

::

  vle8.v   vd, (rs1), vm       # 8-bit unit-stride load with width == '000'
  vle16.v   vd, (rs1), vm       # 16-bit unit-stride load with width == '101'
  vle32.v   vd, (rs1), vm       # 32-bit unit-stride load with width == '110'
  vle64.v   vd, (rs1), vm       # 64-bit unit-stride load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |00   |vm|00000|rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vlse<eew>
---------

Vector strided loads instructions.

::

  vlse8.v    vd, (rs1), rs2, vm       # 8-bit strided load with width == '000'
  vlse16.v    vd, (rs1), rs2, vm       # 16-bit strided load with width == '101'
  vlse32.v    vd, (rs1), rs2, vm       # 32-bit strided load with width == '110'
  vlse64.v    vd, (rs1), rs2, vm       # 64-bit strided load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |10   |vm|rs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vluxei<eew>
-----------

Vector indexed-unordered load instructions.

::

  vluxei8.v    vd, (rs1), vs2, vm       # unordered 8-bit indexed load with width == '000'
  vluxei16.v    vd, (rs1), vs2, vm       # unordered 16-bit indexed load with width == '101'
  vluxei32.v    vd, (rs1), vs2, vm       # unordered 32-bit indexed load with width == '110'
  vluxei64.v    vd, (rs1), vs2, vm       # unordered 64-bit indexed load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |01   |vm|vs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vloxei<eew>
-----------

Vector indexed-ordered load instructions.

::

  vloxei8.v    vd, (rs1), vs2, vm         # ordered  8-bit indexed load with width == '000'
  vloxei16.v    vd, (rs1), vs2, vm         # ordered  16-bit indexed load with width == '101'
  vloxei32.v    vd, (rs1), vs2, vm         # ordered  32-bit indexed load with width == '110'
  vloxei64.v    vd, (rs1), vs2, vm         # ordered  64-bit indexed load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |11   |vm|vs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vse<eew>
--------

Vector unit-stride stores instructions.

::

  vse8.v   vs3, (rs1), vm       # 8-bit unit-stride store with width == '000'
  vse16.v   vs3, (rs1), vm       # 16-bit unit-stride store with width == '101'
  vse32.v   vs3, (rs1), vm       # 32-bit unit-stride store with width == '110'
  vse64.v   vs3, (rs1), vm       # 64-bit unit-stride store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |00   |vm|00000|rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsse<eew>
---------

Vector strided stores instructions.

::

  vsse8.v    vs3, (rs1), rs2, vm       # 8-bit strided store with width == '000'
  vsse16.v    vs3, (rs1), rs2, vm       # 16-bit strided store with width == '101'
  vsse32.v    vs3, (rs1), rs2, vm       # 32-bit strided store with width == '110'
  vsse64.v    vs3, (rs1), rs2, vm       # 64-bit strided store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |10   |vm|rs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsuxei<eew>
-----------

Vector indexed-unordered store instructions.

::

  vsuxei8.v    vs3, (rs1), vs2, vm       # unordered 8-bit indexed store with width == '000'
  vsuxei16.v    vs3, (rs1), vs2, vm       # unordered 16-bit indexed store with width == '101'
  vsuxei32.v    vs3, (rs1), vs2, vm       # unordered 32-bit indexed store with width == '110'
  vsuxei64.v    vs3, (rs1), vs2, vm       # unordered 64-bit indexed store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |01   |vm|vs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsoxei<eew>
-----------

Vector indexed-ordered store instructions.

::

  vsoxei8.v    vs3, (rs1), vs2, vm       # ordered 8-bit indexed store with width == '000'
  vsoxei16.v    vs3, (rs1), vs2, vm       # ordered 16-bit indexed store with width == '101'
  vsoxei32.v    vs3, (rs1), vs2, vm       # ordered 32-bit indexed store with width == '110'
  vsoxei64.v    vs3, (rs1), vs2, vm       # ordered 64-bit indexed store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |11   |vm|vs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

