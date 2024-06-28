# Name: Mohan, Shawn, Kevin
# Date: March 19th
# Purpose: Alien Encountering System

alien_category = "Unknown"

def report_alien_encounter(alien_name, alien_age, alien_height):
    # Local variable
    alien_category = "Friendly" if alien_age <= 10 and alien_height <= 5.0 else "Unknown"

    print(f"ALERT: Alien {alien_name} encountered!")
    print(f"Age: {alien_age} years")
    print(f"Height: {alien_height} meters")
    print(f"Category: {alien_category}")

    if alien_category == "Friendly":
        print("Alien appears to be friendly. No immediate threat.")
    else:
        print("Alien intentions unclear. Proceed with caution.")

    if alien_category == "Unknown":
        if alien_name.startswith("Z") and alien_height > 10.0:
            print("Extreme caution advised. Unknown alien species detected.")
        else:
            print("Further investigation needed to determine the nature of the alien.")

def calculate_distance(travel_speed, travel_time):
    distance = travel_speed * travel_time
    return distance

# Main program
print("ALIEN ENCOUNTER REPORTING SYSTEM")
print("-------------------------------")

alien_name = input("Enter the alien's name: ")
alien_age = int(input("Enter the alien's age (in years): "))
alien_height = float(input("Enter the alien's height (in meters): "))

report_alien_encounter(alien_name, alien_age, alien_height)

travel_speed = float(input("Enter the spaceship's travel speed (in km/h): "))
travel_time = float(input("Enter the travel time (in hours): "))

distance = calculate_distance(travel_speed, travel_time)

print(f"\nThe spaceship has traveled a distance of {distance} kilometers.")

in_danger = False

if alien_category == "Friendly":
    print("The alien is not a threat to your spaceship.")

else:
    if distance > 100:
        print("Oh No! You are in the alien's territory! Run as quickly as possible.")
        in_danger = True
    elif distance > 50:
        print("You are close to the alien's territory, please turn back while you can.")
        in_danger = True
    else:
        print("You are safe from the alien!")


if in_danger:
    fight = input("Do you want to fight the alien?(Yes or No)").lower()

    if fight == "no":
        if distance > 100:
            print("The alien has caught up to you! You have died!")
        else:
            print("You have succesfully escaped!")
    else:
        if alien_age > 10 and alien_height > 5.0:
            print("The alien is too strong! You died to his ultimate powers!")
        else:
            print("Wow! You have beaten the alien beast. For your valiant efforts, this reporting system offers you 1000 gold")
