# Calculate Maximum Roth IRA Contributions for 2024

# Welcome User

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

# Calculate Maximum Contributions

if married == "no":
    max_agi = 146000
    if (agi - max_agi > 15000):
        print("You qualify for the Maximum Contrbution: ", max_contr)
    else:
        reduc_contr = round(((agi - max_agi)/15000), 3)
        if reduc_contr >= 1:
            reduc_contr = 1
        reduc_contr = max_contr-(reduc_contr * max_contr)
        print("Your Maximum Contribtion with Reductions is: ", int(reduc_contr))
else:
    if jointly == "yes":
        max_agi = 230000
        if (agi - max_agi > 10000):
            print("You qualify for the Maximum Contrbution: ", int(reduc_contr))
        else:
            reduc_contr = round(((agi - max_agi)/10000), 3)
            if reduc_contr >= 1:
                reduc_contr = 1
            reduc_contr = max_contr-(reduc_contr * max_contr)
            print("Your Maximum Individual Contribution with Reductions is: ", int(reduc_contr))
    else:
        print("In 2024 Married Individuals Filing Sperately cannot contribute to a Roth IRA.")    

        


    












    