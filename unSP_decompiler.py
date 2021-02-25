#!/usr/bin/python3
import re
import ntpath

min = 20

#regexes for opcodes 

DSI6 = "1111111000[01]{6}"
CALL = ""
JMPF = ""
JMPR = ""
FIR_MOV = ""
Fraction = ""
INT_SET = ""
IRQ = ""
SECBANK = ""
FIQ = ""
IRQ_Nest_Mode = ""
BREAK = ""
CALLR = ""
DIVS = ""
DIVQ = ""
EXP = ""
NOP = ""
DS_Access = ""
FR_Access = ""
MUL = ""
MULS = ""
Register_BITOP = ""
#Register_BITOP2 = ""
Memory_BITOP = ""
#Memory_BITOP2 = ""
#Memory_BITOP3 = ""
_16_bits_Shift = ""
RETI = ""
RETF = ""
Base_plus_Disp6 = ""
IMM6 = ""
Branch = ""
Stack_Operation = ""
DS_Indirect = ""
IMM16 = ""
Direct16 = ""
Direct6 = ""
Register = ""
Ext_Code_y = ""
Ext_Push_Pop = ""
Ext_IMM16 = ""
Ext_A16 = ""
Ext_DS_Indirect = ""
Ext_IM6 = ""
Ext_Base_plus_Disp6 = ""
Ext_A6 = ""


def detect_opcodes(path):
    bin_file = open(path, 'rb')
    bin_lines = bin_file.readlines()
    opcodes = []
    for x in bin_lines:
        serial_buffer = []
        # beginning to end of line, going by 16 bits
        for i in range(0, len(x) - 1, 16):
            serial_buffer.append(x[i:i + 16])
        for opcode in serial_buffer:
            opcodes.append(opcode)
    return opcodes

def disassemble(opcodes):
    asm_funcs = []
    for opcode in opcodes:
        if (opcode.search(DSI6) != None):
            asm_funcs.append("DS=" + hex(int(opcode[10:15], 2)))

    return asm_funcs


    



def output_patterns(path, asm_funcs):
    name = ntpath.basename(path)
    f = open(name + "_decompiled.txt", "w")
    for func in asm_funcs:
        f.write(func)
        f.write("\n")
        print(func)
    f.close()


        

print("Enter file path to detect patterns of: ")
path = input()
opcodes = detect_opcodes(path)
asm_funcs = disassemble(opcodes)
output_patterns(path, asm_funcs)
print("done")

