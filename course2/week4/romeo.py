# Jim R
# Open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words 
# using the split() method. The program should build a 
# list of words. For each word on each line check to 
# see if the word is already in the list and if not append 
# it to the list. When the program completes, sort and 
# print the resulting words in alphabetical order. 

# request file from user
fname = input("Enter file name:")
# get handle on file
fh = open(fname)
# create list
lst = list()
finalList = list()
# loop through file by line and split the line into a list
for line in fh:
    line = line.rstrip() # strip trailing \n
    lst = line.split() # split line into list of words
    for ind in lst: # loop through the line (list)
        if ind not in finalList:
            finalList.append(ind) # append words not already in the final list
        else: continue
# sort the final list        
finalList.sort()
# print the final sorted list
print(finalList)
