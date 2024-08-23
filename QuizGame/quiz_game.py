questions = [
    {
        "prompt": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "prompt": "Which river is considered the holiest in India?",
        "options": ["A. Yamuna", "B. Godavari", "C. Ganga", "D. Narmada"],
        "answer": "C"
    },
    {
        "prompt": "Which Indian festival is known as the festival of lights?",
        "options": ["A. Diwali", "B. Holi", "C. Eid", "D. Pongal"],
        "answer": "A"
    },
    {
        "prompt": "In which year did India gain independence from British rule?",
        "options": ["A. 1947", "B. 1950", "C. 1930", "D. 1945"],
        "answer": "A"
    },
    {
        "prompt": "What is the national animal of India?",
        "options": ["A. Elephant", "B. Lion", "C. Peacock", "D. Tiger"],
        "answer": "D"
    },
    {
        "prompt": "Who was the first Prime Minister of India?",
        "options": ["A. Sardar Vallabhbhai Patel", "B. Jawaharlal Nehru", "C. Rajendra Prasad", "D. Indira Gandhi"],
        "answer": "B"
    },
    {
        "prompt": "Which dance form originates from the Indian state of Kerala?",
        "options": ["A. Kathakali", "B. Bharatanatyam", "C. Odissi", "D. Kathak"],
        "answer": "A"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option);  

        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == question["answer"]:
            print("Correct, hooray!!\n")
            score += 1
        else:
            print("Wrong!!! The correct answer was ",question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} answers correct.")

run_quiz(questions)