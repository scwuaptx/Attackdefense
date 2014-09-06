#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# the prgram will product shellcode form a assembly code
# You can use the command "python shellcodeProduct.py 'your file of asm'" to get the shellcode

import sys,os

def disasm(filename) :
	bistream = []
	stream = os.popen("objdump -d ./" + filename + "| grep '[0-9a-f]:'" ).read().split("\n")
	for i in range(len(stream)-1) :
		line = stream[i].split("\t")
		code = line[1].split()
		bistream = bistream + code
	shellcode = "\\x" +  "\\x".join(bistream)
	return shellcode
if __name__=='__main__' :
	if len(sys.argv) < 2 :
		print "Please input a asmfile"
	else :
		asmfile = sys.argv[1]
		objfile = sys.argv[1].strip(".asm") + ".o"
		exefile = sys.argv[1].strip(".asm")
		os.system("nasm -f elf32 " + asmfile + " -o " + objfile)
		os.system("ld " + objfile + " -o " + exefile)
		print disasm(exefile)

