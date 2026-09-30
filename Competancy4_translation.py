#Program: Competancy4_translation.py
#Programmer: Lillian Letiecq
#Email: lletiecq@student.cnm.edu    
#Purpose: provides user the capability to translate common phrases from English to Danish

while True:
    def translate_phrase(phrase):
        translations = {
            "hello": "hej",
            "goodbye": "farvel",
            "thank you": "tak",
            "yes": "ja",
            "no": "nej",
            "excuse me": "undskyld mig",
            "I'm sad": "jeg er ked af det",
            "how are you?": "hvordan har du det?",
            "what is your name?": "hvad er dit navn?",
            "my name is...": "mit navn er...",
            "I don't understand": "jeg forstår ikke",
            "where is the bathroom?": "hvor er badeværelset?",
            "how much does it cost?": "hvor meget koster det?",
            "I would like...": "jeg vil gerne have...",
        }
        return translations.get(phrase.lower(), phrase)

    user_input = input("Enter a phrase to translate from English to Danish (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Exiting the translator. Goodbye!")
        break
    translated_phrase = translate_phrase(user_input)
    if translated_phrase == user_input:
        print("Sorry, that phrase is not in the translation dictionary.")
    else:
        print(f"The translation of '{user_input}' in Danish is: '{translated_phrase}'")
