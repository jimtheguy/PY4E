# Jim R
# In this assignment you will read through and parse a file 
# with text and numbers. You will extract all the numbers in the 
# file and compute the sum of the numbers. 

# The basic outline of this problem is to read the file, look for 
# integers using the re.findall(), looking for a regular expression 
# of '[0-9]+' and then converting the extracted strings to integers 
# and summing up the integers. 

# import regex
import re
# open the file
with open('adata.txt') as f:
    file_name = f.read()
total = 0
# find all numbers and put them in a list named hit using regex
hit  = re.findall('[0-9]+', file_name)
hit = [int(i) for i in hit] #convert the strings to integers
total = sum(hit) #sum the integers
print(total)

