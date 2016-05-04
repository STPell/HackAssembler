"""SAMUEL PELL 16-05-04
   Initialiser for a python hack language assembler
"""
import HackTranslator
import AssemblyCleaner

def get_file(filename):
    """Gets content of a file with file name passed to it"""
    file = open(filename)
    file_contents = file.readlines()
    return file_contents


def output_file(filename, output):
    """Takes a filename and an output and writes them to a file"""
    file = open(filename, "w")
    #finish me Sam
    

def main():
    """Main Function of a HACK Assembler"""
    input_filename = input("Enter the name of the file to translate:> ")
    output_filename = input("Enter the name of the file to output to:> ")
    cleaned_file = AssemblyCleaner.clean_file(input_file)
    translated_file = HackTranslator.translate(cleaned_file)
    output_file(output_filename, translated_file)
    
if __name__ == "main":
    main()