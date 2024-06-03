from Question import Question

question_propmts = [
    "Who created Python?\n(a) Guido van Rossum\n(b) James Gosling\n(c) Bill Joy\n", 
    "First network was called?\n(a) WWW\n(b) ARPANET\n(c) INTERNET\n", 
    "8 in binary is..\n(a) 0100\n(b) 1000\n(c) 0110\n"
]

questions = [
    Question(question_propmts[0],"a"),
    Question(question_propmts[1],"b"),
    Question(question_propmts[2],"b")
]

ch=""
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+=1
    print("Your score is "+str(score)+" out of "+str(len(questions)))
    ch=input("Do you want to try again? (Y/N): ")
    if ch == "Y" or ch == "y":
        run_test(questions)
    else:
        return
        


run_test(questions)