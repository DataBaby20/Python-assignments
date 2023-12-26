
#Exercise 4: this turns all the text in the hardcoded file into uppercase by iterating through each line
new_file = open("file_operations/mbox-short.txt")
for line in new_file:
    print(line.upper())

#Exercise 5: this takes in user input of a file name and locates the series of strings of form 
# "X-DSPAM-Confidence", selects the attached value after the colon and performs basic operations 
prompt = input("Enter file name:")
# this stores all the numeric results
conf = []
#this throws a custom error incase a nonexistent file is requested
try:
    newer_file = open(prompt)
except:
    print("can not open this file")
    quit()
#this iterates through all the lines in the text and identifies all the text that starts with 
# "X-DSPAM-Confidence", finds the numbers after the colon, changes them to float and stores them 
# as the "extract" variable and in the list "conf"
for line in newer_file:
    if line.startswith("X-DSPAM-Confidence"):
        colon = line.find(":")
        extract = float(line[colon + 1:len(line)])
        conf.append(extract)
#this computes the average confidence
avg = sum(conf)/len(conf)

print("The average confidence is" + ' ' + str(avg))

