# takes user input and initialises a dictionary
file = input("input the file name...")
names = dict()
# try-except block to check the validity of the file
try:
    words = open(file)
except :
    print("This isn't a valid file or the file doesn't exist")
    quit()
# finds lines that start with 'From' then splits them
# populates the dictionary with the sender's emails
# updates the dictionary everytime a unique email is found
for line in words:
    line_split = line.split()
    if len(line_split) > 2 and line_split[0] == 'From':
        names[line_split[1]] = names.get(line_split[1], 0) + 1

# compares the values in the dictionary to get the maximum value
# prints the maximum value and the key
max = names[list(names)[1]]
for key in names:
    if names[key] > max:
        max = names[key] 


print(str(list(names.keys())
	[list(names.values()).index(max)]) + ":" + " " + str(max))


