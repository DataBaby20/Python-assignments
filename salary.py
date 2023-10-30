# user input is collected stating the number of hours worked in a week
hours = input("How many hours did you work this week?: ")
wage = 12.5

# the payment function takes hours worked and the wages per hour as its arguments
def salary(hours, wage):
# this checks if the input is a valid integer and throws a custom error if not
    try:
        hours = int(hours)
    except:
        print("input a valid amount")
        quit()
#the following conditionals check if the hours worked are negative values, exactly 40 hours or above 40
    if hours <= 40 and hours >= 0:
         total_comp = (hours * wage)
         print("total compensation is " + str(total_comp))
    elif hours < 0:
        print("no negatives")
        quit()
    else:
#this computes the overtime py based on increased pay rate of 1.5 times the normal rate
        ovt = hours - 40
        ovt_pay = ovt*1.5*wage
        total_comp = (40*wage) + ovt*1.5*wage
        print("total compensation is " + str(total_comp))

salary(hours, wage)
    
