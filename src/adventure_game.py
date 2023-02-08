import time
import random

def print_pause(words):
    print(words)
    time.sleep(2)

def valid_input(prompt, option1, option2):
    response = input(prompt).lower()
    while True:
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            response = input(prompt)

def start():
    item=[]
    role = random.choice(["wicked fairie", "pirate", "dragon", "troll",
                        "gorgon"])
    intro(role, item)

def intro(role, item):
    plots=["You find yourself standing in an open field, filled with grass"
            "and yellow wildflowers.",
            "Rumor has it that a "+role+" is somewhere around here,"
            "and has been terrifying the nearby village.",
            "In front of you is a house.",
            "To your right is a dark cave.",
            "In your hand you hold your trusty (but not very effective) dagger."]
    for plot in plots:
        print_pause(plot)
    
    field(role, item)

def field(role, item):
    # Things that happen in the field
    print_pause("Enter 1 to knock on the door of the house.") 
    print_pause("Enter 2 to peer into the cave. ")
    print_pause( "What would you like to do? " )
    print(item)
    response = valid_input("(Please enter 1 or 2). \n", "1", "2")
    if response == "1":
        house(role, item)
    else:
        cave(role, item)

def house(role, item):
    # Things that happen to the player in the house
    plots=["You approach the door of the house.",

        "You are about to knock when the door opens and out steps a "+role+".",

        "Eep! This is the "+role+"'s house!",

        "The "+role+" attacks you!"]

    for plot in plots:
        print_pause(plot)
    if "sward" not in item:
         print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.\n")
    
    response = valid_input("Would you like to (1) fight or (2) run away?", "1", "2")
    
    if response == "1":
        fight(role, item)
        play_again()

    if response == "2":
        print_pause("\nYou run back into the field. "
                    "\nLuckily, you don't seem to have been followed.\n")
        field(role, item)

def cave(role, item):
    # Things that happen to the player goes in the cave  
    if "sward" in item:
        plots = ["\nYou peer cautiously into the cave.",

                "\nYou've been here before, and gotten all"
                " the good stuff. It's just an empty cave now.",
                    
                "\nYou walk back to the field.\n"]
        for plot in plots:
            print_pause(plot)
    else:
        plots = ["\nYou peer cautiously into the cave.",
                 "\nIt turns out to be only a very small cave.",
                 "\nYour eye catches a glint of metal behind a rock.",
                 "\nYou have found the magical Sword of Ogoroth!",
                 "\nYou discard your silly old dagger and take "
                    "the sword with you.",
                 "\nYou walk back out to the field.\n"]
        for plot in plots:
            print_pause(plot)
        print(item)
        item.append("sward")
        print(item)

    field(role, item)

def fight(role, item):
    # Things that happen when the player fights  
    if "sward" in item:
        plots=["As the " + role + " moves to attack, "
               "you unsheath your new sword.",

                "The Sword of Ogoroth shines brightly in "
                "your hand as you brace yourself for the attack.",

                "But the " + role + "takes one look at "
                "your shiny new toy and runs away!",

                "You have rid the town of the " + role +
                ". You are victorious!\n"]
        for plot in plots:
            print_pause(plot)
    else:
        plots=["You do your best...",

              "but your dagger is no match for the "+ role + ".",

               "You have been defeated!"]
        for plot in plots:
            print_pause(plot)

def play_again():
    response = valid_input("Would you like to play again? (y/n)\n", "y", "n")
    if response == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...\n\n\n")
        start()
    elif response == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")

start()

