"""Restaurant rating lister."""


# put your code here
import sys
import random

def ratings():
    rate_dict = {}
    with open("scores.txt", mode="rt", encoding="utf-8") as rest_rate:
        scores = rest_rate.readlines()
    
    answer = int(input("What would you like to do? \n" "1. Rate a new restaurant? \n"  "2. See all restaurants and ratings \n"  "3. Quit \n"))
    
    while answer not in range(0, 4):
        answer = int(input("Need to pick an answer between 1-3! "))
        if answer in range(0, 4):
            break
    
    if answer == 1:
    
        rest_name = input("What is restaurant you have tried? ")
        rest_rating = int(input("On a scale from 1-5, how would you rate that restaurant? "))

        while rest_rating not in range(0,6):
            rest_rating = int(input("Need a rating between 1-5! "))
            if rest_rating in range(0, 6):
                break
        rate_dict[rest_name] = rest_rating
    
    elif answer == 2:
        
        for i in scores:
            i = i.split(":")
            rate_dict[i[0]] = i[1].strip("\n")
        rate_dict = sorted(rate_dict.items())
        
        for items in rate_dict:
            print(f"{items[0]}" + " is rated at " + f"{items[1]}")
    
    else:
        sys.exit()
        
    
ratings()

