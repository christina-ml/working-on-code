# Adventure Game - 10-14-20

import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def playing_birdspan():
    dice = ["fish", "fish", "fish", "fish", "fish",
            "mouse", "mouse", "mouse", "mouse", "mouse",
            "worm", "worm", "worm", "worm", "worm",
            "seed", "seed", "seed", "seed", "seed",
            "berry", "berry", "berry", "berry", "berry",
            "apple", "apple", "apple", "apple", "apple"]
    dice_roll = [
        random.choice(dice), random.choice(dice),
        random.choice(dice), random.choice(dice),
        random.choice(dice)
    ]
    target = dice_roll[-2], dice_roll[0]
    print_pause(f"You're looking for a {target} to play your next move.")
    print_pause("You roll 5 dice into the dice tower to gain food.\n")
    print_pause("You just rolled:")
    print_pause(f"{dice_roll} ")
    print_pause(f"You wanted to roll a {target} and you got it!")


def pre_intro_game():
    print_pause("You're sitting at home playing your Birdspan "
                "board game.\nYou're also eating toast with butter.\n")
    print_pause("Yummy!!!! I love toast with butter!\n")
    print_pause("It's your turn. Roll the dice.\n")
    agree = input("Do you want to roll the dice? It's your turn.\n"
                  "(Type something below)\n").upper()
    print_pause(f"'{agree}!!!' you accidentallly yell louder than "
                "expected.\nYour voice echos through the dining "
                "room, making you dizzy!\nIn any case, you were "
                "so enthusiastic that it sounds like you agreed.\n")
    print_pause("You decide to roll. I can win this!\n")
    playing_birdspan()
    name = input("Wait, who am I playing with? What's your name?\n"
                 "(type your name)\n")
    print_pause(f"Hello there, {name}! Of course! Sorry, I didn't "
                "recognize you there with your losing streak...")
    print_pause("Maybe one day you'll win a game.")
    bird = input("What's your favorite bird?\n"
                 "(type favorite bird)\n")
    print_pause(f"{bird}? Well that can't be right...{name}, "
                "you should go visit the zoo when you have "
                "some spare time.")
    print_pause("You say, 'Sure, thing!' and it's your turn "
                "again so you roll the dice "
                "into the dice tower a second time.")
    print_pause("Aha! I rolled!")
    print_pause("Unfortunately, it's not what you wanted.")
    print_pause("Agghh! I've had enough of this game.")
    air = input("Would you like to get some fresh air?\n"
                "(type your response)\n")
    print_pause(f"You said {air}, but didn't say it "
                "loud enough, to try and prevent accidentally "
                "yelling again. You get annoyed that nobody heard "
                "you and go outside anyway. You take a long walk.\n")


def intro(items, same_creature, treasure, treasure_item):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow butterflies.")
    print_pause("In the distance is a rainbow. You wonder if there "
                "is a pot of gold at the end of it.")
    print_pause("It just rained, so the ground is muddy.")
    print_pause("Your sneakers are sticking to the mud with each step.\n")
    print_pause("Rumor has it that a " + same_creature + " is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is an abandoned house.")
    print_pause("To your right is a creepy dark cave with screeching bats.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) butter knife.")
    print_pause("It still has butter on it.\n")
    items.append("butter knife")


def house_or_cave_question(items, same_creature, treasure, treasure_item):
    print_pause("Enter 1 to knock on the door of the abandoned house.")
    print_pause("Enter 2 to peer into the bat infested cave.")
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
    response = input("Not to be greedy, you can only take one item.\n"
                     "Would you like to take a piece of treasure, or "
                     "leave it in the cave?\n(take/leave)\n").lower()
    if response == "leave":
        print_pause("Good idea. The skeleton can guard his treasure.\n")
        treasure.append(treasure_item)  # without this, the game doesn't end.
        treasure.remove(treasure_item)  # without this, the game doesn't end.
    elif response == "take":
        print_pause("You decide to pick up the " + treasure_item +
                    " for good luck. Maybe this will come in handy "
                    "later.\n")
        treasure.append(treasure_item)
    else:
        print("Sorry, you need to make a decision. The skeleton is "
              "watching you.\n")
        treasure_question(items, same_creature, treasure, treasure_item)
    field(items, same_creature, treasure, treasure_item)


def field(items, same_creature, treasure, treasure_item):
    print_pause("You walk back out to the field.")
    house_or_cave_question(items, same_creature, treasure, treasure_item)


def field_run(items, same_creature, treasure, treasure_item):
    print_pause("You run back into the field. Luckily, you "
                "don't seem to have been followed.")
    house_or_cave_question(items, same_creature, treasure, treasure_item)


def house(items, same_creature, treasure, treasure_item):
    print_pause("You approach the door of the abandoned house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a " + same_creature + ".")
    print_pause("Eep! This is the " + same_creature + "'s house!")
    print_pause("The " + same_creature + " attacks you!")
    if "butter knife" in items:
        enter_house_with_knife(items, same_creature, treasure, treasure_item)
    if "rifle" in items:
        enter_house_with_rifle(items, same_creature, treasure, treasure_item)


def enter_house_with_knife(items, same_creature, treasure, treasure_item):
    print_pause("You feel a bit under-prepared for this, what "
                "with only having a tiny butter knife.")
    response = input("Would you like to (1) fight or (2) run away?\n")
    if response == "1":
        print_pause("You do your best...")
        print_pause("but your butter knife is no match for "
                    "the " + same_creature + ".")
        print_pause("You have been defeated!")
        items.remove("butter knife")
        play_again(items, same_creature, treasure, treasure_item)
    elif response == "2":
        print_pause("You run back into the field. Luckily, you "
                    "don't seem to have been followed.")
        house_or_cave_question(items, same_creature, treasure,
                               treasure_item)
    elif response != "1" or "2":
        print("I don't know what that is. Please enter 1 or 2.")
        house(items, same_creature, treasure, treasure_item)


def enter_house_with_rifle(items, same_creature, treasure, treasure_item):
    response = input("Would you like to (1) fight with assault rifle "
                     "or (2) run away?\n")
    if response == "1":
        print_pause("As the " + same_creature + " moves to attack, "
                    "you quickly grab your new assault rifle.")
        for treasure_item in treasure:
            print_pause("The " + same_creature + " is distracted by "
                        "your " + treasure_item + " and stumbles.")
        print_pause("The golden assault rifle shines brightly in your "
                    "hand as you brace yourself for the attack.")
        print_pause("But the " + same_creature + " takes one look at "
                    "your shiny "
                    "new toy and runs away!")
        print_pause("You have rid the town of the " + same_creature +
                    ". You are victorious!")
        print_pause("I repeat, You are victorious!")
        items.remove("rifle")
        play_again(items, same_creature, treasure, treasure_item)
    elif response == "2":
        print_pause("You run back into the field. Luckily, you "
                    "don't seem to have been followed.")
        if treasure_item in treasure:
            print_pause("At least you still have "
                        "your " + treasure_item + " with you. "
                        "What good luck!")
        house_or_cave_question(items, same_creature, treasure,
                               treasure_item)
    elif response != "1" or "2":
        print("I don't know what that is. Please enter 1 or 2.")
        house(items, same_creature, treasure, treasure_item)


def cave(items, same_creature, treasure, treasure_item):
    print_pause("You peer cautiously into the cave.")
    if "rifle" in items:
        print_pause("You've been here before, and gotten all the good "
                    "stuff.\nIt's just an empty cave now.")
        print_pause("The treasure chest is now completely bare, since "
                    "a quick family of goblins managed to haul it all "
                    "away after you left the chest open.\n")
        field(items, same_creature, treasure, treasure_item)
    elif "butter knife" in items:
        print_pause("It turns out to be only a very small cave.\n")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found a shiny gold assault rifle!")
        print_pause("What is this doing in here?")
        print_pause("You discard your silly old butter knife and take "
                    "the assault rifle with you.\n")
        print_pause("*screech* Eek! A bat! It was hit by your butter knife.\n")
        print_pause("You check the gun. It's loaded, alright!")
        items.remove("butter knife")
        items.append("rifle")
        print_pause("You wander around the cave a little bit more and "
                    "stumble upon a treasure chest.\nIt's locked, but "
                    "you then find the key around a skeleton's neck and "
                    "yank it right off.\n")
        print_pause("The key turns smoothly, and it's unlocked!\n")
        print_pause("The treasure chest is filled with...rocks?\n"
                    "You notice some shiny things underneath the rocks.\n")
        print_pause("An inscription in gold lettering inside the chest "
                    "reveals that this once belonged to a very old King, "
                    "and this contains:\na bejeweled crown inlaid with "
                    "the finest jewels, a gold goblet, and a dusty old "
                    "treasure map.\n")
        treasure_question(items, same_creature, treasure, treasure_item)


def play_again(items, same_creature, treasure, treasure_item):
    response = input("Would you like to play again? (y/n)\n").lower()
    if response == "y":
        print_pause("Excellent! Restarting the game ...")
        play_game()  # Go back to the intro to restart the game. No items.
    elif response == "n":
        exit_game()
    else:
        play_again(items, same_creature, treasure, treasure_item)


def exit_game():
    print_pause("Thanks for playing! See you next time.")
    # GAME ENDS


def play_game():
    items = []
    treasure = []
    same_creature = random.choice(["wyvern", "centaur", "wraith",
                                  "flying monkey", "cyber dragon",
                                   "cyclops", "giant python", "hungry orc",
                                   "groggy humanoid", "dark magician"])
    treasure_item = random.choice(["bejeweled crown", "golden goblet",
                                  "dusty old treasure map"])
    pre_intro_game()
    intro(items, same_creature, treasure, treasure_item)
    house_or_cave_question(items, same_creature, treasure, treasure_item)


play_game()
