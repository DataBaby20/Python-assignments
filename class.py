hours = input("How many hours did you work this week?: ")
base_pay = 12.5

def git(hours, base_pay):
    try:
        hours = int(hours)
    except:
        print("input a valid amount")
        quit()
    if hours <= 40 and hours >= 0:
         total_comp = (hours * base_pay)
         print("total compensation is " + str(total_comp))
    elif hours < 0:
        print("no negatives")
        quit()
    else:
        ovt = hours - 40
        ovt_pay = ovt*1.5*base_pay
        total_comp = (40*base_pay) + ovt_pay
        print("total compensation is " + str(total_comp))

git(hours, base_pay)
    
