# Jim R
# Write a program to read through the mbox-short.txt and 
# figure out who has sent the greatest number of mail 
# messages. The program looks for 'From ' lines and takes 
# the second word of those lines as the person who sent the 
# mail. The program creates a Python dictionary that maps 
# the sender's mail address to a count of the number of times 
# they appear in the file. After the dictionary is produced, 
# the program reads through the dictionary using a maximum 
# loop to find the most prolific committer.

# get file name from user and get handle on it to open
fn = input("Enter file name: ")
if len(fn) < 1 : fn = 'mbox-short.txt'
mbox = open(fn)
di = {}
for line in mbox:
    line = line.lower().split() # split for every line and make lowercase
    try:
        if line[0] == 'from':
            di[line[1]] = di.get(line[1],0) + 1 # increment counter
    except:
        pass
#print(di)
# determine the frequency of each sender and sort descending
freq = []
for key, val in di.items():
    freq.append((val, key))
freq.sort(reverse=True)

print(freq[0][1], freq[0][0])

