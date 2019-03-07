#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++

  f=open(filename,'r')
  f_str=f.read()
  f.close()
  year_search=re.search(r'Popularity in (\d\d\d\d)',f_str)
  year=0
  if year_search:
  	  year=year_search.group(1)
  	  
  rank_names=re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',f_str)
  names_dict={}
  names_list=[(rank_tuple[0],rank_tuple[i]) for i in [1,2] for rank_tuple in rank_names]
  # print len(names_list)
  
  # sys.exit(0)
 
  for each_tuple in names_list:
  	  name=each_tuple[1]
  	  rank=each_tuple[0]
  	  if name in names_dict.keys() and rank<=names_dict[name]:
  	  	  names_dict[name]=rank
  	  elif name not in names_dict.keys():
  	  	  names_dict[name]=rank
  	 
  names_rank_list=[name+' '+str(names_dict[name]) for name in sorted(names_dict.keys())]
  names_rank_list.insert(0,str(year))
  return names_rank_list 


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  yearwise_namerank_data=[]
  yearwise_namerank_data=[extract_names(filename) for filename in args]
  
  #listoflists
  if summary==False:
  	  for yearwise_data in yearwise_namerank_data:				#each year list
  	  	  for namerank in yearwise_data:		 #list item in yearwisedatalist
  	  	  	  print namerank
  	  	  	  
  else:
  	  for yearwise_data in yearwise_namerank_data:				#each year list
  	  	  yearwise_summaryfile='baby'+str(yearwise_data[0])+'.html.summary'
   	   	  f=open(yearwise_summaryfile,'w')
   	   	  f.write('\n'.join(yearwise_data)+'\n')
   	   	  f.close()
   	   	  
  	  	 
  	  	
   	   
      
      
if __name__ == '__main__':
  main()
