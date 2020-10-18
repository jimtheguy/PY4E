# Jim R
# Write a program that prompts for a file name, then opens that file 
# and reads through the file, looking for lines of the form:

# X-DSPAM-Confidence:    0.8475

# Count these lines and extract the floating point values 
# from each of the lines and compute the average of those 
# values and produce an output as shown below. Do not use 
# the sum() function or a variable named sum in your solution. 

# Get the filename from the user
fname = input("Enter file name:")
fhandle = open(fname)
# loop through file
count = 0
total = 0.0
for line in fhandle:
# search for the form mentioned in line 4
    if not line.startswith("X-DSPAM-Confidence:"): continue
    else:
        count = count + 1 #increase the count for average calculation
        decAsString = line[line.find("."):] # slice out the decimal
        decAsString = decAsString.rstrip() # strip newlines
        decAsFloat = float(decAsString) #convert to float
        total = total + decAsFloat # running total of decimals
average = total / count # calculate average
#print the average
print("Average spam confidence:", average)



