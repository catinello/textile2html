#!/bin/usr/env python

import sys
#import textile #postponed to convert function to avoid unnecessary loading

#constants
LICENSE = "BSD"
VERSION = "16.DirXmt"
AUTHOR  = "Antonino Catinello"

#functions
def access(filepath):
	''' Check if a file exists and is accessible. '''
	try:
		f = open(filepath, 'r')
		f.close()
	except IOError as e:
		return False

	return True

def convert(text):
	''' Convert textile to HTML. '''
	import textile
	return textile.textile(text)

def main():
	arg_names = ['CMD', 'FILE']
	args = dict(zip(arg_names, sys.argv))

	if len(sys.argv) != 2:
		print(args['CMD'] + " <input.textile>")
		sep   = " | "
		print(" Converter for textile to html format on the command line.")
		print(" " + LICENSE + " License" + sep + u"\N{COPYRIGHT SIGN}" + " 2016 " + AUTHOR + sep + "Version " + VERSION)
		print(" Full credit goes to https://txstyle.org/")
		sys.exit(0)

	if access(args['FILE']):
		with open(args['FILE'], 'r') as f:
			contents = f.read()
			html = convert(contents)
			print(html)
	else:
		print("File " + args['FILE'] + " is not accessible.")
		sys.exit(2)

#entry
if __name__ == "__main__":
	main()
