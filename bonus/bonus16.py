import json

with open("C:/Users/c13673e/app1/pythonProject/.venv/bonus/questions.json" , 'r') as file: 
    content = file.read()

data = json.loads(content)

for question in data: 
    print(question["question_text"])
    for index, alternative in enumerate(question["alternitives"]):
        print(index+ 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else: 
        resul = "Wrong Answer"

    message = f"{result} {index + 1} - Your answer: {question['user_choice']}, Correct answer: {question['correct_answer']}"
    print(message)


#print(data)
print(score, "/", len(data))