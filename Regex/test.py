import re 

file = 'Regex/mbox.txt'
counter = 0
b = 0
new_list = list()
try:
    words = open(file)
except:
    print("File name incorrect or file does not exist")
for i in words:
    l = re.findall('^New Revision: ([0-9]+)',i)
    if len(l) > 0:
        b += int(l[0])

        counter += 1
print(b/counter)

