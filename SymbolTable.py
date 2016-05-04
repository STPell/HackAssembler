"""
   Symbol Table Data Structure
   Data Structure for the symbol table for a HACK assembler.
   -----------------------------------------------------------------------
   Written by: Samuel Pell 5-05-16 (dd-mm-yy)
   -----------------------------------------------------------------------
   contains: SymbolTable
"""

DEFAULT_SYMBOL_TABLE = {
                        "SP" : 0, "LCL" : 1, "ARG" : 2, "THIS" : 3,
                        "THAT" : 4, "SCREEN" : 16384, "KBD" : 24576,
                        "R0" : 0, "R1" : 1, "R2" : 2, "R3" : 3, 
                        "R4" : 4, "R5" : 5, "R6" : 6, "R7" : 7,
                        "R8" : 8, "R9" : 9, "R10" : 10, "R11" : 11,
                        "R12" : 12, "R13" : 13, "R14" : 14, "R15" : 15
                       }
VAR_START_ADDRESS = 16

class SymbolTable(dict):
    """
       A data structure to use for a Symbol Table designed for a HACK
       language translator. Based on the dictionary data structure
       
       Methods: __init__
                __setitem__
                __get_item__
                _add_symbol
                __repr__
       Attributes:
                var_assigned
                symbols
    """
    
    
    def __init__(self):
        """Initialiser for the symbol table"""
        self.symbols = DEFAULT_SYMBOL_TABLE.copy()
        self.var_assigned = 0
        
        
    def _add_symbol(self, symbol, address):
        """Adds a symbol to the table, if it does not already exist"""
        if symbol in self.symbols:
            return None
        
        if address is None:
            address = self.var_assigned + VAR_START_ADDRESS
            self.var_assigned += 1
            
        self.symbols[symbol] = address
        
        
    def __setitem__(self, symbol, address):
        """
           Overwrites the __setitem__ function of the dict structure.
           Takes a symbol and an address which is either an integer 
           or None.
        """
        self._add_symbol(symbol, address)
        
        
    def __getitem__(self, symbol):
        """Overwrites the __getitem__ function fo the dict structure.
           Takes string and returns the address it corresponds to if 
           it exists. If it doesn't raises a KeyError.
        """
        if symbol in self.symbols:
            return self.symbols[symbol]
        else:
            raise KeyError
        
    
    def __repr__(self):
        """Returns a string of the symbol table for printing"""
        return str(self.symbols)