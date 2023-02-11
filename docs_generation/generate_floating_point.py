from load_instructions import Instruction, load_instructions
from init_instructions_info import list_floating_point


def generate_single_format(format):
    format_template = "  {}\n".format(format)
    f.write(format_template)


def generate_arith_format(ins):
    group = ins.group
    name = ins.name

    f.write("::\n\n")

    if name[-2:] == ".w":
        format_widening_wv = """{}v vd, vs2, vs1, vm""".format(name)
        format_widening_wf = """{}f vd, vs2, rs1, vm""".format(name)
        generate_single_format(format_widening_wv)      
        generate_single_format(format_widening_wf)
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

    if ins.name == "VFUNARY0":
        f.write("""vfcvt
------

Conversion operations to convert to and from floating-point values and unsigned and signed integers, where both source and destination are SEW wide.

::

    vfcvt.xu.f.v vd, vs2, vm # Convert float to unsigned integer, with vs1 = '00000'.
    vfcvt.x.f.v vd, vs2, vm # Convert float to signed integer, with vs1 = '00001'.
    vfcvt.rtz.xu.f.v vd, vs2, vm # Convert float to unsigned integer, truncating, with vs1 = '00110'.
    vfcvt.rtz.x.f.v vd, vs2, vm # Convert float to signed integer, truncating, with vs1 = '00111'.
    vfcvt.f.xu.v vd, vs2, vm # Convert unsigned integer to float, with vs1 = '00010'.
    vfcvt.f.x.v vd, vs2, vm # Convert signed integer to float, with vs1 = '00011'.

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+



vfwcvt
------

Conversion instructions to convert between narrower integer and floating-point datatypes to a type of twice the width.

::

    vfwcvt.xu.f.v vd, vs2, vm # Convert float to double-width unsigned integer, with vs1 = '01000'.
    vfwcvt.x.f.v vd, vs2, vm # Convert float to double-width signed integer, with vs1 = '01001.
    vfwcvt.rtz.xu.f.v vd, vs2, vm # Convert float to double-width unsigned integer, truncating, with vs1 = '01110.
    vfwcvt.rtz.x.f.v vd, vs2, vm # Convert float to double-width signed integer, truncating, with vs1 = '01111.
    vfwcvt.f.xu.v vd, vs2, vm # Convert unsigned integer to double-width float, with vs1 = '01010.
    vfwcvt.f.x.v vd, vs2, vm # Convert signed integer to double-width float, with vs1 = '01011.
    vfwcvt.f.f.v vd, vs2, vm # Convert single-width float to double-width float, with vs1 = '01100.

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+



vfncvt
------

Conversion instructions to convert wider integer and floating-point datatypes to a type of half the width.

::

    vfncvt.xu.f.w vd, vs2, vm # Convert double-width float to unsigned integer, with vs1 = '10000'.
    vfncvt.x.f.w vd, vs2, vm # Convert double-width float to signed integer, with vs1 = '10001'.
    vfncvt.rtz.xu.f.w vd, vs2, vm # Convert double-width float to unsigned integer, truncating, with vs1 = '10110'.
    vfncvt.rtz.x.f.w vd, vs2, vm # Convert double-width float to signed integer, truncating, with vs1 = '10111'.
    vfncvt.f.xu.w vd, vs2, vm # Convert double-width unsigned integer to float, with vs1 = '10010'.
    vfncvt.f.x.w vd, vs2, vm # Convert double-width signed integer to float, with vs1 = '10011'.
    vfncvt.f.f.w vd, vs2, vm # Conver double-width float to single-width float, with vs1 = '10100'.
    vfncvt.rod.f.f.w vd, vs2, vm # Convert double-width float to single-width float, with vs1 = '10101'.
    # rounding towards odd.

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010010|vm|vs2  |vs1     |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+


""")
        return


    if ins.name == "VFUNARY1":
        f.write("""vfsqrt
------

Floating-point square root.

::

  vfsqrt.v vd, vs2, vm 

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010011|vm|vs2  |00000   |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+


vfrsqrt7
--------

Floating-point reciprocal square-root estimate to 7 bits.

::

  vfrsqrt7.v vd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010011|vm|vs2  |00100   |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+

vfrec7
------

Floating-point reciprocal estimate to 7 bits.

::

  vfrec7.v vd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010011|vm|vs2  |00101   |001  |vd/rd|1010111|
+------+--+-----+--------+-----+-----+-------+


vfclass
-------

Examines the value in vs1 and writes to vd a 10-bit mask that indicates the class of the floating-point number.

::

  vfclass.v vd, vs2, vm

+------+--+-----+--------+-----+-----+-------+
|31-26 |25|24-20|19-15   |14-12|11-7 |6-0    |
+------+--+-----+--------+-----+-----+-------+
|010011|vm|vs2  |10000   |001  |vd/rd|1010111|
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
        if ins.name in list_floating_point:
            instructions.append(ins)
    # print(len(instructions))
    # for ins in instructions:
    #     print(ins.name)

    output_file = "/root/exper/rvv-isadoc/docs/source/arith_floating_point.rst"
    with open(output_file, "w") as f:
        page_title = "Vector Floating-Point Instructions"
        f.write("{title}\n{underline}\n\n".format(
            title=page_title, underline="="*len(page_title)))
        for ins in instructions:
            generate_instruction(ins)
