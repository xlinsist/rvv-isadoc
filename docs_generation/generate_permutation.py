from load_instructions import Instruction, load_instructions
from init_instructions_info import list_permutation


def generate_single_format(format):
    format_template = "  {}\n".format(format)
    f.write(format_template)


def generate_arith_format(ins):
    group = ins.group
    name = ins.name
    
    f.write("::\n\n")

    if name == "vmerge/vmv":
        format_vmerge_vmv = """vmerge.vvm vd, vs2, vs1, v0 # vd[i] = v0.mask[i] ? vs1[i] : vs2[i]
  vmerge.vxm vd, vs2, rs1, v0 # vd[i] = v0.mask[i] ? x[rs1] : vs2[i]
  vmerge.vim vd, vs2, imm, v0 # vd[i] = v0.mask[i] ? imm : vs2[i]

  vmv.v.v vd, vs1 # vd[i] = vs1[i]
  vmv.v.x vd, rs1 # vd[i] = x[rs1]
  vmv.v.i vd, imm # vd[i] = imm"""
        generate_single_format(format_vmerge_vmv)
        return

    if name == "vfmerge/vfmv":
        format_vfmerge_vfmv = """vfmerge.vfm vd, vs2, rs1, v0 # vd[i] = v0.mask[i] ? f[rs1] : vs2[i]

  vfmv.v.f vd, rs1 # vd[i] = f[rs1]"""
        generate_single_format(format_vfmerge_vfmv)
        return

    if name == "vcompress":
        format_vcompress = "vcompress.vm vd, vs2, vs1 # Compress into vd elements of vs2 where vs1 is enabled"
        generate_single_format(format_vcompress)
        return
         

    format_OPIVV = """{}.vv vd, vs2, vs1, vm""".format(name)
    format_OPFVV = """{}.vv vd, vs2, vs1, vm""".format(name)
    format_OPMVV = """{}.vv vd, vs2, vs1, vm""".format(name)
    format_OPIVI = """{}.vi vd, vs2, imm, vm""".format(name)
    format_OPIVX = """{}.vx vd, vs2, rs1, vm""".format(name)
    format_OPFVF = """{}.vf vd, vs2, rs1, vm""".format(name)
    format_OPMVX = """{}.vx vd, vs2, rs1, vm""".format(name)

    if group == 0:  # instruction belongs to "OPI..
        if ins.isV:
            generate_single_format(format_OPIVV)
        if ins.isX:
            generate_single_format(format_OPIVX)
        if ins.isI:
            generate_single_format(format_OPIVI)
    elif group == 1:  # instruction belongs to "OPM.."
        if ins.isV:
            generate_single_format(format_OPMVV)
        if ins.isX:
            generate_single_format(format_OPMVX)
    else:  # instruction belongs to "OPF.."
        if ins.isV:
            generate_single_format(format_OPFVV)
        if ins.isF:
            generate_single_format(format_OPFVF)


def generate_single_table(table):
    """generate table according to table string."""
    # table_template = ".. tabularcolumns:: |c|c|c|c|c|c|c|\n.. table::\n\n{}\n\n".format(
    #     table)
    f.write(table + "\n\n")


def generate_arith_table(ins):

    group = ins.group

    table_template = """+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|{funct6}|vm|vs2  |{bit_in_19_15}|{bit_in_14_12}  |{bit_in_11_7}|1010111|
+------+--+-----+--------+-----+-----+-------+"""

    table_OPIVV = table_template.format(
        funct6=ins.funct6, bit_in_19_15="vs1     ", bit_in_14_12="000", bit_in_11_7="vd   ")

    table_OPFVV = table_template.format(
        funct6=ins.funct6, bit_in_19_15="vs1     ", bit_in_14_12="001", bit_in_11_7="vd/rd")

    table_OPMVV = table_template.format(
        funct6=ins.funct6, bit_in_19_15="vs1     ", bit_in_14_12="010", bit_in_11_7="vd/rd")

    table_OPIVI = table_template.format(
        funct6=ins.funct6, bit_in_19_15="imm[4:0]", bit_in_14_12="011", bit_in_11_7="vd   ")

    table_OPIVX = table_template.format(
        funct6=ins.funct6, bit_in_19_15="rs1     ", bit_in_14_12="100", bit_in_11_7="vd   ")

    table_OPFVF = table_template.format(
        funct6=ins.funct6, bit_in_19_15="rs1     ", bit_in_14_12="101", bit_in_11_7="vd   ")

    table_OPMVX = table_template.format(
        funct6=ins.funct6, bit_in_19_15="rs1     ", bit_in_14_12="110", bit_in_11_7="vd/rd")

    if group == 0:  # instruction belongs to "OPI.."
        if ins.isV:
            generate_single_table(table_OPIVV)
        if ins.isX:
            generate_single_table(table_OPIVX)
        if ins.isI:
            generate_single_table(table_OPIVI)
    elif group == 1:  # instruction belongs to "OPM.."
        if ins.isV:
            generate_single_table(table_OPMVV)
        if ins.isX:
            generate_single_table(table_OPMVX)
    else:  # instruction belongs to "OPF.."
        if ins.isV:
            generate_single_table(table_OPFVV)
        if ins.isF:
            generate_single_table(table_OPFVF)


def generate_instruction(ins):

    if ins.name == "VRXUNARY0":
        f.write("""vmv.s.x
-------

Copies the scalar integer register to element 0 of the destination vector register. 

::

  vmv.s.x vd, rs1 # vd[0] = x[rs1] (vs2=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|00000|vs1     |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

""")
        return
        
    if ins.name == "VWXUNARY0":
        f.write("""vmv.x.s
-------

Copies a single SEW-wide element from index 0 of the source vector register to a destination integer register.

::

  vmv.x.s rd, vs2 # x[rd] = vs2[0] (vs1=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |00000   |010  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

""")
        return


    if ins.name == "VRFUNARY0":
        f.write("""vfmv.s.f
--------

Copies the scalar floating-point register to element 0 of the destination vector register.

::

  vfmv.s.f vd, rs1 # vd[0] = f[rs1] (vs2=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|00000|rs1     |101  |vd   |1010111|
+------+--+-----+--------+-----+-----+-------+

""")
        return
        
    if ins.name == "VWFUNARY0":
        f.write("""vfmv.f.s
--------

Copies a single SEW-wide element from index 0 of the source vector register to a destination scalar floating-point register.


::

  vfmv.f.s rd, vs2 # f[rd] = vs2[0] (rs1=0)

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |00000   |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

""")
        return


    f.write("{title}\n{underline}\n\n".format(
        title=ins.name, underline="-"*len(ins.name)))
    f.write("{}\n\n".format(ins.description))

    generate_arith_format(ins)
    f.write("\n")

    generate_arith_table(ins)

if __name__ == "__main__":
    instructions_all = load_instructions()
    instructions = []
    for ins in instructions_all:
        if ins.name in list_permutation:
            instructions.append(ins)
    # print(len(instructions))
    # for ins in instructions:
    #     print(ins.name)

    output_file = "/root/exper/rvv-isadoc/docs/source/arith_permutation.rst"
    with open(output_file, "w") as f:
        page_title = "Vector Permutation Instructions"
        f.write("{title}\n{underline}\n\n".format(
            title=page_title, underline="="*len(page_title)))
        for ins in instructions:
            generate_instruction(ins)
