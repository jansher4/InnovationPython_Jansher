import random
import os
import time
from os import system
os.system('cls||clear')
elevator_position = random.choice([i for i in range(1,10)])
while True:
    os.system('cls||clear')
    print("Elevator is on floor level: ", elevator_position)
    system("say 'Elevator is on floor level '" + str(elevator_position))
    time.sleep(1)
    print("What floor are you on?")
    system("say 'Input, What floor are you on? '")
    level = eval(input(""))
    os.system('cls||clear')
    print("Press button for up and down: 1 for up and 2 for down:")
    system("say 'Press button for up and down: 1 for up and 2 for down:'")
    input_request = eval(input(""))
    os.system('cls||clear')
    while True:
        if level == elevator_position:
            break
        elif level < elevator_position:
            os.system('cls||clear')
            print("Elevator coming down, current level: ", elevator_position)
            system("say 'Elevator coming down, current level: '" + str(elevator_position))
            elevator_position -= 1
            time.sleep(3)
        elif level > elevator_position:
            os.system('cls||clear')
            print("Elevator coming up, current level: ", elevator_position)
            system("say 'Elevator coming up, current level: '" + str(elevator_position))
            elevator_position += 1
            time.sleep(3)
        else:
            os.system('cls||clear')
            print("Wait, Elevator is almost at level ",elevator_position)
            system("say 'Wait, Elevator is almost at level '" + str(elevator_position))
            print("\nDoors Opening\n")
            time.sleep(4)
            break
    os.system('cls||clear')
    print("Welcome to Jan's Elevator")
    system("say 'Welcome to Jans Elevator'")
    time.sleep(1)
    print("Enter your desired floor number: ")
    system("say 'Enter your desired floor number: '")
    desired_floor = eval(input(""))
    time.sleep(1)
    print("\nDoors Closing\n")
    system("say 'Doors Closing'")
    time.sleep(3)
    os.system('cls||clear')
    time.sleep(1)
    while True:
        if desired_floor == elevator_position:
            print("\nDoors Opening\n")
            system("say 'Doors Opening'")
            time.sleep(3)
            break
        elif desired_floor > elevator_position:
            print("Elevator going up to floor: ", desired_floor)
            system("say 'Elevator going up to floor: '" + str(desired_floor))
            elevator_position +=1
            time.sleep(3)
            os.system('cls||clear')
            print("Current Floor: ", elevator_position)
            system("say 'Current Floor: '" + str(elevator_position))
        elif desired_floor < elevator_position:
            print("Elevator is going down to floor: ", desired_floor)
            system("say 'Elevator is going down to floor: '" + str(desired_floor))
            elevator_position -= 1
            time.sleep(3)
            os.system('cls||clear')
            print("Current Floor: ", elevator_position)
            system("say 'Current Floor: '" + str(elevator_position))
        else:
            print("Elevator is approaching floor: ", desired_floor)
            system("say 'Elevator is approaching floor: '" + str(desired_floor))
            time.sleep(3)
            os.system('cls||clear')
            print("Current Floor: ", desired_floor)
            system("say 'Current Floor:'" + str(desired_floor))
            time.sleep(2)
            os.system('cls||clear')
            print("Opening doors")
            system("say 'Current Floor:'")
            time.sleep(5)
            break





