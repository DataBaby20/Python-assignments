# this opens and reads a file based on user input and throws a custom error if the file does not exist
file = input("Input file name: ")
letters = dict()
commits = list()
try:
    words = open(file)
except :
    print("This isn't a valid file or the file doesn't exist")
    quit()

# the following lines of code turns the lines in the file into lower case and splits them
# the code then iterates through every character in the file and validates if they are an alphabet
# if "True", a dictionary of "letter-count" key-value pairs is created
#a list containing the aforementioned key-value pairs is reverse order is created
# the list is then sorted creating a list of tuples ordered in descending order of count
for i in words:
    i = i.lower()
    line = i.split()
    for j in line:
        for k in j:
            if k.isalpha():
                letters[k] = letters.get(k, 0) + 1
for letter, count in letters.items():
    commits.append((count, letter))
for count, letter in sorted(commits, reverse = True):
    print(letter, count)




