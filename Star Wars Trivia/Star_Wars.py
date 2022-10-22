from questions import Quiz

def intro_message():
    """
    Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
    Returns true regardless of any key pressed.
    """
    print("Welcome to this Star Wars quiz! \nAre you ready to test your knowledge about Star Wars?")
    print("There are a total of 10 questions, you can skip a question anytime by typing 'skip'")
    input("Press any key to start the fun, MAY THE FORCE BE WITH YOU! ")
    return True

# Make it so the attempts quit game once attempts == 0 

def check_ans(question, ans, attempts, score):
    if Quiz[question]['Answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} attempts left! \n")
        
intro = intro_message()
while True:
    score = 0
    for question in Quiz:
        attempts = 3
        while attempts > 0:
            print(Quiz[question]['Question'])
            answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break   
            attempts -= 1 
        if attempts == 0:                  
                print("YOU LOSE!! MAY THE FORCE BE WITH YOU")
                break
    break

print(f"Your final score is {score}!\n\n")
print("Thanks for playing! May the Force be with You!")