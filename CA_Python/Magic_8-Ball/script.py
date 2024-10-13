import random

# Ask for the player's name
name = input("What is your name? ")

# Ask for a yes/no question
question = input("Enter a 'yes' or 'no' question for the Magic 8-Ball: ")

# Check if the question is empty
if question.strip() == "":
    print("You must ask a question! The fabric of reality is at risk!")
else:
    # Create a variable to store the randomly generated value
    random_number = random.randint(1, 9)

    # Assign the answer based on the random number generated
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

    # Print the output based on whether the name is empty or not
    if name.strip() == "":  # Check if the name is an empty string or only whitespace
        print(f"Question: {question}")
    else:
        print(f"{name} asks: {question}")

    print(f"Magic 8-Ball's answer: {answer}")
