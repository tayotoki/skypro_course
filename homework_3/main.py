from utils import questions


def get_full_stats():
    user_result = [
        question.points
        for question in questions
        if question.points
    ]

    return f"Вот и всё!\n" \
           f"Отвечено {len(user_result)} вопроса " \
           f"из {len(questions)}\n" \
           f"Набрано баллов: {sum(user_result)}"


def main():
    print("Игра начинается!\n")

    for question in questions:
        question.user_answer = input(f"{question}\n")
        print(question.feedback, end="\n")

    print(get_full_stats())


if __name__ == "__main__":
    main()
