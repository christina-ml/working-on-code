import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(items, same_creature):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + same_creature + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) dagger.")
    items.append("dagger")


def play_again(items):
    response = input("Would you like to play again? (y/n)\n").lower()
    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()  # Go back to the intro to restart the game. No items.
    if response == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again(items)


def house_or_cave_question(items, same_creature):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    response = input("(Please enter 1 or 2.)\n")
    if response == "1":
        house(items, same_creature)
    elif response == "2":
        cave(items, same_creature)
    else:
        print("I don't know what that is. Please enter 1 or 2.")
        house_or_cave_question(items, same_creature)


def field(items, same_creature):
    print_pause("You walk back out to the field.")
    house_or_cave_question(items, same_creature)


def field_run(items, same_creature):
    print_pause("You run back into the field. Luckily, you "
                "don't seem to have been followed.")
    house_or_cave_question(items, same_creature)


def house(items, same_creature):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a " + same_creature + ".")
    print_pause("Eep! This is the " + same_creature + "'s house!")
    print_pause("The " + same_creature + " attacks you!")
    if "dagger" in items:
        print_pause("You feel a bit under-prepared for this, what "
                    "with only having a tiny dagger.")
        response = input("Would you like to (1) fight or (2) run away?\n")
        if response == "1":
            print_pause("You do your best...")
            print_pause("but your dagger is no match for "
                        "the " + same_creature + ".")
            print_pause("You have been defeated!")
            items.remove("dagger")
            play_again(items)
        elif response == "2":
            print_pause("You run back into the field. Luckily, you "
                        "don't seem to have been followed.")
            house_or_cave_question(items, same_creature)
        else:
            print("I don't know what that is. Please enter 1 or 2.")
            house(items, same_creature)
    elif "sword" in items:
        response = input("Would you like to (1) fight or (2) run away?\n")
        if response == "1":
            print_pause("As the " + same_creature + " moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.")
            print_pause("But the " + same_creature + " takes one look at "
                        "your shiny "
                        "new toy and runs away!")
            print_pause("You have rid the town of the " + same_creature +
                        ". You are victorious!")
            items.remove("sword")
            play_again(items)
        elif response == "2":
            print_pause("You run back into the field. Luckily, you "
                        "don't seem to have been followed.")
            house_or_cave_question(items, same_creature)
        else:
            print("I don't know what that is. Please enter 1 or 2.")
            house(items, same_creature)


def cave(items, same_creature):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.")
    elif "dagger" in items:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword "
                    "with you.")
        items.remove("dagger")
        items.append("sword")
    field(items, same_creature)


def play_game():
    items = []
    same_creature = random.choice(["gorgon", "troll", "pirate",
                                  "wicked fairie", "dragon",
                                   "mouse", "eggplant", "tiger"])
    intro(items, same_creature)
    house_or_cave_question(items, same_creature)


play_game()
