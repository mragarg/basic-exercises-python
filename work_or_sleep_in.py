#Prompts user for day of week
day = int(input("Day (0-6)? "))

# day_number = {
#     0: "Sunday",
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday"
# }

#If statement to see if sleep in, go to work, or invalid
if(day == 0 or day == 6):
    print("Sleep in.")
elif(day >= 1 and day <= 5):
    print("Go to work.")
else:
    print("Invalid input.")