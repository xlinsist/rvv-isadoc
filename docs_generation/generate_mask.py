from load_instructions import Instruction, load_instructions
from init_instructions_info import list_mask


def generate_single_format(format):
    format_template = "  {}\n".format(format)
    f.write(format_template)


def generate_arith_format(ins):
    name = ins.name

    f.write("::\n\n")
    list_mask_binary = ['vmand', 'vmnand', 'vmandn', 'vmandnot', 'vmornot', 'vmxor', 'vmor', 'vmnor', 'vmorn', 'vmxnor']
    # list_mask_unary = ['vcpop', 'vfirst', 'vmsbf', 'vmsif', 'vmsof', 'viota', 'vid']
    if name in list_mask_binary:
        format_mask_binary = """{}.mm vd, vs2, vs1, vm""".format(name)
        generate_single_format(format_mask_binary)


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

    if ins.name == "VMUNARY0":
        f.write("""vmsbf
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


""")
        return
    
    if ins.name == "VWXUNARY0":
        f.write("""vpopc
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

Find-rst-set mask bit. Finds the lowest-numbered active element of the source mask vector that has the value 1 and \
writes that element's index to a GPR. If no active element has the value 1, -1 is written to the GPR.

::

  vfirst.m rd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010000|vm|vs2  |10001   |010  |vd/rd|1010111|
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
        if ins.name in list_mask:
            instructions.append(ins)
    # print(len(instructions))
    # for ins in instructions:
    #     print(ins.name)

    output_file = "/root/exper/rvv-isadoc/docs/source/arith_mask.rst"
    with open(output_file, "w") as f:
        page_title = "Vector Mask Instructions"
        f.write("{title}\n{underline}\n\n".format(
            title=page_title, underline="="*len(page_title)))
        for ins in instructions:
            generate_instruction(ins)
