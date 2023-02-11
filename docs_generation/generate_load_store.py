dict_width = {8: "000", 16: "101", 32: "110", 64: "111"}


class Instruction:
    """Information of an load/store instruction.

    Attributes:
        name: 
        description: 
        funct7: Seven-length bit codes decided whether it is a load or store instruction. "0000111" for load and "0100111" for store.
        bit_int_24_20: Five-length bit codes ranged from bit11 to bit7 in Load and Store instructions' format.
        mop: Two-length bit codes specified memory addressing mode.
             mop="00" for unit-stride, "01" for indexed-unordered, "10" for strided, "11" for indexed-ordered.
        mew: One bit code representing extended memory element width. For regular vector loads and stores, mew='0'.
        nf: Three-length bit codes used for segment load/stores instructions. For regular vector loads and stores, nf='000'.
        usage: A string indicating the usage of the instruction.
    """

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.funct7 = "xxxxxxx"
        self.bit_in_24_20 = "xxxxx"
        self.mop = "xx"
        self.mew = "0"
        self.nf = "000"
        self.usage = ""
        self.width = "width"


def generate_instruction(ins):

    f.write("{title}\n{underline}\n\n".format(
        title=ins.name, underline="-"*len(ins.name)))
    f.write("{}\n\n".format(ins.description))


    # Adds additional description for segment loads and stores.
    if ins.name in ["vlseg<nf>e<eew>", "vlsseg<nf>e<eew>", "vluxseg<nf>ei<eew>", "vloxseg<nf>ei<eew>", "vsseg<nf>e<eew>", "vssseg<nf>e<eew>", "vsuxseg<nf>ei<eew>", "vsoxseg<nf>ei<eew>"]:
        f.write("In segment loads and stores, the three-bit nf[2:0] field in the vector instruction encoding is an unsigned integer that \
contains one less than the number of fields per segment, NFIELDS, which is presented in instructions as <nf>.\n")
        table_segment = """
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
=======  ===="""
        f.write("{}\n\n".format(table_segment))

    # Adds additional description for whole register loads and stores.
    if ins.name in ["vl<nf>re<eew>", "vs<nf>r"]:
        f.write("In whole register load and store instructions, the three-bit nf[2:0] field encodes how many vector registers to load and store using the NFIELDS encoding, which is presented in instructions as <nf>. \
The encoded number of registers must be a power of 2 and the vector register numbers must be aligned as with a vector register group.\n")
        table_segment = """
=======  ====
nf[2:0]  <nf>
=======  ====
000      1   
001      2   
011      4    
111      8   
=======  ===="""
        f.write("{}\n\n".format(table_segment))


    f.write("::\n\n") # Adds instructions' usage and format.
    if ins.name == "vlm":
        f.write("  vlm.v vd, (rs1) # Load byte vector of length ceil(vl/8)\n\n")
    elif ins.name == "vsm":
        f.write("  vsm.v vs3, (rs1) # Store byte vector of length ceil(vl/8)\n\n")
    elif ins.name == "vl<nf>re<eew>":
        f.write("""  # <eew>=8, width == '000'; <eew>=16, width == '101'; <eew>=32, width == '110'; <eew>=64, width == '111';
        
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
  vl8re64.v v8, (a0)\n\n""")

    elif ins.name == "vs<nf>r":
        f.write("""  vs1r.v v3, (a1) # Store v3 to address in a1
  vs2r.v v2, (a1) # Store v2-v3 to address in a1
  vs4r.v v4, (a1) # Store v4-v7 to address in a1
  vs8r.v v8, (a1) # Store v8-v15 to address in a1
\n\n""")
        
    else:
        for len_bits in {8, 16, 32, 64}:
            f.write(ins.usage.format(len=len_bits,
                    op_len=dict_width[len_bits]))
        f.write("\n")

    if ins.name == "vlseg<nf>ei<eew>":
        f.write("  # There are also fault-only-rst versions of the unit-stride instructions.\n\
  {}ff.v vd, (rs1), vm # Unit-stride fault-only-first segment loads\n\n".format(ins.name))

    # f.write(".. tabularcolumns:: |c|c|c|c|c|c|c|c|c|\n.. table::\n\n")
    bit_in_11_7 = "vd " if ins.funct7 == "0000111" else "vs3"
    table_load_unit_stride = """
+-----+---+-----+--+-----+-----+-----+----+-------+
|31-29|28 |27-26|25|24-20|19-15|14-12|11-7|6-0    |
+-----+---+-----+--+-----+-----+-----+----+-------+
|{nf}  |{mew}  |{mop}   |vm|{bit_in_24_20}|rs1  |{width}|{bit_in_11_7} |{funct7}|
+-----+---+-----+--+-----+-----+-----+----+-------+""".format(funct7=ins.funct7, bit_in_11_7=bit_in_11_7, width=ins.width, bit_in_24_20=ins.bit_in_24_20, mop=ins.mop, mew=ins.mew, nf=ins.nf)

    f.write("{}\n\n".format(table_load_unit_stride))


instructions = []


def init_instructions():

    ins = Instruction("vle<eew>")
    ins.description = "Vector unit-stride load instructions."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "00000"
    ins.mop = "00"
    ins.usage = "  vle{len}.v   vd, (rs1), vm # {len}-bit unit-stride load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vlm")
    ins.description = "Vector unit-stride mask load."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "01011"
    ins.mop = "00"
    ins.width = "000  "
    instructions.append(ins)

    ins = Instruction("vlse<eew>")
    ins.description = "Vector strided load instructions."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "rs2  "
    ins.mop = "10"
    ins.usage = "  vlse{len}.v    vd, (rs1), rs2, vm # {len}-bit strided load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vluxei<eew>")
    ins.description = "Vector indexed-unordered load instructions."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "01"
    ins.usage = "  vluxei{len}.v    vd, (rs1), vs2, vm # unordered {len}-bit indexed load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vloxei<eew>")
    ins.description = "Vector indexed-ordered load instructions."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "11"
    ins.usage = "  vloxei{len}.v    vd, (rs1), vs2, vm   # ordered  {len}-bit indexed load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vle<eew>ff")
    ins.description = "Vector unit-stride fault-only-first loads."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "10000"
    ins.mop = "00"
    ins.usage = "  vle{len}ff.v    vd, (rs1), vm   # {len}-bit unit-stride fault-only-first load with width == '{op_len}'\n"
    instructions.append(ins)

    """Segment instructions"""

    ins = Instruction("vlseg<nf>e<eew>")
    ins.description = "Unit-stride segment loads."
    ins.funct7 = "0000111"
    # Takes segment loads/stores as normal unit-stride loads/stores, hence got '00000'.
    ins.bit_in_24_20 = "00000"
    ins.mop = "00"
    ins.nf = "nf "
    ins.usage = "  vlseg<nf>e{len}.v    vd, (rs1), vm   # {len}-bit unit-stride segment load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vlsseg<nf>e<eew>")
    ins.description = "Strided segment loads."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "rs2  "
    ins.mop = "10"
    ins.nf = "nf "
    ins.usage = "  vlsseg<nf>e{len}.v vd, (rs1), rs2, vm   # {len}-bit strided segment load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vluxseg<nf>ei<eew>")
    ins.description = "Indexed-unordered segment loads."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "01"
    ins.nf = "nf "
    ins.usage = "  vluxseg<nf>ei{len}.v vd, (rs1), vs2, vm   # {len}-bit indexed-unordered segment load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vloxseg<nf>ei<eew>")
    ins.description = "Indexed-ordered segment loads."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "11"
    ins.nf = "nf "
    ins.usage = "  vloxseg<nf>ei{len}.v vd, (rs1), vs2, vm     # {len}-bit indexed-ordered segment load with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vl<nf>re<eew>")
    ins.description = "Whole register load instructions."
    ins.funct7 = "0000111"
    ins.bit_in_24_20 = "01000"
    ins.mop = "00"
    ins.nf = "nf "
    ins.usage = ""
    instructions.append(ins)



    ins = Instruction("vse<eew>")
    ins.description = "Vector unit-stride store instructions."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "00000"
    ins.mop = "00"
    ins.usage = "  vse{len}.v   vs3, (rs1), vm # {len}-bit unit-stride store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vsm")
    ins.description = "Vector unit-stride mask store."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "01011"
    ins.mop = "00"
    ins.width = "000  "
    instructions.append(ins)

    ins = Instruction("vsse<eew>")
    ins.description = "Vector strided store instructions."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "rs2  "
    ins.mop = "10"
    ins.usage = "  vsse{len}.v    vs3, (rs1), rs2, vm # {len}-bit strided store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vsuxei<eew>")
    ins.description = "Vector indexed-unordered store instructions."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "01"
    ins.usage = "  vsuxei{len}.v    vs3, (rs1), vs2, vm # unordered {len}-bit indexed store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vsoxei<eew>")
    ins.description = "Vector indexed-ordered store instructions."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "11"
    ins.usage = "  vsoxei{len}.v    vs3, (rs1), vs2, vm # ordered {len}-bit indexed store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vsseg<nf>e<eew>")
    ins.description = "Unit-stride segment stores."
    ins.funct7 = "0100111"
    # Takes segment loads/stores as normal unit-stride loads/stores, hence got '00000'.
    ins.bit_in_24_20 = "00000"
    ins.mop = "00"
    ins.nf = "nf "
    ins.usage = "  vsseg<nf>e{len}.v    vd, (rs1), vm   # {len}-bit unit-stride segment store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vssseg<nf>e<eew>")
    ins.description = "Strided segment stores."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "rs2  "
    ins.mop = "10"
    ins.nf = "nf "
    ins.usage = "  vssseg<nf>e{len}.v vs3, (rs1), rs2, vm   # {len}-bit strided segment store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vsuxseg<nf>ei<eew>")
    ins.description = "Indexed-unordered segment stores."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "01"
    ins.nf = "nf "
    ins.usage = "  vsuxseg<nf>ei{len}.v vs3, (rs1), vs2, vm   # {len}-bit indexed-unordered segment store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vsoxseg<nf>ei<eew>")
    ins.description = "Indexed-ordered segment stores."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "vs2  "
    ins.mop = "11"
    ins.nf = "nf "
    ins.usage = "  vsoxseg<nf>ei{len}.v vs3, (rs1), vs2, vm    # {len}-bit indexed-ordered segment store with width == '{op_len}'\n"
    instructions.append(ins)

    ins = Instruction("vs<nf>r")
    ins.description = "Whole register store instructions."
    ins.funct7 = "0100111"
    ins.bit_in_24_20 = "01000"
    ins.mop = "00"
    ins.nf = "nf "
    ins.usage = ""
    ins.width = "000  "
    instructions.append(ins)


if __name__ == "__main__":

    init_instructions()

    output_file = "/root/exper/rvv-isadoc/docs/source/load_and_store.rst"
    with open(output_file, "w") as f:

        page_title = "Vector Load and Store Instructions"
        f.write("{title}\n{underline}\n\n".format(
            title=page_title, underline="="*len(page_title)))

        for ins in instructions:
            generate_instruction(ins)
