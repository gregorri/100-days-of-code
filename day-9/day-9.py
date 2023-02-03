# student_score = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for student in student_score:
#     score = student_score[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)

# travel_log = [
# {
#     "country": "France",
#     "visits": 12,
#     "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#     "country": "Germany",
#     "visits": 5,
#     "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]

# def add_new_country(country, visits, cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = visits
#     new_country["cities"] = cities
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        highest_bid = 0
        winner = ""
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")
    elif should_continue == "yes":
        clear()
bids = {}

# while True:
#   name = input("Enter your name: ")
#   bid = input("Enter your bid: ")
  
#   # Check if bid is valid
#   if bid.isdigit() == False:
#     print("Invalid bid, please enter a number.")
#     continue
#   bid = int(bid)
  
#   bids[name] = bid
  
#   another_bidder = input("Is there another bidder? (yes/no) ")
#   if another_bidder.lower() == "no":
#     break
#   else:
#     print("\033c") # Clear the screen for the next bidder

# # Determine the winner and their winning bid
# winning_bid = max(bids.values())
# winner = [key for key, value in bids.items() if value == winning_bid]

# # Print the winner and their winning bid
# print("The winner is:", winner[0])
# print("Winning bid:", winning_bid)
