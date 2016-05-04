"""
   Assembly Cleaner
   Cleans the Hack Assembly language so the HackTranslator module can then
   translate it
   -----------------------------------------------------------------------
   Written by: Samuel Pell 04-05-16 (dd-mm-yy)
   -----------------------------------------------------------------------
   Contains: clean_file
             _strip_non_instructions
             _strip_comments
             _strip_whitespace
             test_module
"""

COMMENT_INDICATOR = "//"


def clean_file(file_contents):
    """
       Cleans a hack assembly file so it can be translated.
       Takes a list lines to clean and returns a list of 
       cleaned lines.
    """
    commentless_file = _strip_comments(file_contents)
    brackets_removed = _strip_non_instructions(commentless_file)
    assembly_code = _remove_whitespace(brackets_removed)
    return assembly_code


def _strip_non_instructions(file_contents):
    """Removes all lines begining with open bracket"""
    return [line for line in file_contents if not line.startswith("(")]


def _remove_whitespace(file_contents):
    """
       Strips all the whitespace from a list of strings 
       and removes empty strings from the list
    """
    whitespace_stripped = [line.strip() for line in file_contents]
    return [line for line in whitespace_stripped if line != ""]    


def _strip_comments(file_contents):
    """Strips all the comments from a file"""
    lines_without_comments = []
    for line in file_contents:
        comment_position = line.find(COMENT_INDICATOR)
        if comment_position != -1:
            lines_without_comments.append(line[:comment_position])
        else:
            lines_without_comments.append(line)
    return lines_without_comments


def test_module():
    """Tests the module to make sure it works properly"""
    print("-------Testing Module-------")
    
    test_string = ["//Remove Me", "(Me Too)", "But leave me", 
                   "and most of me //just this bit",
                   "Don't forget //this aswell", "     "]
    print("--Original--")
    print(test_string)
    print("--Cleaned--")
    print(clean_file(test_string))
    

if __name__ == "__main__":
    test_module()