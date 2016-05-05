"""
   Hack Assembly Language Translator
   Provides tools and methods to translate HACK assembly code into
   HACK CPU instructions
   -----------------------------------------------------------------------
   Written by: Samuel Pell 06-05-16 (dd-mm-yy)
   -----------------------------------------------------------------------
   Contains: translate
             _create_symbol_table
             _translate_into_bin
             _is_A_instruction
             _add_pseudoinstruction_to_table
             _add_symbol_to_table
             _translate_A_instruction
             _translate_C_instruction
             _dec_to_bin
             _command_to_bin
"""

import SymbolTable
import AssemblyCleaner

SYMBOL_INDICATOR = "@"
PSUEDOINSTRUCTION_INDICATOR = "("
SIDE_DELIM = "="
JUMP_DELIM = ";"
COMMAND_TABLE = {
                 "0" : "0101010", "1" : "0111111", "-1" : "0111010",
                 "D" : "0001100", "A" : "0110000", "M" : "1110000",
                 "!D" : "0001101", "!A" : "0110001", "!M" : "1110001",
                 "-D" : "0001111", "-A" : "0110011", "-M" : "1110011",
                 "D+1" : "0011111", "A+1" : "0110111", "M+1" : "1110111",
                 "D-1" : "0001110", "A-1" : "0110010", "M-1" : "1110010",
                 "D+A" : "0000010", "D+M" : "1000010", "D-A" : "0010011",
                 "D-M" : "1010011", "A-D" : "0000111", "M-D" : "1000111",
                 "D&A" : "0000000", "D&M" : "1000000", "D|A" : "0010101",
                 "D|M" : "1010101"
                }
DEST_TABLE = {
              "null" : "000", "M" : "001", "D" : "010", "MD" : "011",
              "A" : "100", "AM" : "101", "AD" : "110", "AMD" : "111"
             }
JUMP_TABLE = {
              "null" : "000", "JGT" : "001", "JEQ" : "010", "JGE" : "011",
              "JLT" : "100", "JNE" : "101", "JLE" : "110", "JMP" : "111"
             }
              
            
def translate(file_contents):
    """
       Translates HACK assembly language into HACK CPU code
       Takes a raw assembly file, and returns a list of 
       CPU instructions.
    """
    assembly_instructions = AssemblyCleaner.clean_file(file_contents)
    symbol_table = _create_symbol_table(assembly_instructions)
    assembly_instructions = AssemblyCleaner.remove_psuedoinstructions(
                                                  assembly_instructions)        
    cpu_instructions = _translate_to_bin(assembly_instructions, 
                                                 symbol_table)
    return cpu_instructions


def _create_symbol_table(assembly_instructions):
    """
       Takes a list of assembly instructions and finds all the references 
       in the program and assigns them to the symbol table. If it is a 
       user defined label it passes None to the table for that variable.
    """
    symbol_table = SymbolTable.SymbolTable()
    
    _add_psuedoinstructions_to_table(assembly_instructions, symbol_table) 
    
    for instruction in assembly_instructions:
        if instruction.startswith(SYMBOL_INDICATOR):
            _add_symbol_to_table(instruction, symbol_table)
            
    return symbol_table
  

def _add_symbol_to_table(instruction, symbol_table):
    """Adds a symbol to the table"""
    if instruction[1:].isnumeric():
        symbol_table[instruction[1:]] = int(instruction[1:])
    else:
        symbol_table[instruction[1:]] = None
    
        
def _add_psuedoinstructions_to_table(instructions, symbol_table):
    """Adds a psuedo instruction to the table so it can be jumped to"""
    num_labels_assigned = 0
    for i in range(len(instructions)):
        instruction = instructions[i]
        if instruction.startswith(PSUEDOINSTRUCTION_INDICATOR):
            symbol_table[instruction[1:-1]] = i - num_labels_assigned
            num_labels_assigned += 1
                    
                    
def _translate_to_bin(assembly_instructions, symbol_table):
    """Translates each line into CPU instruction"""
    translated_instructions = []
    for instruction in assembly_instructions:
        if _is_A_instruction(instruction):
            translated_line = _translate_A_instruction(instruction, 
                                                       symbol_table)
        else:
            translated_line = _translate_C_instruction(instruction)
        translated_instructions.append(translated_line)
        
    return translated_instructions
                
                
def _is_A_instruction(instruction):
    """Returns True if instruction is an A instruction"""
    return instruction.startswith(SYMBOL_INDICATOR)


def _translate_A_instruction(instruction, symbol_table):
    """
       Translates an assembly instruction into a HACK CPU 
       A-type instruction
    """
    return _dec_to_bin(symbol_table[instruction[1:]])


def _translate_C_instruction(instruction):
    """
       Translates an assembly instruction into a HACK CPU 
       C-type instruction
    """
    cleaned_instruction = AssemblyCleaner.remove_space(instruction)
    rhs_indicator = cleaned_instruction.find(SIDE_DELIM)
    if rhs_indicator == -1:
        command, jump = cleaned_instruction.split(JUMP_DELIM)
        return _command_to_bin(command, "null", jump)
    else:
        dest, command = cleaned_instruction.split(SIDE_DELIM)
        return _command_to_bin(command, dest)
    

def _dec_to_bin(number):
    """Turns a decimal number into a binary string"""
    converted_number = "{0:b}".format(number)
    padding = "0" * (16 - len(converted_number))
    return padding + converted_number


def _command_to_bin(command, dest, jump="null"):
    """
       Turns a C instruction (command and dest sections) 
       into its binary equivalent. If jump is not passed
       to the function it defaults to it's null codes.
    """
    conc_command = COMMAND_TABLE[command] + DEST_TABLE[dest]
    return "111" + conc_command + JUMP_TABLE[jump]