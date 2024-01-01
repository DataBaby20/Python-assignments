# this opens and reads a file based on user input and throws a custom error if the file does not exist
file = input("input the file name...")
hours = dict()
commits = list()
try:
    words = open(file)
except :
    print("This isn't a valid file or the file doesn't exist")
    quit()

# this splits the lines of the file into lists and identifies the lines that begin with "From" and have more than 5 elements
#a dictionary containing key-value pairs of hours-count is created
# a list of tuples containing the aforementioned key-value pairs is created
# the list is sorted giving a list of tuples in ascending order of count
for i in words:
    line = i.split()
    if len(line) > 5 and line[0] == "From":
        line = line[5].split(":")
        hours[line[0]] = hours.get(line[0], 0) + 1
for hours, count in hours.items():
    commits.append((hours, count))
for hours, count in sorted(commits, reverse=False)[:]:
    print(hours, count)


        
