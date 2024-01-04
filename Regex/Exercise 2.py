#this imports the regex library
import re 

# the following code collects the file name as user input and initialises a count variable
# the variable b is a temporary storage of the extracted integers
file = input("file name? ")
counter = 0
b = 0

try:
    words = open(file)
except:
    print("File name incorrect or file does not exist")
# the following lines of code finds and extracts the texts that fit the regex argument in the 'findall' method
# the string is extracted and transformed into an integer then a summation is performed till the last value
# the counter variable increases by 1 each time a string is successfully extracted
for i in words:
    l = re.findall('^New Revision: ([0-9]+)',i)
    if len(l) > 0:
        b += int(l[0])
        counter += 1

print(b/counter)


