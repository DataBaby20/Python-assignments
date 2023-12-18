
# EXERCISE 4
# open the "romeo.txt" file
# create a list called "words"
# iterate through the lines in the text and split it into lists
# iterate over the created lists and check if the words exist in the "words" list
# if they do not, add the words to the "words"m list
# sort and print the list

romeo = open("romeo.txt")
words = list()
for line in romeo:
    line = line.split()
    for word in line:
        if word not in words:
            words.append(word)

#words.sort()
#print(words)

# EXERCISE 5
# this opens and reads, line-by-line, the mail file
# this iterates over each line and finds the ones that start with "from"
# it identifies the sender by splitting and locating the second word using its index of 1
#it counts the number of times a line starting with "From" is found

mbox = open("mbox-short.txt")
count = 0
for line in mbox:
    if line.startswith("From"):
        count += 1
        line = line.split()
        print(line[1])
print(count)

#EXERCISE 6
# a list called numbers is created
# user input is collected
# the input is validated as an integer, if it is not, a custom error is thrown
# the numbers list is updated until the user is done
# the max and min values are printed

numbers = list()
while True:
        user_input = input("Enter a value. Type 'done' when you are done:")
        if user_input == "done":
             
             print("Maximum:" + ' ' + str(max(numbers)))
             print("Minimum:" + ' ' + str(min(numbers)))
             break
        else:
        
            try:
                user_input = int(user_input)
            except:
                print("input a valid integer or 'done'")
                quit()
            numbers.append(user_input)
        



