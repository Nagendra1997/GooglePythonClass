#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir_path):
	abs_path_list=[]
	filenames=os.listdir(dir_path)
	for filename in filenames:
		special_match=re.search(r'__\w+__',filename)
		if special_match:
			abs_path_list.append(os.path.abspath(os.path.join(dir_path, filename)))
	
	return abs_path_list
	
	
def copy_to(source_path_list,dest_dir):
	for file_path in source_path_list:
		shutil.copy(file_path,dest_dir)
		
	cmd = 'ls -l ' + dest_dir
	(status, output) = commands.getstatusoutput('ls -l ' + dest_dir)
	if status:
		sys.stderr.write(output)
		print "Error in copying files"
		sys.exit(status)
	
	print output
	print '\n\tSucesssssssss!!!'
	
	
def zip_to(source_path_list,zip_path):
	print 'Your wish is my command\n\n'
	print 'Command I am going to do:zip -j'+' '+zip_path+ ' '+' '.join(source_path_list)
	(status, output) = commands.getstatusoutput('zip -j'+' '+zip_path+ ' '+' '.join(source_path_list))
	if status:
		sys.stderr.write(output)
		print "Error in zipping files"
		sys.exit(status)
	
	print output
	print '\n\t Go zippin yo!!!'
	

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for arg in args:
    if todir:
    	copy_to(get_special_paths(arg),todir)
    if tozip:
    	zip_to(get_special_paths(arg),tozip)
  
if __name__ == "__main__":
  main()
