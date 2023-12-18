
word = 'X-DSPAM-Confidence:0.8475'
#given the string above, the below line of code finds the colon in the text and stores 
#its index as the "colon" variable
colon = word.find(":")
#the line of code below slices the initial string using the "colon" + 1 as the starting index and the 
# length of the text as the end point, transforms it into a float and stores it as the "extract" variable
extract = float(word[colon + 1:len(word)])


