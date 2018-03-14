#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
import sys, os, gzip, sqlite3

# Troubleshooting CGI
cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
user_input = form.getvalue('input_seq')
print "Content-type:text/html\r\n\r\n"

with open('input_file.faa', 'w') as tmp_file:
        print(">id1", file=tmp_file)
        print(user_input, file=tmp_file))
        
# find user_input in BLAST db
blast_run = "blastp -query input_file.faa -db dinoAa -evalue 1e-10 -out dino.blastp -num_descriptions 10 -num_alignments 5 -num_threads 4"
os.system(blast_run)
print('running blast')

# result: print top hit fom BLAST search output
# take top hit's accession number
# search for corresponding data e.g. goterm, pfam id in sqlite table

print('ready for connection')
conn = sqlite3.connect('SwissProt.sqlite') # Make a connection object
print('printing connection')
cursorObject = conn.cursor()
print('printing cursor_obj')
statement = "SELECT accnr, sequence FROM taxonomy, swissprot WHERE swissprot.taxid = taxonomy.taxid AND taxonomy.tax_path LIKE '%%%s%%';" % (user_input)
print(statement)
#cursorObject.execute(statement)
for row in cursorObject.execute(statement):
        print(row)
#print("\t".join(map(str, row)))
print "%s" % (user_input)
