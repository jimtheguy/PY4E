# Jim R
# Write a program to read through the mbox-short.txt and figure 
# out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the 
# time and then splitting the string a second time using a colon. 

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the 
# counts, sorted by hour as shown below.

# obtain file from user and create handle
file = input("Enter file name: ")
if len(file) < 1 : file = 'mbox-short.txt' # auto assign for testing
fh = open(file)
times = []
hours = {}
for line in fh: #loop through lines in file
    line = line.lower().split() #make lowercase and split lines
    try:
        if line[0] == 'from': #isolate lines beginning in 'from'
            times = line[5] #extract the time from each line
            tmp = times.split(':') #split times and save into temp var
            hours[tmp[0]] = hours.get(tmp[0],0) + 1 #extract hour from tmp and count instances
    except:
        pass
# print the frequency for each hour sorted by hour
for i in sorted(hours):
    print(i, hours[i])

