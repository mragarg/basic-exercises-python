#Prompts user for Celsius temperature
user_celsius = float(input("Temperature in Celsius? "))

#Converts C into F
convert_f = user_celsius * 1.8 + 32

print("%.2f F" % (convert_f))