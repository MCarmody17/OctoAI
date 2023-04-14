import pyjokes
from todo import Todo, Item
from ai import AI
from weather import Weather
from randfacts import randfacts
from datetime import datetime


octo = AI()
todo = Todo()


def facts():
    fact = randfacts.get_fact()
    print(fact)
    octo.say(fact)

def joke():
    funny = pyjokes.get_joke()
    print(funny)
    octo.say(funny)

def add_todo()->bool:
    item = Item()
    octo.say("Tell me whjat to add to the list")
    try:
        item.title = octo.listen()
        todo.new_item(item)
        message = "Added " + item.title
        octo.say(message)
        return True
    except:
        print("Ooops there was an error")
        return False

def list_todos():
    if len(todo) > 0:
        octo.say("Here are your to do's")
        for item in todo:
            octo.say(item.title)
    else:
        octo.say("The list is empty")

def remove_todo():
    octo.say("Tell me which item to remove")
    try:
        item_title = octo.listen()
        todo.remove_item(title = item_title)
        message = "Removed" + item_title
        octo.say(message)
        return True
    except:
        octo.say("Oops there was an error")
        return False
    


def weather():
    myweather = Weather()
    forecast = myweather.forecast
    octo.say(forecast)
    print(forecast)

command = ""
octo.say("Hello")


while True and command != "goodbye":
    try:
        command = octo.listen()
        print("command was: ",command)
    except:
        print("Oops there was an error")
        command = ""

    if command == "tell me a joke":
        joke()
        command = ""

    if command in ["add to-do", "add to do", "add item", "another to-do"]:
        add_todo()
        command = ""

    if command in ["What is the weather like",'give me the forecast','give me the weather', 'Whats the weather like',"What's the weather like"]:
        weather()
        command = ""
    
    if command in ["Tell me a fact","Tell me something","Fact"]:
        facts()
        command = ""
    
    if command in ["Good morning","Good evening","Morning", "Good afternoon"]:
        now = datetime.now()
        hour = now.hour
        if (0 <= hour <= 12):
            message = "Morning"
        if (12 <= hour <= 17):
            message = "Afternoon"
        if (17 <= hour <=21):
            message = "Evening"
        if hour > 21:
            message = "Night"
        message = "Good" + message + "Matthew"
        octo.say(message)
        weather()
        #list_todos()
        joke()
        facts()
        command = ""

    
    
octo.say("Goodbye, I'm going to sleep now")