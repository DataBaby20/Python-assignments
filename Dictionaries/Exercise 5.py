# takes user input and initialises a dictionary
file = input("input the file name...")
email_id = dict()
# try-except block to check the validity of the file
try:
    words = open(file)
except :
    print("This isn't a valid file or the file doesn't exist")
    quit()
# splits the lines
# identifies the list that start with 'From' and have more than 2 elements
# the result is further split with the '@' delimiter
# populates the dictionary with the sender's email domain name
# updates the dictionary everytime a unique email domain name is found
for line in words:
    line_split = line.split()
    if len(line_split) > 2 and line_split[0] == 'From':
        line_split = line_split[1].split('@')
        email_id[line_split[1]] = email_id.get(line_split[1], 0) + 1

print(email_id)




