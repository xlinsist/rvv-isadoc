Vector Load and Store Instructions
==================================

vle<eew>
--------

Vector unit-stride load instructions.

::

  vle8.v   vd, (rs1), vm # 8-bit unit-stride load with width == '000'
  vle16.v   vd, (rs1), vm # 16-bit unit-stride load with width == '101'
  vle32.v   vd, (rs1), vm # 32-bit unit-stride load with width == '110'
  vle64.v   vd, (rs1), vm # 64-bit unit-stride load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |00   |vm|00000|rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vlm
---

Vector unit-stride mask load.

::

  vlm.v vd, (rs1) # Load byte vector of length ceil(vl/8)


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |00   |vm|01011|rs1  |000  |vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vlse<eew>
---------

Vector strided load instructions.

::

  vlse8.v    vd, (rs1), rs2, vm # 8-bit strided load with width == '000'
  vlse16.v    vd, (rs1), rs2, vm # 16-bit strided load with width == '101'
  vlse32.v    vd, (rs1), rs2, vm # 32-bit strided load with width == '110'
  vlse64.v    vd, (rs1), rs2, vm # 64-bit strided load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |10   |vm|rs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vluxei<eew>
-----------

Vector indexed-unordered load instructions.

::

  vluxei8.v    vd, (rs1), vs2, vm # unordered 8-bit indexed load with width == '000'
  vluxei16.v    vd, (rs1), vs2, vm # unordered 16-bit indexed load with width == '101'
  vluxei32.v    vd, (rs1), vs2, vm # unordered 32-bit indexed load with width == '110'
  vluxei64.v    vd, (rs1), vs2, vm # unordered 64-bit indexed load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |01   |vm|vs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vloxei<eew>
-----------

Vector indexed-ordered load instructions.

::

  vloxei8.v    vd, (rs1), vs2, vm   # ordered  8-bit indexed load with width == '000'
  vloxei16.v    vd, (rs1), vs2, vm   # ordered  16-bit indexed load with width == '101'
  vloxei32.v    vd, (rs1), vs2, vm   # ordered  32-bit indexed load with width == '110'
  vloxei64.v    vd, (rs1), vs2, vm   # ordered  64-bit indexed load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |11   |vm|vs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vle<eew>ff
----------

Vector unit-stride fault-only-first loads.

::

  vle8ff.v    vd, (rs1), vm   # 8-bit unit-stride fault-only-first load with width == '000'
  vle16ff.v    vd, (rs1), vm   # 16-bit unit-stride fault-only-first load with width == '101'
  vle32ff.v    vd, (rs1), vm   # 32-bit unit-stride fault-only-first load with width == '110'
  vle64ff.v    vd, (rs1), vm   # 64-bit unit-stride fault-only-first load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |00   |vm|10000|rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vlseg<nf>e<eew>
---------------

Unit-stride segment loads.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vlseg<nf>e8.v    vd, (rs1), vm   # 8-bit unit-stride segment load with width == '000'
  vlseg<nf>e16.v    vd, (rs1), vm   # 16-bit unit-stride segment load with width == '101'
  vlseg<nf>e32.v    vd, (rs1), vm   # 32-bit unit-stride segment load with width == '110'
  vlseg<nf>e64.v    vd, (rs1), vm   # 64-bit unit-stride segment load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |00   |vm|00000|rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vlsseg<nf>e<eew>
----------------

Strided segment loads.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vlsseg<nf>e8.v vd, (rs1), rs2, vm   # 8-bit strided segment load with width == '000'
  vlsseg<nf>e16.v vd, (rs1), rs2, vm   # 16-bit strided segment load with width == '101'
  vlsseg<nf>e32.v vd, (rs1), rs2, vm   # 32-bit strided segment load with width == '110'
  vlsseg<nf>e64.v vd, (rs1), rs2, vm   # 64-bit strided segment load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |10   |vm|rs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vluxseg<nf>ei<eew>
------------------

Indexed-unordered segment loads.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vluxseg<nf>ei8.v vd, (rs1), vs2, vm   # 8-bit indexed-unordered segment load with width == '000'
  vluxseg<nf>ei16.v vd, (rs1), vs2, vm   # 16-bit indexed-unordered segment load with width == '101'
  vluxseg<nf>ei32.v vd, (rs1), vs2, vm   # 32-bit indexed-unordered segment load with width == '110'
  vluxseg<nf>ei64.v vd, (rs1), vs2, vm   # 64-bit indexed-unordered segment load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |01   |vm|vs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vloxseg<nf>ei<eew>
------------------

Indexed-ordered segment loads.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vloxseg<nf>ei8.v vd, (rs1), vs2, vm     # 8-bit indexed-ordered segment load with width == '000'
  vloxseg<nf>ei16.v vd, (rs1), vs2, vm     # 16-bit indexed-ordered segment load with width == '101'
  vloxseg<nf>ei32.v vd, (rs1), vs2, vm     # 32-bit indexed-ordered segment load with width == '110'
  vloxseg<nf>ei64.v vd, (rs1), vs2, vm     # 64-bit indexed-ordered segment load with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |11   |vm|vs2  |rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vl<nf>re<eew>
-------------

Whole register load instructions.

In whole register load and store instructions, the three-bit nf[2:0] field encodes how many vector registers to load and store using the NFIELDS encoding, which is presented in instructions as <nf>.The encoded number of registers must be a power of 2 and the vector register numbers must be aligned as with a vector register group.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
011      4    
111      8   
=======  ====

::

  # <eew>=8, width == '000'; <eew>=16, width == '101'; <eew>=32, width == '110'; <eew>=64, width == '111';
        
  vl1r.v v3, (a0) # Pseudoinstruction equal to vl1re8.v

  vl1re8.v v3, (a0) # Load v3 with VLEN/8 bytes held at address in a0
  vl1re16.v v3, (a0) # Load v3 with VLEN/16 halfwords held at address in a0
  vl1re32.v v3, (a0) # Load v3 with VLEN/32 words held at address in a0
  vl1re64.v v3, (a0) # Load v3 with VLEN/64 doublewords held at address in a0

  vl2r.v v2, (a0) # Pseudoinstruction equal to vl2re8.v v2, (a0)
  vl2re8.v v2, (a0) # Load v2-v3 with 2*VLEN/8 bytes from address in a0
  vl2re16.v v2, (a0) # Load v2-v3 with 2*VLEN/16 halfwords held at address in a0
  vl2re32.v v2, (a0) # Load v2-v3 with 2*VLEN/32 words held at address in a0
  vl2re64.v v2, (a0) # Load v2-v3 with 2*VLEN/64 doublewords held at address in a0

  vl4r.v v4, (a0) # Pseudoinstruction equal to vl4re8.v
  vl4re8.v v4, (a0) # Load v4-v7 with 4*VLEN/8 bytes from address in a0
  vl4re16.v v4, (a0)
  vl4re32.v v4, (a0)
  vl4re64.v v4, (a0)

  vl8r.v v8, (a0) # Pseudoinstruction equal to vl8re8.v
  vl8re8.v v8, (a0) # Load v8-v15 with 8*VLEN/8 bytes from address in a0
  vl8re16.v v8, (a0)
  vl8re32.v v8, (a0)
  vl8re64.v v8, (a0)


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |00   |vm|01000|rs1  |width|vd  |0000111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vse<eew>
--------

Vector unit-stride store instructions.

::

  vse8.v   vs3, (rs1), vm # 8-bit unit-stride store with width == '000'
  vse16.v   vs3, (rs1), vm # 16-bit unit-stride store with width == '101'
  vse32.v   vs3, (rs1), vm # 32-bit unit-stride store with width == '110'
  vse64.v   vs3, (rs1), vm # 64-bit unit-stride store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |00   |vm|00000|rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsm
---

Vector unit-stride mask store.

::

  vsm.v vs3, (rs1) # Store byte vector of length ceil(vl/8)


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |00   |vm|01011|rs1  |000  |vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsse<eew>
---------

Vector strided store instructions.

::

  vsse8.v    vs3, (rs1), rs2, vm # 8-bit strided store with width == '000'
  vsse16.v    vs3, (rs1), rs2, vm # 16-bit strided store with width == '101'
  vsse32.v    vs3, (rs1), rs2, vm # 32-bit strided store with width == '110'
  vsse64.v    vs3, (rs1), rs2, vm # 64-bit strided store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |10   |vm|rs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsuxei<eew>
-----------

Vector indexed-unordered store instructions.

::

  vsuxei8.v    vs3, (rs1), vs2, vm # unordered 8-bit indexed store with width == '000'
  vsuxei16.v    vs3, (rs1), vs2, vm # unordered 16-bit indexed store with width == '101'
  vsuxei32.v    vs3, (rs1), vs2, vm # unordered 32-bit indexed store with width == '110'
  vsuxei64.v    vs3, (rs1), vs2, vm # unordered 64-bit indexed store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |01   |vm|vs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsoxei<eew>
-----------

Vector indexed-ordered store instructions.

::

  vsoxei8.v    vs3, (rs1), vs2, vm # ordered 8-bit indexed store with width == '000'
  vsoxei16.v    vs3, (rs1), vs2, vm # ordered 16-bit indexed store with width == '101'
  vsoxei32.v    vs3, (rs1), vs2, vm # ordered 32-bit indexed store with width == '110'
  vsoxei64.v    vs3, (rs1), vs2, vm # ordered 64-bit indexed store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|000  |0  |11   |vm|vs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsseg<nf>e<eew>
---------------

Unit-stride segment stores.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vsseg<nf>e8.v    vd, (rs1), vm   # 8-bit unit-stride segment store with width == '000'
  vsseg<nf>e16.v    vd, (rs1), vm   # 16-bit unit-stride segment store with width == '101'
  vsseg<nf>e32.v    vd, (rs1), vm   # 32-bit unit-stride segment store with width == '110'
  vsseg<nf>e64.v    vd, (rs1), vm   # 64-bit unit-stride segment store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |00   |vm|00000|rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vssseg<nf>e<eew>
----------------

Strided segment stores.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vssseg<nf>e8.v vs3, (rs1), rs2, vm   # 8-bit strided segment store with width == '000'
  vssseg<nf>e16.v vs3, (rs1), rs2, vm   # 16-bit strided segment store with width == '101'
  vssseg<nf>e32.v vs3, (rs1), rs2, vm   # 32-bit strided segment store with width == '110'
  vssseg<nf>e64.v vs3, (rs1), rs2, vm   # 64-bit strided segment store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |10   |vm|rs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsuxseg<nf>ei<eew>
------------------

Indexed-unordered segment stores.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vsuxseg<nf>ei8.v vs3, (rs1), vs2, vm   # 8-bit indexed-unordered segment store with width == '000'
  vsuxseg<nf>ei16.v vs3, (rs1), vs2, vm   # 16-bit indexed-unordered segment store with width == '101'
  vsuxseg<nf>ei32.v vs3, (rs1), vs2, vm   # 32-bit indexed-unordered segment store with width == '110'
  vsuxseg<nf>ei64.v vs3, (rs1), vs2, vm   # 64-bit indexed-unordered segment store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |01   |vm|vs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vsoxseg<nf>ei<eew>
------------------

Indexed-ordered segment stores.

In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
010      3   
011      4   
100      5   
101      6   
110      7   
111      8   
=======  ====

::

  vsoxseg<nf>ei8.v vs3, (rs1), vs2, vm    # 8-bit indexed-ordered segment store with width == '000'
  vsoxseg<nf>ei16.v vs3, (rs1), vs2, vm    # 16-bit indexed-ordered segment store with width == '101'
  vsoxseg<nf>ei32.v vs3, (rs1), vs2, vm    # 32-bit indexed-ordered segment store with width == '110'
  vsoxseg<nf>ei64.v vs3, (rs1), vs2, vm    # 64-bit indexed-ordered segment store with width == '111'


+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |11   |vm|vs2  |rs1  |width|vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

vs<nf>r
-------

Whole register store instructions.

In whole register load and store instructions, the three-bit nf[2:0] field encodes how many vector registers to load and store using the NFIELDS encoding, which is presented in instructions as <nf>.The encoded number of registers must be a power of 2 and the vector register numbers must be aligned as with a vector register group.

=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
011      4    
111      8   
=======  ====

::

  vs1r.v v3, (a1) # Store v3 to address in a1
  vs2r.v v2, (a1) # Store v2-v3 to address in a1
  vs4r.v v4, (a1) # Store v4-v7 to address in a1
  vs8r.v v8, (a1) # Store v8-v15 to address in a1



+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|nf   |0  |00   |vm|01000|rs1  |000  |vs3 |0100111|
+-----+---+-----+--+-----+-----+-----+----+-------+

