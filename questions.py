rom Questions import Question

question_prompt = [
  "What color is sky? \n (a) blue \n (b) red \n\n",
  "What color is grass? \n (a) green \n (b) blue\n\n"
]

questions = [Question(question_prompt[0],"a"),
             Question(question_prompt[1],"a") ]

  
def run_questions(questions):
  score=0
  for question in questions:
    answer= input(question.prompt)
    if answer == question.response:
      score +=1

  print("you got" + str(score) + "/" + str(len(questions)))

run_questions(questions)
