import time
def start():
    print("Welcome to the adventure game!")
    print("You find yourself in space. Your goal is to find a way to go back home, While here, you will explore different planets, meet creatures, interact with them, aliens and much more")

def do_choice():
    print("\nMake a choice: ")
    print("1. Land on Orionis")
    print("2. Continue journey")
    return input("Enter what you chose(1, 2): ")

def orionis_scenario():
    print("You chose Orionis planet")
    print("In order to enter Orionis planet, solve this problem: 45*45")
    return input("Your answer is: ")
def continue_journey():
    print("You want to continue journey?")
    print("If so, solve this problem--> 45*45 ")
    return input("Type your answer here--> ")

def chapter_2():
    print("Welcome to another adventure")
    print("Lets discove more things and gain valuable insights")
    print("You are in aliens place")
    print("Would you like to discover aliens culture? or would you like to continue your journey?")
    return ("Give your answer here--> ")

