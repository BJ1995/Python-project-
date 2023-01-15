# Python-project-
Multiple choice questions 
from question import Question

question_prompt = [
    "What is the colour of Apple? \n(a) green\n(b) purple\n(c) mangero\n\n",
    "what is the colour of orange? \n(a) red\n(b) blue\n(c) green\n\n",
    "What is the colour of strawberry? \n(a) green\n(b) purple\n(c) red\n\n",
    "what is the colour of salad? \n(a) white\n(b) blue\n(c) green\n\n"

]
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    #because of the for loop in the program, each line here is now question,
    #because the loop said "for question in questions" relating it to class, its now (question.prompt, question.answer)
    Question(question_prompt[0], "b"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "c"),
    Question(question_prompt[3], "a")


]
def run_test(questions):
    score = 0
    for question in questions:
 #create a variable called answer that will store the input
        answer = input(question.prompt)
        if question.answer == answer:
            score += 1

    print("you got " + str(score)+ "/" + str(len(questions))+ " correct.")

run_test(questions)

