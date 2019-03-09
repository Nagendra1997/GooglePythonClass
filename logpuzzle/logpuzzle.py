#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  puzzle_url_list=[]
  f=open(filename,'r')
  for line in f:
  	  puzzle_url=re.search(r'GET (\S+/puzzle/\S+) HTTP',line)
  	  if puzzle_url:
  	  	  if puzzle_url.group(1) not in puzzle_url_list:
  	  	  	  puzzle_url_list.append(puzzle_url.group(1))
  
  	  
  puzzle_url_list.sort(key=find_anything_special)
  server_name='http://'
  server_name_search=re.search(r'_(\S+)',filename)
  if server_name_search:
  	  server_name+=server_name_search.group(1)

  	  
  for i,each_url in enumerate(puzzle_url_list):
  	  puzzle_url_list[i]=server_name+each_url
  
  return puzzle_url_list
  
  
  

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  if not os.path.exists(dest_dir):
  	  os.mkdir(dest_dir)
  
  for i,url_id in enumerate(img_urls):
  	  file_name='img'+str(i)
  	  file_dir_path=os.path.join(dest_dir,file_name)
  	  print 'retrieveing img'+str(i)
  	  urllib.urlretrieve(url_id,file_dir_path)
  	 
  create_indexfile(dest_dir)
  

def find_img_id(img_name):
	return int(img_name[3:])
	
def find_anything_special(url_id):
	match=re.search(r'-\w+-(\w+).jpg',url_id)
	if match:
		return match.group(1)
	else:
		return url_id[0]
		
def create_indexfile(dest_dir):
	dest_dir='/home/nagendra/gpe/logpuzzle/secretimage'
	img_file_list=os.listdir(dest_dir)
	img_file_list.sort(key=find_img_id)
	
	#Descrambling
	
	
	f=open(dest_dir+'index.html','w')
	f.write('<verbatim>\n<html>\n<body>\n')
	
	for file_name in img_file_list:
		f.write('<img src="'+dest_dir+'/'+file_name+'">')
	f.close()
	
	
	
	
def main():
  
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
