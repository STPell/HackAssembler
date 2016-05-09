// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

//Code by Samuel Pell 01-05-16 (dd-mm-yy)
//Note: Will not run unless 16348 in MEM[0] and 24576 in MEM[1]
(KEY)
//RESET VARIABLES
@0
D = M
@b
M = D
@i
M=0
//KEYBOARDCONTROL
@KBD
D=M
@DEC //Jumps to decision script
D;JGT
@KEY
0;JMP

(DEC) //DECISION SCRIPT
@2
D=M
@c
D=D-1
@WHT
D;JEQ
@BLACK
D;JLT

(BLACK) //BLACKOUT SCREEN
@b	//set A to -1
D=M	
A=D
M=-1
@b  //b = b + 1
M=D+1
@b //check if screen filled (ie. b >=24576)
D=M
@1 
D=D-M
@KEY
D;JEQ
@2 //set RAM[2] to 1 to let decision script know the screen is blacked out
M=1
@BLACK
0;JMP

(WHT) //WHITEOUT SCREEN
@b	//set A to 0
D=M	
A=D
M=0
@b  //b = b + 1
M=D+1
@b //check if screen emptied (ie. b >= 24576)
D=M
@1
D=D-M
@KEY
D; JEQ
@2 //set RAM[2] to 0 to let decision script know the screen is blacked out
M=0
@WHT
0;JMP



