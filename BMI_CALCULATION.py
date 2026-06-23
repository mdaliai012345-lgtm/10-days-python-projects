# This is program to calculate BMI (Body Mass Index)

Weight = float(input(" Enter Your Weight : "))            # enter body weight
Unit   = input(" is this in kg or lb: ").lower()                
Height = float(input(" Enter Your Height in M : "))       # enter body height
unit   = input(" is it in m or inch : ").lower()   

if Unit == "lb":                  # convert lb into kg
    Weight = (Weight / 2.20462)
if unit == "inch":                # convert inch into meter
    Height = (Height * 0.0254)

    print(Weight)
    print(Height)

def BMI(Weight,Height):                                    # function for calculating BMI 
    calculation = (Weight / (Height ** 2))
    return  f"{calculation:.2f}"

print(BMI(Weight,Height))   # calling the fuction