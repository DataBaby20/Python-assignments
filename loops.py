## this creates a list
num_list = []
print("Kindly input 'done' once you wish to see your results!")
## the while loop iterates through the following conditions
while True:
    ## collects user input
    num = input("Enter a number:")
    ##checks if user is done giving input then performs the sum, count and average calculations and ends code
    if num == "done":
        total = sum(num_list)
        count = len(num_list)
        average = total/count
        print("the sum, count and average are: ", total, count, average)
        break
    ## this runs if the user is still giving input
    else:
    ## this throws a custom error if the input isn't an integer
        try:
            num = int(num)
        except:
            print("input valid integer")
            quit()
    ##if no error is thrown then the list is updated with any new values and the loop continues
        num_list.append(num)

            
        

    
    
    
