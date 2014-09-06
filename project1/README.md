Description
===========

Write two programs with the following properties:

On a host, called server host, write a program, called password\_holder.c, that allows a user to input a character string.
        
After obtaining an input string from a user, password\_holder.c opens a TCP/IP socket and listens on the socket to wait for any incoming request from a host, called client host.
        
When an incoming connection is established, password\_holder.c sends the input string to the the client host as a password.
        
On a host, called client host, write a program, called mission\_impossible.c, that connects to the above remote server to retrieve a password.
      
The compiled executable file of mission\_impossible.c is called mission\_impossible.exe.
        
After obtaining a password from the above server, mission\_impossible.c asks its users to input a password.
        
If an input password is identical to the passwrod that mission\_impossible.c retrieved from the above server, the program will execute a piece of code, called Mission Briefing Code (MBC) hereafter, that will display the following message ("Ethan Hunt, Run Now!") for 2 minutes and then delete the file mission\_impossible.exe and terminate itself.
        
If an erroneous password is input, the program will delete the file mission\_impossible.c and terminate itself.
        
Initially, MBC must be stored in a global array and is encoded with your password. You can use any approach to encode MBC. When the input password is correct, your program will decode MBC and place it in the heap and then transfer your execution flow to the decoded MBC. 


**This project only can be execue on i386.**

MBCcorrect.asm
--------------
When the code of MBCcorrect.asm been executed, the string "Ethan Hunt, Run Now!" would be print and mission\_impossible.exe would be deleted.

MBCerror.asm 
-------------
When the code of MBCerror.asm been executed, mission\_impossible.c would be deleted immediately.


How to execute MBC code:
	
####Step 1 :

You need to install "nasm" first.If your OS is Ubuntu,you can type

	sudo apt-get install nasm

####Step 2 :

	nasm -f elf32 MBCcorrect.asm -o MBCcorrect.o

####Step 3 :

	ld MBCcorrect.o -o MBCcorrect

####Step 4 :

	./MBCcorrect 

####Step 5 :
Then your file(mission\-impossible.exe) will be deleted



**if there is some error in your asm code, you can use "gdb debugger" to disassmbler.**


How to get the shellcode of MBC 
--------------------------------

You can user the ShellcodeProduct.py to produce the Shellcode::
	
	python ShellcodeProduct.py "your file of asm"


Remark
------

**MBCerror.asm is similary as MBCcorrect.asm**

Shellcode.c is a example to change eip to your shellcode.
You need to let the stack can be execue.i.e. "gcc -z execstack shellcode.c -o shellcode.exe"


decode.asm
----------

It can decode shellcode with key in enshellcode.c by itself.But you need to encode the decode block in decode.asm first.

That is encode 

	"\xeb\x0e\x5a\x4a\x31\xc9\xb1\xf0\x80\x34\x0a\xce\xe2\xfa\xeb\x05\xe8\xed\xff\xff\xff"
to

	"\x25\xc0\x94\x84\xff\x07\x7f\x3e\x4e\xfa\xc4\x00\x2c\x34\x25\xcb\x26\x23\x31\x31\x31"

Then the decode block will be decode when you want to encode your shellcode.When you execue your enshellcode it will be decode by itself,then execue your shellcode.
