# Calculate Maximum Roth IRA Contributions for 2024

# Welcome User

#Guard Rails need to be added in future update

print("Welcome to the Roth IRA contributions calculator!")

# Ask for Marital Status
married = input("Are you married? yes/no: ")

# Determine if filed jointly if married
if married == "yes":
    jointly = input("Do you file jointly? yes/no: ")
    if jointly == "yes":
        # Ask for Gross Income
        gi = int(input("Please input your combined gross income: "))
else:
    gi = int(input("Please input your gross income: "))

# Determine Age
age = int(input("What is your age?: "))
if age >= 50:
    max_contr = 8000
else:
    max_contr = 7000
# Determine if deductions from GI are applicable
adjustments = int(input("Please enter any deductions such as Pre-Tax 401k contributions: "))
# adjust gi
agi = (gi - adjustments)

# Calculate Maximum Contributions with Reductions and Print Results

if married == "no":
    max_agi = 146000
    if (agi - max_agi < 0):
        print("You qualify for the Maximum Contrbution: ", max_contr)
    elif (agi - max_agi < 15000):
        reduc_contr = round(((agi - max_agi)/15000), 4)
        if reduc_contr >= 1:
            reduc_contr = 1
        reduc_contr = round(max_contr-(reduc_contr * max_contr), -1)
        if (reduc_contr > 200):
            print("Your Maximum Contribution with Reductions is: ", int(reduc_contr))
        else:
            print("Your Maximum Contribution with Reductions is: 200")
    else:
        print("Your Maximum Contribution with Reductions is: 0")
else:
    if jointly == "yes":
        max_agi = 230000
        if (agi - max_agi < 0):
            print("You qualify for the Maximum Contrbution: ", int(max_contr))
        elif (agi - max_agi < 10000):
            reduc_contr = round(((agi - max_agi)/10000), 4)
            if reduc_contr >= 1:
                reduc_contr = 1
            reduc_contr = round(max_contr-(reduc_contr * max_contr), -1)
            if (reduc_contr > 200):
                print("Your Maximum Contribution with Reductions is: ", int(reduc_contr))
            else:
                print("Your Maximum Contribution with Reductions is: 200")
        else:
            print("Your Maximum Individual Contribution with Reductions is: 0")
    else:
        print("In 2024 Married Individuals Filing Sperately cannot contribute to a Roth IRA.")    

        


    












    
