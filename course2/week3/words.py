# Jim R
# Write a program that prompts for a file name, then 
# opens that file and reads through the file, and print 
# the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

#Get filename from user
fname = input("Enter file name:")
fhandle = open(fname)

#loop through lines in the file, srip \n and capitalize, then print
for line in fhandle:
    line = line.rstrip().upper()
    print(line)