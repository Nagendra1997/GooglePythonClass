#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###
def setup(filename):
	f=open(filename,'rU')
	word_list=[word.lower() for line in f for word in line.split()]
	word_list.sort()
	word_count_dict={}
	for word in word_list:
		if word.isalpha():
			if word not in word_count_dict.keys():
				word_count_dict[word]=0
			word_count_dict[word]+=1
			#milestone--1
			
	return word_count_dict
	
	

def print_words(filename):
	word_count_dict=setup(filename)
	for word,count in word_count_dict.items():
		print '%10s %10s' %(word,count)

def print_top(filename):
	word_count_dict=setup(filename)
	# top_sorted_word_count_dict=sorted(word_count_dict,reverse=True,key=word_count_dict.get)
	#ref itemgetter ,lambda function over typles
	top_words_list=sorted(word_count_dict.items(),key=lambda x:x[1],reverse=True)
	for item in top_words_list[:20]:
		print '%10s %10s' %(item[0],item[1])
	
	print('\n'*3)
	top_20_commons=[
		'the', 'be', 'to', 'of', 
		'and', 'a', 'in', 'that',
		'have', 'it', 'for', 'not', 
		'on', 'with', 'he', 'as', 
		'you', 'do', 'at']
		
	for word in top_words_list[:20]:
		if word[0] not in top_20_commons:
			print word[0]
	
	


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
