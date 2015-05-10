#!/usr/bin/python

#Two arguments input to the file
#Arg 1 should be the name of the PDF file containing seat numbers
#Arg 2 should be the name of the PDF file with questions (if applicable)

'''
Two ways I thought this can be done ! 

1) Create a PDF with randomized seat-numbered pages. Print them. Print 95(no. of students) STAPLED copies of the question paper.
	1 more round of stapling seat numbers on the (already) stapled question papers. (only 1 argument)
	This is mainly to use the printer which can also staple the sheets.

2) Create a PDF where there is a seat number followed by the question paper. Print. This would print out everything in the order
	required. But you will have to FIND and staple every set. If x has the number of pages in the question paper,
	you will have to find and staple every (x+1) pages manually.
	
'''


import sys
import random

from pyPdf import PdfFileWriter, PdfFileReader

# read input pdf and instantiate output pdf
output = PdfFileWriter()
input1 = PdfFileReader(file(sys.argv[1],"rb"))		#Name of file with seat numbers
#input2 = PdfFileReader(file(sys.argv[2],"rb"))		#Name of file with questions

# construct and shuffle page number list
pages = list(range(input1.getNumPages()))
random.shuffle(pages)

# add the new sequence of pages to output pdf
for page in pages:
    output.addPage(input1.getPage(page))
    '''							
    for qpage in list(range(input2.getNumPages()):	#To add qpaper after each seat-numbered page
    	output.addPage(input2.getPage(qpage))
    '''

# write the output pdf to file
outputStream = file(sys.argv[1]+'-mixed.pdf','wb')
output.write(outputStream)
outputStream.close()
