#importing libraries
import wikipedia
from chatterbot import ChatBot

#create chatbot
chatbot = ChatBot ('OMEN')

#Add packages to train the chatbot
from chatterbot.trainers import ListTrainer

#Created a personality to talk to.
personality_smalltalk = [
    "Hello, how are you?",
    "I am good!",
    "How has your day been?",
    "It has been going good, I hope yours has as well!",
    "What are you doing today?",
    "Waiting to talk to you!"
]

personality_hobbies = [
    "What do you like to do?",
    "I enjoy playing video games and watching tv shows.",
    "What games do you like to play?",
    "I like playing Valorant, and Apex Legends.",
    "What tv shows do you watch?",
    "Currently I am watching Dexter and Sons of Anarchy!"
]

personality_information = [
    "What is your purpose?",
    "I am here to talk with you, and to research topics for you!",
    "What can you research?",
    "Any topic you would like to!",
    "How can I research it?",
    "Just type in research and I will ask you what your topic is."
]

#Setup to train personality
trainer_personality_smalltalk = ListTrainer(chatbot)
trainer_personality_information = ListTrainer(chatbot)
trainer_personality_hobbies = ListTrainer(chatbot)

#training personality
trainer_personality_smalltalk.train(personality_smalltalk)
trainer_personality_information.train(personality_information)
trainer_personality_hobbies.train(personality_hobbies)

#Created a function to have the user enter a topic to research using the Wiki library.
def research():
    #Getting user input to research
    user_input2 = input ("What is your first topic?")
    wiki_page = wikipedia.page(user_input2)

    print("\n\n" + wiki_page.title + "\n\n")
    print("\n\n" + wiki_page.summary + "\n\n")

    wiki_summary = wiki_page.summary

     #Creating a file
    data_to_summarize = open('wiki.txt', 'w')
    #Writing in the summary information to the file
    data_to_summarize.write(wiki_summary)
    #closing the file
    data_to_summarize.close()




#lets say hello to the user for the first time
print("\n\n\nHello, I am OMEN, how can I help you?")

#Now I am going to ask the user for input and then print the response
# using a loope to keep asking the user input until the user types "quit"
#If the user enters research then it will run the function to get a user topic.
is_exit = False
while not is_exit:
    user_input = input("\nWhat is your question?")
    if user_input == "quit":
        is_exit = True
    elif user_input == "research":
        research()
        is_exit = False
    else:
        response_chatbot = chatbot.get_response(user_input)
        print("\nALIS: " + str(response_chatbot))
        