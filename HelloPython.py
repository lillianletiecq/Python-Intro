#Program Name: HelloPython
#Programmer: Lillian Letiecq
#Email: lletiecq@student.cnm.edu
#Purpose: Allows user to calculate the volume and surface area of a square pyramid
#enjoy!

print("Welcome to the Square Pyramid Calculator!")      #hi


base= float(input("Enter the base value: "))
height= float(input("Enter the height value: "))             
volume= base**2 * height / 3                            #volume formula
lsa = base * (base**2 +4 * height**2) **0.5             #lateral surface area formula


print("Base:", base, "Height:", height)                 #show inputs
bool=(input("Is this correct? (True/False): "))         #input confirmation
if bool=="False":                                       # if not confirmes
    print("Please re-enter the values.")                #re-enter values
    base= float(input("Enter the base value: "))
    height= float(input("Enter the height value: "))  
    print("Base:", base, "Height:", height)             #show inputs
    bool=(input("Is this correct? (True/False):"))      #re-confirm


if bool=="True":
    print("The volume of the square pyramid is:", {round(volume,3)})                #give volume
    print("The lateral surface area of the square pyramid is:", {round(lsa,3)})     #give surface area

print("Goodbye!")                                                                   #Voila!
