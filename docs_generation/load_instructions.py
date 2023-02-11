from init_instructions_info import dict_info


class Instruction:
    """Information of an instruction.

    Attributes:
        group: An integer of {0, 1, 2}. "= 0" means the type of this instruction is "OPI..", "=1" means "OPM..", and "=2" means "OPF..".
        isV/isX/isI/isF: A boolean indicating the type of this instruction can be "...VV", "...VX", "...VI" and "...VF" separately.
        funct6: A six-length bit codes represented "funct6" in ISA's format.
        name: 
        description:
    """

    def __init__(self, group):
        self.group = group
        self.isV = self.isX = self.isI = self.isF = False
        self.funct6 = ""
        self.name = ""
        self.description = ""


def check_isT(word):
    if word in {"V", "X", "I", "F"}:
        return True
    return False


def check_funct6(word):
    if len(word) != 6:
        return False
    for i in word:
        if i < '0' or i > '9':
            return False
    return True


def load_instructions():
    """Turn input from file into list of instruction class, then return the list."""

    input_file = "./input.txt"
    inputs = []
    with open(input_file) as f:
        for line in f:
            line = line[:-1]
            if line.replace(" ", "") == "":
                continue
            inputs.append(line)

    instructions = []
    ins = Instruction(0)
    for line_id in range(len(inputs)):
        words = inputs[line_id].strip().split()
        if len(words) == 1: # Ignore empty instructions.
            continue
        for word in words:
            if check_funct6(word):
                ins = Instruction(line_id % 3)
                instructions.append(ins)
                ins.funct6 = word
            elif check_isT(word):
                if word == "V":
                    ins.isV = True
                if word == "X":
                    ins.isX = True
                if word == "I":
                    ins.isI = True
                if word == "F":
                    ins.isF = True
            else:
                ins.name = word

    # instructions_nonempty = []
    # for ins in instructions:
    #     if ins.name != "":
    #         instructions_nonempty.append(ins)
    # instructions = instructions_nonempty

    for ins in instructions:
        ins.description = dict_info.get(
            ins.name, "Instruction info placeholder.")

    return instructions


if __name__ == "__main__":
    print(load_instructions())
