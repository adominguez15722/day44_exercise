"""Restaurant rating lister."""


# put your code here

def ratings():
    rate_dict = {}
    with open("scores.txt", mode="rt", encoding="utf-8") as rest_rate:
        scores = rest_rate.readlines()

    rest_name = input("What is restaurant you have tried? ")
    rest_rating = input("On a scale from 1-5, how would you rate that restaurant? ")

    rate_dict[rest_name] = rest_rating

    for i in scores:
        i = i.split(":")
        rate_dict[i[0]] = i[1].strip("\n")
    rate_dict = sorted(rate_dict.items())
    
    for items in rate_dict:
        print(f"{items[0]}" + " is rated at " + f"{items[1]}")
     

ratings()

