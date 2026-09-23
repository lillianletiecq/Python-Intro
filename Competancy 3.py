#Program:LetiecqP3
#Programmer: Lillian Letiecq
#Email: lletiecq@student.cnm.edu
#Purpose: provides user the capability to find a fruit in a string

import string

print("Welcome to the Fruit Finder Program!")

while True:

    result=[]
# set up the variables
    fruits = [ 'Apricot',	'Asian Pear',	'Avocado',	'Banana',	'Blackberries',
	'Blueberries',	'Boysenberries',	'Cactus Pear',	'Cantaloupe',	'Cherries',
    'Coconut',	'Cranberries',	'Figs',	'Gooseberries',	'Grapefruit',	'Grapes',
    'Honeydew Melon',	'Kiwifruit',	'Limes',	'Longan',	'Loquat', 'Lychee',	
    'Madarins',	'Malanga',	'Mandarin Oranges',	'Mangos',	'Mulberries',	
    'Nectarines',	'Oranges',	'Papayas',	'Passion Fruit',	'Peaches',	'Pears',
    'Persimmons',	'Pineapple',	'Plums',	'Pomegranate',	'Prunes',	'Quince',
    'Raisins',	'Raspberries',	'Rhubarb',	'Strawberries',	'Tangelo',	'Tangerines',
    'Tomato',	'Ugli Fruit',	'Watermelon'
]
    print(fruits)
    sentence = input("Please enter a sentence containing two fruits from the list above:")
    title_case = sentence.title()
    new_sentence = title_case.translate(str.maketrans('', '', string.punctuation))

    sentence_list = list(new_sentence.split(" "))
    print(list(sentence_list))

    fruit1 = set(sentence_list)
    fruit2 = set(fruits)
    result = list(fruit1 & fruit2)

    if len(result) > 0:
        substitution = sentence.split()
        substitution[sentence_list.index(result[-1])] = 'Brussels Sprouts'
        print(f"\n\nI found {len(result)} fruits in your sentence")
        print("Your fruits are", result)
        print("Your final sentence with some brussels spouts is:", ' '.join(substitution))
        user_input = input("\n\nPress enter to continue or type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("\n\nThank you for using my fruit finder!")
            break
    else:
        print(f"\n\nI found no fruits in your sentence")
        print("The fruits found is an empty list:", result)
        print("Your final sentence is:", sentence)


# Print the final affirmation
    print("\nThank you for using my fruit finder!")
