# Ainur
# 10/15/2023
# tells you the day of the week you will return on

days_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

start = int(input("Please enter starting day number: "))
stay = int(input("Please enter length of your stay: "))
return_number =(start + stay) % 7
return_day = (days_week[return_number])

print("You going to return on " + str(return_day))