"""
   Main
   Initialiser for a python hack language assembler.
   -----------------------------------------------------------------------
   Written by: Samuel Pell 04-05-16 (dd-mm-yy)
   -----------------------------------------------------------------------
   Contains: main
             get_file (temp)
             output_file (temp)   
   -----------------------------------------------------------------------          
   Notes: File name entry to be replaced with a GUI version later.
"""

import HackTranslator
import AssemblyCleaner


def get_file(filename):
    """Gets content of a file with file name passed to it"""
    file = open(filename)
    file_contents = file.readlines()
    file.close()
    return file_contents


def output_file(filename, output):
    """Takes a filename and a list of lines and writes them to a file"""
    file = open(filename, "w")
    [file.write(s+"\n") for s in output]
    file.close()
    

def main():
    """Main Function of a HACK Assembler"""
    input_filename = input("Enter the name of the file to translate:> ")
    output_filename = input("Enter the name of the file to output to:> ")
    try:
        input_file = get_file(input_filename)
        cleaned_file = AssemblyCleaner.clean_file(input_file)
        translated_file = HackTranslator.translate(cleaned_file)
        output_file(output_filename, translated)        
    except FileNotFoundError:
        print("Error. Input file not found.")
    
    
if __name__ == "__main__":
    main()