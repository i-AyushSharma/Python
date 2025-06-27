questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]
questions = ["Which language is used to create FB", "French", "Python", "JavaScript", "None", 3]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for ruppes {levels[i]}")
    print(f"1. {questions[1]}                  2. {questions[2]}")
    print(f"3. {questions[3]}                  4. {questions[4]}")
    reply = int(input("Enter your answer (1-4): "))
    if(reply == question[-1]):
       print(f"Correct answer, you have won ruppes{levels[i]}")
    if(i == 4):
        money = 10000
    elif(i == 9):
        money = 32000
    elif(i == 14):
        money = 10000000
    else:
        print("Wrong Answer!")
        break