# -*- coding: utf-8 -*-
#!usr/bin/python2.7 
# No script kiddies please!!
# Author Rh077king
# CYBER KING SQUAD
#Line + Duplicate Remover 
import os, sys, codecs
from platform import system
if system() == 'Linux':
	os.system('clear')
if system() == 'Windows':
	os.system('cls')
print ("""\033[1;32;40m


 ##################################################################
 ##      CYBER KING SQUAD Line Remover + Duplicate Remover       ##
 ##        Author  :    Rh077king                                ##
 ##        Facebook:    https://www.facebook.com/Rh077King       ##
 ##        Telegram:    https://t.me/Rh077king                   ##
 ##################################################################
   
\n""")
try:
    File = raw_input("\n\033[91mEnter Text File \033[97m:~# \033[97m")
    outfile = raw_input("\n\033[91mEnter Outfile File Name \033[97m:~# \033[97m")
    word = raw_input("\n\033[91mEnter Remove Text\033[97m:~# \033[97m")

    with open(File, 'r') as fr:
        lines = fr.readlines()
        with open(File, 'w') as fw:
            for line in lines:

                if line.find(word) == -1:

                    fw.write(line)
    lines_seen = set() 
    outfile = open((outfile) + ".txt", "w")
    for line in open(File, "r"):
         if line not in lines_seen: 
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()

    print ("""\033[1;32;40mDeleted[ Check Your Output File Dear ] [ Stay_With_CKS ]\n""")

except:
    
    print("")
    print ("""\033[1;32;91m[ something error!! ] [ Stay_With_CKS ]\n""")
