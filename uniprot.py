#!usr/bin/env python3
import sys
import re
import urllib.request
import gzip
import os # for terminal inputs

'''
  Title: uniprot.py
  Date: 2018-03-16
  Author(s): Nazeefa Fatima

Description:

SQL table is SwissProt.sqlite

  a) The program retrieves data from the Uniprot database
  b) filters out on Dinoflagellates
  c) filters protein sequences of dinoflagellate species, 
  d) creates .faa file
  e) creates BLAST database based on the .faa file
  f) on web interface, take protein sequence as input
  g) looks for sequences containing the input (e.g. protein residues) BLAST database
  h) print top hit from BLAST search output
  i) take top hit and search for corresponding data in sqlite table
  j) print data from table

List of functions:

List of "non-standard" modules:
  None.

Procedure:

grep -B17 '(Dinoflagellate)' uniprot_sprot.dat (get 17 lines before dinoflagellates)
grep -B17 '(Dinoflagellate)' uniprot_sprot.dat | grep -c '^AC'

-> if sequence begins with 10 capital letters read line until // appears

# # url = urllib.request.urlopen('ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz')
# # To extract the filename from the above URL we can write a filename which fetches the last string after backslash (/).
# # wb indicates that the file is opened for writing in binary mode
# if re.search('/', url):
#     filename = url.rsplit('/', 1)[1]

// 

# Download UniProt database
print('Downloading UniProt Database')
handle = urllib.request.urlopen('ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.fasta.gz')

    with open('response', 'wb') as out:
        while True:
            data = handle.read()
            if len(data) == 0: break
            out.write(data)

# Extract uniprot database
handle = gzip.GzipFile('handle')
with open('uniprot_sprot.dat', 'wb') as out:
    line = out.readlines()

//

select accnr, sequence from taxonomy, swissprot where swissprot.taxid = taxonomy.taxid and taxonomy.tax_path like "%Dino%";

use flask to get 

Usage:
        ./uniprot.py

'''
