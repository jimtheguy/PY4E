# Jim R
# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line: 

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# You will parse the From line using split() and print out 
# the second word in the line (i.e. the entire address of 
# the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 
# 'From:'. Also look at the last line of the sample output 
# to see how to print the count.

# Get the file from the user
fname = input("Enter the file name:")
# Get a handle on the file
fh = open(fname)
# Loop through the file by line
count = 0
linesplit = list()
for line in fh:
    if line.startswith("From:"): continue # ignore lines with From:
    elif not line.startswith("From"): continue # ignore stuff we don't want
    else:
        linesplit = line.split() # split the line into a list
        print(linesplit[1]) # isolate and print email address
        count = count + 1 # increment the count
# print out the count
print("There were", count, "lines in the file with From as the first word")