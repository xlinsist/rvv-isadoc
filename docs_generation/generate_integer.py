from load_instructions import Instruction, load_instructions, dict_info
from init_instructions_info import list_integer


def generate_single_format(format):
    format_template = "  {}\n".format(format)
    f.write(format_template)


def generate_arith_format(ins):
    group = ins.group
    name = ins.name

    f.write("::\n\n")

    if name[-2:] == ".w": # Widening instructions have special format.
        format_widening_wv = """{}v vd, vs2, vs1, vm""".format(name)
        format_widening_wx = """{}x vd, vs2, rs1, vm""".format(name)
        generate_single_format(format_widening_wv)      
        generate_single_format(format_widening_wx)
        return

    if name in ["vnsrl", "vnsra"]: # Narrowing instructions have special format.
        format_narrowing_V = """{}.wv vd, vs2, vs1, vm""".format(name)
        format_narrowing_X = """{}.wx vd, vs2, rs1, vm""".format(name)
        format_narrowing_I = """{}.wi vd, vs2, uimm, vm""".format(name)
        generate_single_format(format_narrowing_V)
        generate_single_format(format_narrowing_X)
        generate_single_format(format_narrowing_I)
        return
    
    if name == "vadc":
        format_vadc = """# vd[i] = vs2[i] + vs1[i] + v0.mask[i]
  vadc.vvm vd, vs2, vs1, v0
  # vd[i] = vs2[i] + x[rs1] + v0.mask[i]
  vadc.vxm vd, vs2, rs1, v0
  # vd[i] = vs2[i] + imm + v0.mask[i]
  vadc.vim vd, vs2, imm, v0"""
        generate_single_format(format_vadc)
        return

    if name == "vmadc":
        format_vmadc = """# vd.mask[i] = carry_out(vs2[i] + vs1[i] + v0.mask[i])
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
  vmadc.vi vd, vs2, imm # Vector-immediate, no carry-in"""
        generate_single_format(format_vmadc)
        return

    if name == "vsbc":
        format_vabc = """# vd[i] = vs2[i] - vs1[i] - v0.mask[i]
  vsbc.vvm vd, vs2, vs1, v0 # Vector-vector
  # vd[i] = vs2[i] - x[rs1] - v0.mask[i]
  vsbc.vxm vd, vs2, rs1, v0 # Vector-scalar"""
        generate_single_format(format_vabc)
        return

    if name == "vmsbc":
        format_vmsbc = """# vd.mask[i] = borrow_out(vs2[i] - vs1[i] - v0.mask[i])
 vmsbc.vvm vd, vs2, vs1, v0 # Vector-vector
 # vd.mask[i] = borrow_out(vs2[i] - x[rs1] - v0.mask[i])
 vmsbc.vxm vd, vs2, rs1, v0 # Vector-scalar
 # vd.mask[i] = borrow_out(vs2[i] - vs1[i])
 vmsbc.vv vd, vs2, vs1 # Vector-vector, no borrow-in
 # vd.mask[i] = borrow_out(vs2[i] - x[rs1])
 vmsbc.vx vd, vs2, rs1 # Vector-scalar, no borrow-in"""
        generate_single_format(format_vmsbc)
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
    
    if ins.name == "VXUNARY0":
        f.write("""vzext/vsext
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
        if ins.name in list_integer:
            instructions.append(ins)
    # print(len(instructions))
    # for ins in instructions:
    #     print(ins.name)

    output_file = "/root/exper/rvv-isadoc/docs/source/arith_integer.rst"
    with open(output_file, "w") as f:
        page_title = "Vector Integer Instructions"
        f.write("{title}\n{underline}\n\n".format(
            title=page_title, underline="="*len(page_title)))
        for ins in instructions:
            generate_instruction(ins)
