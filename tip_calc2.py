#Prompting user's input for bill and service level
invalid_number = True
while(invalid_number):
    total_bill = input("Total bill amount? ")
    try:
        total_bill = float(total_bill)
        invalid_number = False
    except:
        pass

service_level = input("Level of service (good, fair, bad) ? ").lower()
#While loop to check for valid input
valid_input = False
while(valid_input != True):
    if(service_level == "good" or 
    service_level == "fair" or
    service_level == "bad"):
        valid_input = True
    else:
        service_level = input("Invalid input, please try again: ")

split_amount = float(input("Split how many ways? "))

#Dictionary to store values corresponding to service level
service_scale = {
    "good": 0.20,
    "fair": 0.15,
    "bad": 0.10
}

#Variables to calculate tip and add to total_bill
tip_amount = service_scale[service_level] * total_bill
total_bill += tip_amount

#Print final answers
print("Tip amount: %.2f" % (tip_amount))
print("Total amount: %.2f" % (total_bill))
print("Amount per person: %.2f" % (total_bill / split_amount))