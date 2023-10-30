This is a repository of all the Pyhton assignments given in the [*Python for Everybody Specialisation held on Coursear taught by Charles Russell Severance*](https://www.coursera.org/specializations/python). Below are a list of the projects and an explanation of their purpose.

## 1. Salary Calculator:
This program calculates the total weekly pay of its user by multiplying the fixed hourly wage rate by the number of hours worked. In the even that the user works more than the usual 40 hours, the code computes an increased wage rate of 1.5 times the normal wage rate and thus leads to a higher compensation for any overtime work done.

Total_weekly_pay = total_hours_worked(less than or exactly 40 hours) * wage_rate
in the event of overtime:
Total_weekly_pay = [(total_hours_worked - 40)* 1.5*wage_rate]  + (40*wage_rate)

The above is a basic explanation of the code's purpose. Additionally, it throws a custom error using the "try-except" conditionals if the input from the user is a non-integer and it also throws an error if the input is a negative value. The program was written to solidify my knowledge on functions, variables and conditionals.