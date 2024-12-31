
questions = [   
     {
        'Ques' : 'NameShares with no face value are known as: ',
        'Options': [ 'A. Equal Stock' , 'B. Debt Equity Stock' , 'C. At par stock' , 'D. No par stock'],
        'Answers': 'D'
    },
    {
        'Ques' : 'The basis of consumer surplus, according to Marshall, is: ',
        'Options': [ 'A. Law of diminishing MU' , 'B. Law of proportions' , 'C. Law of Equi-MU' , 'D. All of the above '],
        'Answers': 'A'
    },
    {
        'Ques' : 'What kinds of costs are paid from Gross Profit? ',
        'Options': [ 'A.  Selling expenses' , 'B. General expenses' , 'C. Financial expenses' , 'D. All of the above'],
        'Answers': 'D'
    },
    {
        'Ques' : 'Which of the following makes the most FDI trades? ',
        'Options': [ 'A.  ASEAN' , 'B.  USA' , 'C.  Japan, China, and the UK' , 'D. EU, India, and the USA'],
        'Answers': 'A'
    }
]



def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['Ques'])
        for option in question['Options']:
            print(option)
        answer = input('Enter your Answers [A,B,C,D]: ').upper()
        if answer == question['Answers']:
            print("Correct answer, Horrah!! \n ")
            score += 2
        else:
            print(f"wrong answer, the correct answer is:, {question['Answers']} \n")
    
    print(f'You got {score} out of {len(questions) * 2} questions correct')


run_quiz(questions)
