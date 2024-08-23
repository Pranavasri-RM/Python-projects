import random

words = [
    {"Spanish": "Hola", "English": "Hello"},
    {"Spanish": "Adiós", "English": "Goodbye"},
    {"Spanish": "Por favor", "English": "Please"},
    {"Spanish": "Gracias", "English": "Thank you"},
    {"Spanish": "Sí", "English": "Yes"},
    {"Spanish": "No", "English": "No"},
    {"Spanish": "Perdón", "English": "Sorry"},
    {"Spanish": "¿Cómo estás?", "English": "How are you?"},
    {"Spanish": "Buenos días", "English": "Good morning"},
    {"Spanish": "Buenas noches", "English": "Good night"},
    {"Spanish": "Hasta luego", "English": "See you later"},
    {"Spanish": "¿Hablas inglés?", "English": "Do you speak English?"},
    {"Spanish": "No entiendo", "English": "I don't understand"},
    {"Spanish": "¿Puedes ayudarme?", "English": "Can you help me?"},
    {"Spanish": "¿Cuánto cuesta?", "English": "How much does it cost?"},
    {"Spanish": "¿Dónde está el baño?", "English": "Where is the bathroom?"},
    {"Spanish": "Me llamo", "English": "My name is"},
    {"Spanish": "Amigo", "English": "Friend"},
    {"Spanish": "Familia", "English": "Family"},
    {"Spanish": "Casa", "English": "House"},
    {"Spanish": "Coche", "English": "Car"},
    {"Spanish": "Libro", "English": "Book"},
    {"Spanish": "Ciudad", "English": "City"},
    {"Spanish": "País", "English": "Country"},
    {"Spanish": "Calle", "English": "Street"},
    {"Spanish": "Comida", "English": "Food"},
    {"Spanish": "Agua", "English": "Water"},
    {"Spanish": "Leche", "English": "Milk"},
    {"Spanish": "Café", "English": "Coffee"},
    {"Spanish": "Cerveza", "English": "Beer"},
    {"Spanish": "Manzana", "English": "Apple"},
    {"Spanish": "Pan", "English": "Bread"},
    {"Spanish": "Queso", "English": "Cheese"},
    {"Spanish": "Perro", "English": "Dog"},
    {"Spanish": "Gato", "English": "Cat"},
    {"Spanish": "Pájaro", "English": "Bird"},
    {"Spanish": "Escuela", "English": "School"},
    {"Spanish": "Profesor", "English": "Teacher"},
    {"Spanish": "Estudiante", "English": "Student"},
    {"Spanish": "Bicicleta", "English": "Bicycle"},
    {"Spanish": "Autobús", "English": "Bus"},
    {"Spanish": "Tren", "English": "Train"},
    {"Spanish": "Avión", "English": "Airplane"},
    {"Spanish": "Estación de tren", "English": "Train station"},
    {"Spanish": "Hospital", "English": "Hospital"},
    {"Spanish": "Farmacia", "English": "Pharmacy"},
    {"Spanish": "Supermercado", "English": "Supermarket"},
    {"Spanish": "Dinero", "English": "Money"},
    {"Spanish": "Banco", "English": "Bank"},
    {"Spanish": "Tiempo", "English": "Time"},
    {"Spanish": "Amor", "English": "Love"}
]

def quiz_user(words):
    random.shuffle(words)
    score = 0

    for i in range(10):
        word = words[i]
        print(f"What is the English translation of '{word['Spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = str(word['English']).lower()

        if user_answer == correct_answer:
            print("Correct!!\n")
            score += 1
        else:
            print(f"wrong answer!! The correct answer is '{word['English']}'.\n")
    
    print(f"Quiz complete! Your score is {score}/10")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz!!")
    quiz_user(words)

if __name__ == "__main__":
    main()