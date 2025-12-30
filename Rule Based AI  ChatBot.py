#Rule Based AI pythone chatBot

import datetime
import time
name = input("swagat h, enter your name :")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good morning,", name)
elif 11 <= presentHour <= 17:
    print("Good afternoon", name)
elif 17 <= presentHour <= 20:
    print("Good evening", name)
    





print("Nmaste! Welcome to Your chatBot:.")
print("you can ask me basic question: , Type 'bye ' to exit from the bot.")

# chatBot Memory Creation of responses!

responses = {
    "hellow": "Ho , Welocome. How can I help you",
    "how are you": "I am very fine. Thank you",
    "who are you": "I am smart AI chatbot",
    "motivate me": "Keep going. Every bug of your project makes you a better",
    "happy": "Great to hear that",
}


#Function to get responses of ChatBot

def getResponseOfBot(userQuestion):
    userquestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am not able to tell that yet. Mai jald hi ye sikh lunga"



# Tak user input

while True:
    userInput= input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Responses:", reply)

    if 'bye' in userInput.lower():
     break
