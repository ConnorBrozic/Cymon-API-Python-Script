#!/usr/bin/python
#SRT411 Assignment 2 - Part 2
#Cymon API Interaction
#Written by: Connor Brozic
#Malware Domains retrieved from https://malwaredomains.usu.edu/
#Implements Cymon API Calls

#Import time for sleep function.
#Import Cymon to allow for Cymon API calls

import time
from cymon import Cymon
#Personal Key Removed.  Replace 'xxx' with your own key.
api = Cymon('xxx')

#Parsing Text file retrieved from:
#http://stackoverflow.com/questions/6277107/parsing-text-file-in-python

#Open malware domain file.
f = open('TestedMalwareDomains.txt','r')
#Open output file to write to
cymondata = open('cymondata.txt','w')
while True:
   try:
      #Read the next domain in file.
      text = f.readline()
      print(text)
	  #Lookup the domain through Cymon and print results back to output file.
      cymondata.write(repr(api.domain_lookup(text)))
      cymondata.write("\n")
      cymondata.write("\n")
   #If 404 error encountered, skip domain and move to the next one.
   except Exception:
      pass
   time.sleep(1)

#Once finished, close the connection.
cymondata.close()

