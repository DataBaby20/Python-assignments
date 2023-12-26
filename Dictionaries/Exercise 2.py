#This takes the filename the as the input from the user
# the try-except condition checks if its a valid file; if it isn't it throws a custom error
# the 'days' dictionary is initialised
# the words in the text file are split and identified if they start with a 'From'
# the code checks to see if the days of the week exist in the dictionary and populates the dictionary
# if it exists, the dictionary is updated.

file = input("input the file name...")

try:
    words = open(file)
except :
    print("This isn't a valid file or the file doesn't exist")
    quit()

days = dict()

for line in words:
    line_split = line.split()
    if len(line_split) > 3 and line_split[0] == 'From':
        days[line_split[2]] = days.get(line_split[2], 0) + 1

print(days)







 