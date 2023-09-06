"""Restaurant rating lister."""


# put your code here
import random
# restaurant = []
def read_scores():
    scores = {}
    file = open("scores.txt")

    for line in file:
        restaurant, score = line.rstrip().split(":")
        scores[restaurant] = int(score)
    return scores

def add_user_res_score(scores):
    restaurant = input("Please enter restaurant name:")
    score = int(input("Please enter the restaurant rating:"))

    scores[restaurant] = score

def print_score(scores):
    for restaurant, score in sorted(scores.items()):
        print(f"{restaurant} is rated at ... {score}")

scores = read_scores()  
# add_user_res_score(scores)
# print_score(scores)

while True:
    print("Hello, this is our new resturant rating application called Belp!")
    userchoice = input("""What would you like to do
(R)Seeing all the ratings(in alphabetical order)
(A)Adding a new restaurant(and rating it)
(U)Update a random restaurant
(Q)uit \n""").upper()
    if userchoice == "R":
        print_score(scores)
    elif userchoice == "A":
        add_user_res_score(scores)
        print_score(scores)
    elif userchoice == "U":
        ranres = random.choice(list(scores))
        print(f"This is your restaurant and its rating is {ranres}.")
        
    elif userchoice == "Q":
        exit()

    else:
        print("Sorry, that was an invalid input")    
        continue
                