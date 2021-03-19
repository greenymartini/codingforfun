

class questions:
    def __init__(self, prompt, answer):
        self.prompt=prompt
        self.answer=answer

questions_prompts= [
    "what does anti-facsim mean to you? \n (a) punch nazis \n (b) communism \n (c) daily fight against hate \n (d) all of the above",
    "What have you done to fight nazis? \n (a) I punched nazis \n (b) joined a local Antifa group \n (c) I moved to a region threatend to become a >National befreite Zone< plus all of the above \n (d) counting on the police to solve the problem for me bc we are living in a >Rechtsstaat<  "

]



questionair = [
    questions(questions_prompts[0], "d"),
    questions(questions_prompts[1], "c")

]

def run_test(questionair):
    score=0
    
    for questions in questionair:
        answer=input(questions.prompt + "\n your answer:  ")
        if answer == questions.answer:
            score+=1
    if score == 1:
        print ("You will become an anti-facist pretty sure. enjoy the installation and stay safe!")
    elif score > 1:
        print("You are a fullon anti-facist")
    else: 
        print("\n you should start reading some books of our wonderful table in the Kategorie >How to start fighting for a better future<")

run_test(questionair)

