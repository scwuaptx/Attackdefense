#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# the prgram will product shellcode form a completed assembly code
# You can use the command "python shellcodeProduct.py 'your program'" to get the shellcode

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
	print disasm(sys.argv[1])

