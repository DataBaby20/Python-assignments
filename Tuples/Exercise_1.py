# this opens and reads a file based on user input and throws a custom error if the file does not exist
file = input("input the file name...")
names = dict()
commits = list()
try:
    words = open(file)
except :
    print("This isn't a valid file or the file doesn't exist")
    quit()

# this splits the lines of the file into lists and identifies the lines that begin with "From"
#a dictionary containing key-value pairs of email-count is created
# a list of tuples containing the aforementioned key-value pairs is created
# the list is sorted in descending order giving a list of tuples arranged based on the largest count
for i in words:
    line = i.split()
    if len(line) > 2 and line[0] == "From":
        names[line[1]] = names.get(line[1], 0) + 1
for email, count in names.items():
    commits.append((count, email))
for count, email in sorted(commits, reverse = True)[:1]:
    print(email, count)
        
