#Prompts user to fill in blanks for the statement and stores input in variables
user_name = input("Please fill in the blanks below: \n___(name)___'s favorite subject in school is ___(subject)___. \nWhat is name? ")
user_subject = input("What is subject? ")

#Prints completed statement with user's input
print("%s's favorite subject in school is %s." % (user_name, user_subject))