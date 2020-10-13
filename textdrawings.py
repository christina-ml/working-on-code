import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(0.5)


def print_fast(message_to_print):
    print(message_to_print)
    time.sleep(0.2)


def house_cave():
    print_fast("          ____")
    print_fast("         / .. |       __")
    print_fast("        / .... |     ( ,)")
    print_fast("       /________|   (', ')            _____________")
    print_fast("      |   ◊◊◊◊   |   ( ,)            // + ; + ;  + |")
    print_fast("      |   ____   |    ||            //+ ; |^^^^| ; +|")
    print_fast("      |   |  |   |    ||           (| ; |       | ; |)")
    print_fast("      |   |  |   |    ||          // + |         | + |)")
    print_fast("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^")


def standing():
    print("                O")
    print("               /|)")
    print("                |")
    print("               / |")
    print(".^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.")


house_cave()
standing()

print_pause("In front of you is a house.")
print_pause("To your right is a dark cave.")


# print_pause("Welcome home!  This is your house.")
# def house():
#     print("          ____")
#     print("         / .. |       __")
#     print("        / .... |     ( ,)")
#     print("       /________|   (', ')")
#     print("      |   ◊◊◊◊   |   ( ,)")
#     print("      |   ____   |    ||")
#     print("      |   |  |   |    ||")
#     print("      |   |  |   |    ||")
#     print("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.")
#     print_pause("Come outside, We're going on an adventure!")


# def cave():
#     print_pause("Welcome to the cave.")
#     print("        _____________")
#     print("       // + ; + ;  + |")
#     print("      //+ ; |^^^^| ; +|")
#     print("     (| ; |       | ; |)")
#     print("    // + |         | + |)")
#     print("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.")


def treasure_chest():
    print(" _____________")
    print("|__|_+++++_|__|")
    print("|   +  +  +   |")
    print("|_____________|")

treasure_chest()
