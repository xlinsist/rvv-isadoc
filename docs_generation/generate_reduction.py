from load_instructions import Instruction, load_instructions
from init_instructions_info import list_reduction


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
    assert(False)

def generate_single_table(table):
    """generate table according to table string."""
    # table_template = ".. tabularcolumns:: |c|c|c|c|c|c|c|\n.. table::\n\n{}\n\n".format(
    #     table)
    f.write(table + "\n\n")


def generate_arith_table(ins):

    group = ins.group
    assert(ins.isV == True) # Instructions of permutation should be with isV set.

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

    if group == 0:  # instruction belongs to "OPI.."
        if ins.isV:
            generate_single_table(table_OPIVV)
        else:
            assert(False)
    elif group == 1:  # instruction belongs to "OPM.."
        if ins.isV:
            generate_single_table(table_OPMVV)
        else:
            assert(False)
    else:  # instruction belongs to "OPF.."
        if ins.isV:
            generate_single_table(table_OPFVV)
        else:
            assert(False)


def generate_instruction(ins):

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
        if ins.name in list_reduction:
            instructions.append(ins)
    # print(len(instructions))
    # for ins in instructions:
    #     print(ins.name)

    output_file = "/root/exper/rvv-isadoc/docs/source/arith_reduction.rst"
    with open(output_file, "w") as f:
        page_title = "Vector Reduction Instructions"
        f.write("{title}\n{underline}\n\n".format(
            title=page_title, underline="="*len(page_title)))
        for ins in instructions:
            generate_instruction(ins)
