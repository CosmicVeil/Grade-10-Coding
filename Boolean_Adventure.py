# Name: Mohan, Shawn, Kevin
# Date: March 18th
# Purpose: Create a quest using boolean variables

def main():

    found_key = False
    opened_door = False
    defeated_enemy = False
    
    search_chest = input("Do you want to open this chest on the floor? (yes or no)").lower()

    if search_chest == "yes":
        print("Congrats! You found the key!")
        found_key = True

    dangerous_door = input("Do you want to open this door, which could lead to potential danger? ").lower()

    if dangerous_door == "yes":
        print("You have found the enemy!")
        opened_door = True

    fight_enemy = input("Do you wish to fight the enemy or run(fight or run)? ")

    if fight_enemy == "fight":
        defeated_enemy = True

    if found_key and opened_door and defeated_enemy:
        print("Hooray! You have defeated the enemy! You have unlocked the treasure room, giving yourself money for the rest of your life!")
    else:
        print("You have failed the adventure! Better luck next time! ")
main()
