"""
   Hack Assembly Language Translator
   Provides tools and methods to translate HACK assembly code into
   HACK CPU instructions
   -----------------------------------------------------------------------
   Written by: Samuel Pell 05-05-16 (dd-mm-yy)
   -----------------------------------------------------------------------
   Contains: translate
             _create_symbol_table
             _translate_into_bin
             _is_A_instruction
             _add_pseudoinstruction_to_table
             _add_symbol_to_table
             _translate_A_instruction
             _translate_C_instruction
"""

import SymbolTable
import AssemblyCleaner

SYMBOL_INDICATOR = "@"
ADDRESS_INDICATOR = "A"
PSUEDOINSTRUCTION_INDICATOR = "("

def translate(file_contents):
    """
       Translates HACK assembly language into HACK CPU code
       Takes a raw assembly file, and returns a list of 
       CPU instructions.
    """
    assembly_instructions = AssemblyCleaner.clean_file(file_contents)
    symbol_table = _create_symbol_table(assembly_instructions)
    assembly_instructions = AssemblyCleaner.remove_psueodinstructions(
                                                  assembly_instructions)        
    cpu_instructions = _translate_into_bin(assembly_instructions, 
                                                 symbol_table)
    return cpu_instructions


def _create_symbol_table(assembly_instructions):
    """
       Takes a list of assembly instructions and finds all the references 
       in the program and assigns them to the symbol table. If it is a 
       user defined label it passes None to the table for tha var.
    """
    symbol_table = SymbolTable.SymbolTable()
    for instruction in assembly_instructions:
        
        if instruction.startswith(SYMBOL_INDICATOR):
            _add_symbol_to_table(instruction, symbol_table)
            
        elif instruction.startswith(PSEUDOINSTRUCTION_INDICATOR):
            _add_pseudoinstruction_to_table(instruction, symbol_table)
            
    return symbol_table
  

def _add_symbol_to_table(instruction, symbol_table):
    """Adds a symbol to the table"""
    if instruction[1:].isnumeric():
        symbol_table[instruction[1:]] = int(instruction[1:])
    else:
        symbol_table[instruction[1:]] = None
    
        
def _add_psuedoinstruction_to_table(instruction, symbol_table):
    """Adds a psuedo instruction to the table so it can be jumped to"""
    if instruction[1:-1].isnumeric():
        symbol_table[instruction[1:-1]] = int(instruction[1:-1])
    else:
        symbol_table[instruction[1:-1]] = None    
                    
                    
def _translate_to_bin(assembly_instructions, symbol_table):
    """Translates each line into CPU instruction"""
    translated_instructions = []
    
    for instruction in assembly_instructions:
        
        if _is_A_instruction(instruction):
            translated_line = _translate_A_instruction(instruction, 
                                                       symbol_table)
        else:
            translated_line = _translate_C_instruction(instruction, 
                                                       symbol_table)
        translated_instructions.append(translated_line)
        
    return translated_instructions
                
                
def _is_A_instruction(instruction):
    """Returns True if instruction is an A instruction"""
    symbol = instruction.startswith(SYMBOL_INDICATOR)
    address_instruction = instruction.startswith (ADDRESS_INDICATOR)
    return symbol or address_instruction


def _translate_A_instruction(instruction):
    """
       Translates an assembly instruction into a HACK CPU 
       A-type instruction
    """
    pass


def _translate_C_instruction(instruction):
    """
       Translates an assembly instruction into a HACK CPU 
       C-type instruction
    """
    pass