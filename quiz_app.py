print("-----WELCOME TO QUIZ-----")
user = input("YOU WANT TO START THE QUIZ Y/N :   ").lower()
score = 0
if user == "y":
    print("starting quiz")
    question = {
        "Question 1" : {
            "question":"Which planet in our solar system is commonly known as the Red Planet?",
            "A"      : "Venus",
            "B"      : "Mars" ,
            "C"      : "Jupiter",
            "D"      : "Satum",
            "answer" : "B"
        } , 
        "Question 2" : {
            "question" : "Who was the first President of the United States?",
            "A"        : "Thomas Jefferson",
            "B"        : "Abraham Lincoln",
            "C"        : "George Washington",
            "D"        : "John AdamsShow",
            "answer"   : "C"
        } ,
        "Question 3"  : {
            "question" : "Which is the largest ocean on Earth?",
            "A"        : "Atlantic Ocean",
            "B"        : "Indian Ocean",
            "C"        : "Pacific Ocean",
            "D"        : "Arctic Ocean",
            "answer"   : "C"
        }
    }
    for key, value in question.items():
        print("\n"+ key)
        print(value["question"])
        print("A " , value ["A"])
        print("B " , value ["B"])
        print("C " , value ["C"])
        print("D " , value ["D"])
        user_name = input("YOUR OPTION : ").upper()
        if user_name == value["answer"]:
            print("you are correct ")
            score += 1
        else:
            print("wrong")
            print("correct ans:", value["answer"])
print("\n quiz finiesd")
print("your score", score)


