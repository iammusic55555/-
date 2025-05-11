def main():
    questions = [
        {
            "question": "Какой химический элемент обозначается символом 'O'?",
            "options": ["Олово", "Кислород", "Золото", "Серебро"],
            "answer": 1
        },
        {
            "question": "Сколько сторон у правильного шестиугольника?",
            "options": ["5", "6", "8", "7"],
            "answer": 1
        },
        {
            "question": "Какой океан самый большой на планете?",
            "options": ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"],
            "answer": 2
        },
        {
            "question": "Кто написал роман 'Война и мир'?",
            "options": ["Достоевский", "Гоголь", "Чехов", "Толстой"],
            "answer": 3
        },
        {
            "question": "Что из этого — планета?",
            "options": ["Луна", "Сириус", "Марс", "Полярная звезда"],
            "answer": 2
        }
    ]

    prize_levels = ["1 000", "5 000", "10 000", "50 000", "1 000 000"]

    print("Добро пожаловать в игру 'Кто хочет стать миллионером!'\n")

    for i, q in enumerate(questions):
        print(f"Вопрос {i + 1}: {q['question']}")
        for idx, option in enumerate(q["options"]):
            print(f"  {idx + 1}. {option}")

        while True:
            try:
                choice = int(input("Ваш ответ (1-4): ")) - 1
                if choice < 0 or choice > 3:
                    raise ValueError
                break
            except ValueError:
                print("Введите число от 1 до 4.")

        if choice == q["answer"]:
            print(f"Правильно! Вы выиграли {prize_levels[i]} рублей.\n")
        else:
            print("Неправильно. Игра окончена.")
            print(f"Правильный ответ: {q['options'][q['answer']]}")
            break
    else:
        print("Поздравляем! Вы стали миллионером!")

if __name__ == "__main__":
    main()