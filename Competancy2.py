#Program name: Competancy2.py
#Programmer: Lillian Letiecq
#Email: lletiecq@student.cnm.edu
#Purpose: provides user capability to view info about a state


states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
'Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana',
'Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska',
'Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio',
'Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas',
'Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']

capitals = ['Montgomery','Juneau','Phoenix','Little Rock','Sacramento','Denver','Hartford','Dover',
'Tallahassee','Atlanta','Honolulu','Boise','Springfield','Indianapolis','Des Moines','Topeka',
'Frankfort','Baton Rouge','Augusta','Annapolis','Boston','Lansing','Saint Paul','Jackson',
'Jefferson City','Helena','Lincoln','Carson City','Concord ','Trenton','Santa Fe','Albany','Raleigh',
'Bismarck','Columbus','Oklahoma City','Salem','Harrisburg','Providence','Columbia','Pierre','Nashville',
'Austin','Salt Lake City','Montpelier','Richmond','Olympia','Charleston','Madison','Cheyenne']

districts = [7,1,9,4,52,8,5,1,28,14,2,2,17,9,4,4,6,6,2,8,9,13,8,4,8,
2,3,4,2,12,3,26,14,1,15,5,6,17,2,7,1,9,38,4,1,11,10,2,8,1]

order = [22,49,48,25,31,38,5,1,27,4,50,43,21,19,29,34,15,18,23,7,6,
26,32,20,24,41,37,36,9,3,47,11,39,12,17,46,33,2,13,40,8,16,28,45,14,10,42,35,30,44]

print("Welcome to the State information database!")                             #hi
state_name = input("Enter the name of a state to begin: ")                      #initial input

if state_name in states:                                                        #input is within states list
    state_index = states.index(state_name)                                      
else:                                                                           #bool for invalid state name
    print("State name not found.")
    nofind =(input("Would you like to look up another state? (Yes/No)"))
    if nofind=="Yes":
        state_name = input("Enter the name of a state to begin: ")
        state_index = states.index
    if nofind=="No":
        print("Try again later. Goodbye!")
        exit()

for state in states:                                                             #loop through states and info 
    print(f"The capital of {state_name} is {capitals[state_index]}, the U.S. Congressional district is {districts[state_index]}, and the order of addition to the Union is {order[state_index]}.")
    again =(input("Would you like to look up another state? (Yes/No)"))
    if again=="Yes":
        state_name = input("Enter the name of a state to begin: ")
        state_index = states.index(state_name)

    if again=="No":
        print("Goodbye!")
        exit()
