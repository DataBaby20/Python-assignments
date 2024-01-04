# the regex library is imported

import re 

# the file name is taken as user input
file = input("file name? ")
try:
    words = open(file)
except:
    print("File name incorrect or file does not exist")

# the user inputs the regex characters they want to locate in the file
find_word = input("what word do you seeek?: ")

# a counter variable is created and updated everytime a line matches the regex text
counter = 0
for line in words:
    if re.search(str(find_word),line):
        counter += 1
print(counter)
