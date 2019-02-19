#Prompts user for day of week
day = int(input("Day (0-6)? "))

#Dictionary to store corresponding day with number
day_number = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

#If statement to check for invalid output or print correct day
if(day >= 7):
    print("Invalid input. ")
else:
    print(day_number[day])