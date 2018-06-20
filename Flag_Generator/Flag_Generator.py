
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Author : Ori0n__
#Team : TheFlagIsNotHere

import pickle
import sys
from termcolor import colored

try:
	import xerox

except:
	print ("No module named 'xerox'")
import sys


syntax =colored("'","red")


def how_to():

	print ("\n[*]Usage:")
	print ("\t[*]python3 Flag_Generator.py: to display help.")
	print ("\t[*]python3 Flag_Generator.py remplace: Change the/this value for the CTF name.")
	print ("\t[*]python3 Flag_Generator.py 'flag': to have your final flag.\n")




def remplace():
	
	user_input = input("[*]Do you want change the syntax ? (Y)es/(N)o\n")

	if user_input.upper() == "Y":
		new_value = input("[*]Enter the new value:\n")

		with open('data', 'wb') as file:
			write_data = pickle.Pickler(file)
			#Save the new value
			write_data.dump(new_value)

	elif user_input.upper() == "N":
		pass

	else:
		print ("\n[*]Usage: python3 Flag_Generator.py "+syntax+"flag"+syntax+"\n")



def copy():

	with open('data', 'rb') as file:

		load_data = pickle.Unpickler(file)
		name_ctf = load_data.load()


	flag = str(name_ctf)+"{"+(sys.argv[1])+"}"
	flag_color = colored(flag,"green")
	xerox.copy(flag, xsel=True)

	print("\n[*]The Flag: "+str(flag_color)+" has been copied in your clipboard.\n")


if __name__ == '__main__':

	try:
		with open('data', 'rb') as file:

			load_data = pickle.Unpickler(file)
			name_ctf = colored(load_data.load(),"blue")
			print("[*]Value: "+str(name_ctf))
			
	except:
		pass


	if len(sys.argv) == 1:
		how_to()
	elif sys.argv[1] == "remplace":
		remplace()
	elif len(sys.argv) == 2:
		copy()
	

	else:
		print ("\n[*]Usage: python3 Flag_Generator.py "+syntax+"flag"+syntax+"\n")
