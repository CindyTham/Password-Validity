import sys


has_upper_case_character = 0
has_lower_case_character = 0
has_number = 0


#Is password between 6 and 12 characters
while True:
    password = input ("Hello User, A strong password will contain uppercase, lowercase and numericals. Please enter your password: ")
    password_length = len(password)

    if password_length < 6 or password_length > 12:
        print ("Error, Password must be longer than 5 but no more than 13 charactors.")
    else:
        print ("Password length matches criteria")
        break

#About characters
for character in password:
    if character == character.upper() and not character.isdigit():
        has_upper_case_character = 1   
    if character == character.lower() and not character.isdigit():
        has_lower_case_character = 1   
    if character.isdigit():
        has_number = 1

        
total = has_upper_case_character + has_lower_case_character + has_number 


if total == 3:
    print ("Password Strength = STRONG")
if total == 2:
    print ("Password Strength = MEDIUM")
if total == 1:
    print ("Password Strength = WEAK")
