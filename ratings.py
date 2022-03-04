"""Restaurant rating lister."""


# put your code here
from operator import le
import sys
import random

def ratings():
    rate_dict = {}
    with open("scores.txt", mode="rt", encoding="utf-8") as rest_rate:
        scores = rest_rate.readlines()
    
    for i in scores:
            i = i.split(":")
            rate_dict[i[0]] = i[1].strip("\n")
        
    
    answer = 1
    while answer != 3:
        
        answer = int(input("What would you like to do? \n" "1. Rate a new restaurant \n"  "2. See all restaurants and ratings \n"  "3. Quit \n" "4. Update a random restaurant's rating \n" "5. Update a specific restaurant's rating \n"))
    
        while answer not in range(0, 6):
            answer = int(input("Need to pick an answer between 1-5! "))
            if answer in range(0, 5):
                break
        
        if answer == 1:
        
            rest_name = input("What is restaurant you have tried? ")
            rest_rating = int(input("On a scale from 1-5, how would you rate that restaurant? "))

            while rest_rating not in range(0,6):
                rest_rating = int(input("Need a rating between 1-5! "))
                if rest_rating in range(0, 6):
                    break
            rate_dict[rest_name] = rest_rating

            for i in scores:
                i = i.split(":")
                rate_dict[i[0]] = i[1].strip("\n")
            rate_dict_new = sorted(rate_dict.items())
            
            for items in rate_dict_new:
                print(f"{items[0]}" + " is rated at " + f"{items[1]}")

        elif answer == 2:
            
            # for i in scores:
            #     i = i.split(":")
            #     rate_dict[i[0]] = i[1].strip("\n")
            rate_dict_list = sorted(rate_dict.items())
            
            for items in rate_dict_list:
                print(f"{items[0]}" + " is rated at " + f"{items[1]}")
            
        elif answer == 3:
            sys.exit()

        elif answer == 4:
            restaurants = list(rate_dict.items())
            rand_rest = random.choice(restaurants)
            print('The restaurant you chose is '+ f"{rand_rest[0]}" + ' with a rating of ' + f"{rand_rest[1]}")
            change = int(input('What would you like to change the rating to between 1-5? '))
            
            while change not in range(0,6):
                change = int(input("Need a rating between 1-5! "))
                if change in range(0, 6):
                    break
            rate_dict[rand_rest] = change
            print(f"The {rand_rest[0]} now has a rating of " + f"{change}")
            
            for items in rate_dict:
                print(f"{items[0]}" + " is rated at " + f"{items[1]}")

        elif answer == 5:
            rate_dict_list = sorted(rate_dict.items())
            counter = 1
            
            for items in rate_dict_list:
                print(f"{counter}." f"{items[0]}" + " is rated at " + f"{items[1]}")
                counter += 1

            choice = int(input("Which restaurant do you want to change? "))

            while choice not in range(0, len(rate_dict) + 1):
                choice = int(input("Need a rating between 1-" + f"{len(rate_dict)}" + " "))
                break
            
            if choice in range(0, len(rate_dict) + 1):
                change = int(input("What do you want to change the rating to? "))
                new_choice = choice - 1
                rate_dict[new_choice] = change

ratings()

