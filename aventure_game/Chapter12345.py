import time

import turtle

def welcome():
    turtle.bgcolor("black")
    turtle.pencolor("White")
    turtle.write("Welcome to Adventure Game!!!", align="center" , font=("Sans" , 30, "bold"))

    turtle.exitonclick()




def introduction():

    print("Welcome to the Adventure Game!")
    time.sleep(1)
    name = input("What's your name, space explorer?: ")
    print(f"Hello, {name}! Get ready for an exciting journey through the cosmos.\n")

def chapter_one():
    print("Chapter 1: The Cosmic Gateway")
    time.sleep(1)
    print("You find yourself in front of a cosmic gateway. It shimmers with energy.")
    choice = input("Do you want to enter? (yes/no): ").lower()
    if choice == "yes":
        print("Now in order to enter, please solve this question and type your answer")

        while True:
            choice2 = input("What is the largest planet in our solar system?: ").lower()

            if choice2 == "jupiter":
                print("Well done! You step through the gateway.")
                break
            else:
                print("Sorry, that's not correct. Try again.")

    else:
        print("You decide not to enter and continue your exploration.\n")




def chapter_two():
    print("\nChapter 2: Alien Encounter")
    time.sleep(1)
    print("On the alien planet, you encounter a friendly alien named Zork.")
    print("Zork offers to guide you through their fascinating world.")
    choice = input("Do you want to follow Zork? (yes/no): ").lower()

    if choice == "yes":
        print("You and Zork continuing the journey, discovering the wonders of the alien civilization.")

        print("As you walk, Zork starts a conversation:")
        print("Zork: Welcome, Earthling! I'm delighted to show you around. What brings you to our planet?")
        user_response = input("You: ")

        print(f"Zork: {user_response} That's fascinating! On our planet, we value {user_response} too.")
        time.sleep(2)

        zork_age_question = "Zork: By the way, can you guess my age? Solve this mathematical question and you gonna get my age : 3 + 5 + 2 + 100 + 100 + 90: "
        user_guess = input(zork_age_question)

        if user_guess.isdigit() and int(user_guess) == 300:
            time.sleep(1)
            print(
                "Zork: Congratulations! You guessed my age correctly.")



        else:
            time.sleep(1)
            print("Zork: Oops! That's not correct. Nevertheless, I appreciate your effort.")

        print("You and Zork continue your journey, sharing stories and learning from each other.")

    else:
        time.sleep(1)
        print("You decide to explore on your own and come across strange landscapes and peculiar creatures.\n")




def chapter_three():
    time.sleep(2)
    print("\nChapter 3: The Nebula Challenges")
    time.sleep(1)
    print("Welcome to my Nebulla challenges")
    time.sleep(1)
    print("Can you solve my contests? If ready, lezzz goooo !!!")
    choice = input("I'm a black abyss, a mystery profound,\n Gravity so strong, nothing can be found. \n Swallowing light, a cosmic enigma, \n What am I, in the vast celestial stigma?:").lower()
    if choice == "black hole":
        print("Congratulations!!! You solved it!!!")
        print("Here is another quest-->")
    else:
        print("Sorry, not correct, but I have another trial!!!")

    time.sleep(2)
    choice2 = input("I'm a giant ball of gas, shining bright, \n In the solar system, the center of light. \n Hydrogen fuses, creating energy so vast, \n What am I, a cosmic furnace to last?: ").lower()
    if choice2 == "sun":
        print("Ow waow!!! You again won!")
        print("Lets see what our next chapter has for us!")
        time.sleep(1)
    else:
        print("Sorry, not correct, But we gonna have lots of trials!!! Lez continue our journey")


def chapter_four():
    time.sleep(1)
    print("\nChapter 4: The Moon")
    time.sleep(1)
    print("You arrive at a moon.")
    print("A mysterious force surrounds you.")
    time.sleep(2)
    print("                                    #")
    print("                               ## ")
    print("                           #### ")
    print("                         ####")
    print("                        ####")
    print("                       #####")
    print("                     ##### ")
    print("                     #####")
    print("                    ##### ")
    print("                   ##### ")
    print("                  ##### ")
    print("                  #####")
    print("                  #####")
    print("                   #####")
    print("                     #####")
    print("                      #### ")
    print("                        #### ")
    print("                          ####")
    print("                              ####")
    print("                                  ####")
    print("                                        #")
    choice = input("What do you see in this picture?:  ").lower()
    time.sleep(1)
    if choice == "moon":
        print("Exactly!!! That's me!!!")
        time.sleep(1)
        print("Thanks for guessing me right! Lezz move on! ")
    else:
        print("Yeah, that was close, but thats me--> Moon:)")
        print("Lets move to our next and final adventure!!!")

def chapter_five():
    print("\nChapter 5: Homecoming")
    time.sleep(1)
    print("After very gripping adventure, it's time to return home.")

    time.sleep(1)
    choice = input("But before returning home, do you remember alien friend that you met? Can you provide his name? : ").lower()
    time.sleep(1)
    if choice == "Zork":
        print("Yaay!!! You are a good friend!!!")
        print("Your friend has message to you -> ")
        print(f"Zork: Hey, my dear friend!!! I am glad for joining this journey! \n I hope you enjoyed your time! And see you in next journeys:)")

    else:
        print("Zork: Oh dear friend, that was close! \n I hope you enjoyed your time! And see you in next journeys")

    time.sleep(1)

    print(f"CONGRATULATIONS! \nYou've completed the Interstellar Adventure.\n")

# Main game loop

welcome()
introduction()
chapter_one()
chapter_two()
chapter_three()
chapter_four()
chapter_five()


