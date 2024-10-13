import random

# Declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
name = input("What is your name? ")

# Declare a variable question, and assign it to a "Yes" or "No" question you’d like to ask the Magic 8-Ball.
question = input("Enter a 'yes' or 'no' question for the Magic 8-ball: ")

# We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer.
answer = ""

# Create a variable to store the randomly generated value
random_number = random.randint(1, 9)

# Utilise control flow with an if/elif/else statement to assign different answers for each randomly generated value
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

# Print the name, question, and answer using f-strings
print(f"{name} asks: {question}")
print(f"Magic 8-Ball's answer: {answer}")
