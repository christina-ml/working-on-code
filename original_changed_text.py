# The code in this file functions great - checked pycodestyle, and
# just need to change the words, be creative!

import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.5)


def intro(items, same_creature, treasure, treasure_item):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + same_creature + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) dagger.")
    items.append("dagger")


# This begins the game, after the intro. Items with you - dagger:
def house_or_cave_question(items, same_creature, treasure, treasure_item):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    response = input("(Please enter 1 or 2.)\n")
    if response == "1":
        house(items, same_creature, treasure, treasure_item)
    elif response == "2":
        cave(items, same_creature, treasure, treasure_item)
    else:
        print("I don't know what that is. Please enter 1 or 2.")
        house_or_cave_question(items, same_creature, treasure, treasure_item)


def treasure_question(items, same_creature, treasure, treasure_item):
    response = input("Would you like to take a piece of treasure, or "
                     "leave it in the cave? (take/leave)\n")
    if response == "leave":
        print_pause("Good idea. The skeleton can guard his treasure.")
    elif response == "take":
        print_pause("You decide to pick up the " + treasure_item +
                    " for good luck. Maybe this will come in handy "
                    "later.")
        treasure.append(treasure_item)  # Appended treasure_item
    else:
        print("Sorry, you need to make a decision. The guard is "
              "watching you.")
        treasure_question(items, same_creature, treasure, treasure_item)
    field(items, same_creature, treasure, treasure_item)


def field(items, same_creature, treasure, treasure_item):
    print_pause("You walk back out to the field.")
    house_or_cave_question(items, same_creature, treasure, treasure_item)


def field_run(items, same_creature, treasure, treasure_item):
    print_pause("You run back into the field. Luckily, you "
                "don't seem to have been followed.")
    house_or_cave_question(items, same_creature, treasure, treasure_item)


# You have this item - dagger:
def house(items, same_creature, treasure, treasure_item):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a " + same_creature + ".")
    print_pause("Eep! This is the " + same_creature + "'s house!")
    print_pause("The " + same_creature + " attacks you!")
    if "dagger" in items:
        enter_house_with_dagger(items, same_creature, treasure, treasure_item)
    if "sword" in items:
        enter_house_with_sword(items, same_creature, treasure, treasure_item)


def enter_house_with_dagger(items, same_creature, treasure, treasure_item):
    print_pause("You feel a bit under-prepared for this, what "
                "with only having a tiny dagger.")
    response = input("Would you like to (1) fight or (2) run away?\n")
    if response == "1":
        print_pause("You do your best...")
        print_pause("but your dagger is no match for "
                    "the " + same_creature + ".")
        print_pause("You have been defeated!")
        items.remove("dagger")
        play_again(items, same_creature, treasure, treasure_item)
    elif response == "2":
        print_pause("You run back into the field. Luckily, you "
                    "don't seem to have been followed.")
        house_or_cave_question(items, same_creature, treasure,
                               treasure_item)
    elif response != "1" or "2":
        print("I don't know what that is. Please enter 1 or 2.")
        house(items, same_creature, treasure, treasure_item)


def enter_house_with_sword(items, same_creature, treasure, treasure_item):
    response = input("Would you like to (1) fight with sword or (2) run "
                     "away?\n")
    if response == "1":
        print_pause("As the " + same_creature + " moves to attack, "
                    "you unsheath your new sword.")
        for treasure_item in treasure:
            print_pause("The " + same_creature + " is distracted by "
                        "your " + treasure_item + " and stumbles.")
        print_pause("The Sword of Ogoroth shines brightly in your "
                    "hand as you brace yourself for the attack.")
        print_pause("But the " + same_creature + " takes one look at "
                    "your shiny "
                    "new toy and runs away!")
        print_pause("You have rid the town of the " + same_creature +
                    ". You are victorious!")
        print_pause("I repeat, You are victorious!")
        items.remove("sword")
        play_again(items, same_creature, treasure, treasure_item)
    elif response == "2":
        print_pause("You run back into the field. Luckily, you "
                    "don't seem to have been followed.")
        if treasure_item in treasure:
            print_pause("At least you still have your "
                        + treasure_item + " with you. What good luck!")
        house_or_cave_question(items, same_creature, treasure,
                               treasure_item)
    elif response != "1" or "2":
        print("I don't know what that is. Please enter 1 or 2.")
        house(items, same_creature, treasure, treasure_item)


def cave(items, same_creature, treasure, treasure_item):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
        print_pause("The treasure chest is now completely bare, since "
                    "a quick family of goblins managed to haul it all "
                    "away after you left the chest open.")
        field(items, same_creature, treasure, treasure_item)
    elif "dagger" in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        items.remove("dagger")
        items.append("sword")
        print_pause("You wander around the cave a little bit more and "
                    "stumble upon a treasure chest. It's locked, but you "
                    "then find the key around a skeleton's neck.")
        print_pause("The key turns smoothly and it's unlocked!")
        print_pause("The treasure chest is filled with...rocks? "
                    "You notice there are things underneath the rocks.")
        print_pause("An inscription in gold lettering inside the chest "
                    "reveals that this once belonged to a king, and this "
                    "contains: a crown inlaid with the finest jewels, "
                    "a goblet, and a dusty old treasure map.")
        treasure_question(items, same_creature, treasure, treasure_item)
        # field(items, same_creature, treasure, treasure_item)


def play_again(items, same_creature, treasure, treasure_item):
    response = input("Would you like to play again? (y/n)\n").lower()
    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()  # Go back to the intro to restart the game. No items.
    elif response == "n":
        exit_game()
        # print_pause("Thanks for playing! See you next time.")
    else:
        play_again(items, same_creature, treasure, treasure_item)


def exit_game():
    print_pause("Thanks for playing! See you next time.")
    # GAME ENDS - YOU EITHER WON OR LOST!


def play_game():
    items = []
    treasure = []
    same_creature = random.choice(["gorgon", "troll", "pirate",
                                  "wicked fairie", "dragon",
                                   "mouse", "eggplant", "tiger"])
    treasure_item = random.choice(["crown", "goblet",
                                  "dusty old treasure map"])
    intro(items, same_creature, treasure, treasure_item)
    house_or_cave_question(items, same_creature, treasure, treasure_item)


play_game()
