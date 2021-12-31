def guard(treasure_chest_items):

    crappy_sword = True
    for treasure in treasure_chest_items:
        if treasure == "crappy sword":
            crappy_sword = False

    actions_dict = {"check": "You see the guard is still sleeping, you need to get to that door behind him. What are you waiting for?",
                    "sneak": "You attempt to slip past the guard. In doing so, you wake him up!",
                    "attack": "With your sword you harness all your energy and attack the guard!"
                   }

    while(1):

        user_move = input("What do you do? attack | sneak | check: > ").lower()
        if user_move in actions_dict.keys():
            print(actions_dict[user_move])
            if user_move == "attack":
                if crappy_sword == False:
                    print("Your shiny sword slices the guard's armour and stabs the heart. You go through the door and are now outside! Freedom! \n{VICTORY}")
                    return
                else: you_die("Since your sword is too crappy, it instantly breaks, and the guard wakes up and jabs his sword in your chest")

            elif user_move == "sneak":
                you_die("In the blink of an eye, the guard wakes up and hiss dagger goes right through your chest.")



def you_die(reason):
    print(f"{reason} \n<GAME OVER>")
    exit(0)

def red_door():
    print("You enter a room and encounter an angry red dragon!")
    next_move = input("Do you choose to flee or stay? > ")

    if next_move == 'flee':
        start_adventure()
    else:
        you_die("The dragon spits firey red flames and burns you alive before eating your dusty remains.")

def blue_door():
    treasure_chest = ["diamonds", "gold", "silver", "sword"]
    print("You enter a room with a sleeping guard infront of a door to the right and to the left a shiny treasure chest")
    action = input("What do you do? > ")

    if action.lower() in ['treasure', 'left', 'chest']:
        print("You slowly walk towards the shiny treasure chest")
        open_chest = input("Do you open the treasure chest? yes/no > ")

        if open_chest == 'yes':
            print("The chest creaks open, you find the following: ")

            for treasure in treasure_chest:
                print(treasure)

            treasure_size = len(treasure_chest)
            collect_item = input(f"Would you like to collect all {treasure_size} items? yes/no > ")

            if collect_item == 'yes':
                treasure_chest.remove('sword')
                print("You collect a shiny new sword! This will be a fine replacement for the old crappy sword")

                temp_chest = treasure_chest[:]
                treasure_contents = ', '.join(treasure_chest)
                print(f"You also collected {treasure_contents}")

                for treasure in temp_chest:
                    treasure_chest.remove(treasure)

                treasure_chest.append('crappy sword')
                print("You close the chest and now the only thing that stands infront of the door to freedom is the guard. Time to face him")
                guard(treasure_chest)
            else:
                print("You ignore the items in the chest and go towards the guard who is sleeping infront of the door to freedom")
                guard(treasure_chest)
        else:
            print("You ignore the treasure chest and go towards the guard who is sleeping infront of the door to freedom")
            guard(treasure_chest)
    else:
        print("You go to the right, straight to the guard!")
        guard(treasure_chest)

def start_adventure():
    print("You have encountered two doors: red and blue")
    door_color = input("Which door do you choose to pass through? > ")

    if door_color == 'red':
        red_door()
    elif door_color == 'blue':
        blue_door()
    else:
        print(f"You were asked to choose red or blue and you chose {door_color} Goodbye!")

player_name = input("Enter name to begin: > ")
print(f"Greetings, {player_name}")
start_adventure()
