import time


# def print_pause(message_to_print):
#     print(message_to_print)
#     time.sleep(0.5)


def print_fast(message_to_print):
    print(message_to_print)
    time.sleep(0.2)


def house_cave():
    print_fast("          ____")
    print_fast("         / .. \\       __")
    print_fast("        / .... \\     ( ,)")
    print_fast("       /________\\   (', ')            _____________")
    print_fast("      |   ◊◊◊◊   |   ( ,)            // + ; + ;  + \\")
    print_fast("      |   ____   |    ||            //+ ;|^^^^^| ; +\\")
    print_fast("      |   |  |   |    ||           (| ; |       | ; |)")
    print_fast("      |   |  |   |    ||          // + |         | + |\\")
    print_fast("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.^")


def standing():
    print_pause("                O")
    print_pause("               /|)")
    print_pause("                |")
    print_pause("               / |")
    print_pause(".^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.")


# house_cave()
# standing()

# print_pause("In front of you is a house.")
# print_pause("To your right is a dark cave.")


# # print_pause("Welcome home!  This is your house.")
# # def house():
# #     print("          ____")
# #     print("         / .. |       __")
# #     print("        / .... |     ( ,)")
# #     print("       /________|   (', ')")
# #     print("      |   ◊◊◊◊   |   ( ,)")
# #     print("      |   ____   |    ||")
# #     print("      |   |  |   |    ||")
# #     print("      |   |  |   |    ||")
# #     print("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.")
# #     print_pause("Come outside, We're going on an adventure!")


# # def cave():
# #     print_pause("Welcome to the cave.")
# #     print("        _____________")
# #     print("       // + ; + ;  + |")
# #     print("      //+ ; |^^^^| ; +|")
# #     print("     (| ; |       | ; |)")
# #     print("    // + |         | + |)")
# #     print("^.^.^.^.^.^.^.^.^.^.^.^.^.^.^.")


# def treasure_chest():
#     print(" _____________")
#     print("|__|_+++++_|__|")
#     print("|__|_+++++_|__|")
#     print("|   +  +  +   |")
#     print("|_____________|")

# treasure_chest()


def weapon():
    print_fast("            __-^^-_______________________/\\_")
    print_fast(" |---\\_____| |-_-_-_-__---[]-^^-]--]__------]_________")
    print_fast("|    ======|_________-_-_^^-^-__]_]_]_______]---------'")
    print_fast("|----/   |_|_____________________|      \\__/")
    print_fast(" |__/         /====/")
    print_fast("             [][][]")
    print_fast("            /====/")
    print_fast("            [][][]")

weapon()


# #    ____________________|-^^^-]
# #  | |-_-_-_-__-----__[--^^-]--]
# #  |___________-_-_^^-^-^-__]_]_]
# #  |_|_________________________|
# #                       |====|
# #                       [][][]
# #                       |====|
# #                       [][][]




#     ____
#  //      \\
# || Pizza  |
# || Castle |
#  \\ ____ /



#     _______
#  //          \
# ||   ======   |
# ||   \o o /   |
# ||    \o /    |
# ||     \/     |
#  \\ ________ /



# def bat():
#     print_fast("                 /\      /\\")
#     print_fast("      ....      /A \^^^^/ A\      ....")
#     print_fast("     / .. \    |    o  o    |    / .. \\")
#     print_fast("    / .. . \   |     ^^     |   / . .. \\")
#     print_fast("   / . . .  \   \   |^^|   /   /  . . . \\")
#     print_fast("  /  . .  .  \   /--\^^/--\   /  .  . .  \\")
#     print_fast(" /  . .    .  \/           \ /  .    . .  \\")
#     print_fast("/  /\ .  /\ .  |   ^^^^^^   |  . /\  . /\  \\")
#     print_fast("| /  \. /  \ ./|    ^^^^    |\. /  \ ./  \ |")
#     print_fast("|/    \/    \/  \_   ^^   _/  \/    \/    \|")
#     print_fast("                  \______/")
#     print_fast("                   {}  {}")

# # bat()


def print_flash(message_to_print):
    print(message_to_print)
    time.sleep(0.05)


def bat():
    print_flash("                 /\\      /\\")
    print_flash("      ....      /A \\^^^^/ A\\      ....")
    print_flash("     / .. \\    |    o  o    |    / .. \\")
    print_flash("    / .. . \\   |     ^^     |   / . .. \\")
    print_flash("   / . . .  \\   \\   |^^|   /   /  . . . \\")
    print_flash("  /  . .  .  \\   /--\\^^/--\\   /  .  . .  \\")
    print_flash(" /  . .    .  \\/           \\ /  .    . .  \\")
    print_flash("/  /\\ .  /\\ .  |   ^^^^^^   |  . /\\  . /\\  \\")
    print_flash("| /  \\. /  \\ ./|    ^^^^    |\\. /  \\ ./  \\ |")
    print_flash("|/    \\/    \\/  \\_   ^^   _/  \\/    \\/    \\|")
    print_flash("                  \\______/")
    print_flash("                   {}  {}")

bat()
