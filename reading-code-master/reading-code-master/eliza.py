import random
import sys

responses = [
  ("hello",                                                       
     ["Hello!  Glad you could be here today.",                   
      "Hi there.  How are you today?",                          
      "Hello, how are you feeling today?"                      
      ]),
  ("mother",
     ["Tell me more about your mother",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?"
      ]),
  ("father",
     ["Tell me more about your father",
      "What was your relationship with your father like?",
      "How do you feel about your father?"
      ]),
  ("i feel",
     ["Good, tell me more about those feelings",
      "Do you often feel that?",
      "When you feel that way, what do you do?"
      ]),      
  ("i am",
     ["How long have you been that way?",
      "How do you feel about that?",
      "Why do you think you are like that?"
      ]),      
  ("",
     ["Please tell me more",
      "Can you elaborate on that?",
      "I see",
      "How does that make you feel?",
      "How do you feel when you say that?"
      ]),
  ]

##################################################################################
#### This is the code that asks the user for input, and then prints out a response


# Begin by asking the user a question
print("Welcome to Eliza!")
print("How are you feeling today?")

while True:                                    
  resp = input("> ").lower()              
  if "goodbye" in resp:                       
    print("Goodbye!")                        
    sys.exit(0)                             
                                           
  for response in responses:              
    if response[0] in resp:              
      print(random.choice(response[1])) 
      break                            



