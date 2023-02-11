from load_instructions import Instruction, load_instructions
from init_instructions_info import list_integer, list_fixed_point, list_floating_point, list_reduction, list_mask, list_permutation


def generate_single_format(format):
    format_template = "  {}\n".format(format)
    f.write(format_template)


def generate_arith_format(ins):
    group = ins.group
    name = ins.name

    format_OPIVV = """{}.vv vd, vs2, vs1, vm""".format(name)
    format_OPFVV = """{}.vv vd, vs2, vs1, vm""".format(name)
    format_OPMVV = """{}.vv vd, vs2, vs1, vm""".format(name)
    format_OPIVI = """{}.vi vd, vs2, imm, vm""".format(name)
    format_OPIVX = """{}.vx vd, vs2, rs1, vm""".format(name)
    format_OPFVF = """{}.vf vd, vs2, rs1, vm""".format(name)
    format_OPMVX = """{}.vx vd, vs2, rs1, vm""".format(name)

    f.write("::\n\n")

    if "red" in name:
        format_reduce = """{}.vs vd, vs2, vs1, vm""".format(name)
        generate_single_format(format_reduce)
        return
    if name[0:2] == "vm":
        format_mask_binary = """{}.mm vd, vs2, vs1, vm""".format(name)
        generate_single_format(format_mask_binary)
    if name[-2:] == ".w":
        format_widening_wv = """{}v vd, vs2, vs1, vm""".format(name)
        generate_single_format(format_widening_wv)
        if name[1] == "f":
            format_widening_wx = """{}x vd, vs2, vs1, vm""".format(name)
        else:
            format_widening_wx = """{}f vd, vs2, vs1, vm""".format(name)

        generate_single_format(format_widening_wx)
        return
    
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

    f.write("{title}\n{underline}\n\n".format(
        title=ins.name, underline="-"*len(ins.name)))
    f.write("{}\n\n".format(ins.description))

    generate_arith_format(ins)
    f.write("\n")

    generate_arith_table(ins)

if __name__ == "__main__":
    instructions = load_instructions()
    # print(len(instructions))
    # for ins in instructions:
    #     print(ins.name)

    # list_integer, list_fixed_point, list_floating_point, list_reduction, list_mask, list_permutation
    # output_file = "output.rst"

    """11. Vector Integer Arithmetic Instructions"""
    """12. Vector Fixed-Point Arithmetic Instructions"""
    """"13. Vector Floating-Point Instructions"""
    """14. Vector Reduction Operations"""
    """15. Vector Mask Instructions"""
    """16. Vector Permutation Instructions"""

    output_file = "/root/exper/rvv-isadoc/docs/source/arith_integer.rst"
    with open(output_file, "w") as f:
        page_title = "Vector Arithmetic Instructions"
        f.write("{title}\n{underline}\n\n".format(
            title=page_title, underline="="*len(page_title)))
        for ins in instructions:
            generate_instruction(ins)
