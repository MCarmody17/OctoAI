import pyjokes
from ai import AI

octo = AI()

def joke():
    funny = pyjokes.get_joke()
    print(funny)

    octo.say(funny)

command = ""

while True and command != "goodbye":
    command = octo.listen()
    print("command was: ",command)

    if command == "tell me a joke":
        joke()
    
octo.say("Goodbye, I'm going to sleep now")