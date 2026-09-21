def classify(message: str) -> str:
    text = message.lower()

    complaint_words = [
        "пропал",
        "холодн",
        "очередь",
        "не работает",
        "проблем",
        "сломал",
    ]

    inquiry_words = [
        "как получить",
        "где",
        "хочу записаться",
        "как записаться",
        "можно ли",
    ]

    if any(word in text for word in complaint_words):
        return "жалоба"

    if any(word in text for word in inquiry_words):
        return "справка"

    return "другое"


def make_answer(category: str, message: str) -> str:
    if category == "жалоба":
        return (
            "Спасибо, что сообщили. Мы зафиксировали обращение "
            "и передадим информацию ответственному сотруднику."
        )

    if category == "справка":
        return (
            "Здравствуйте! Спасибо за обращение. "
            "Уточните, пожалуйста, дополнительные детали, чтобы мы могли помочь."
        )

    return (
        "Здравствуйте! Спасибо за обращение. "
        "Мы рассмотрим ваш запрос и сообщим дальнейшие действия."
    )


def main():
    with open("messages.txt", "r", encoding="utf-8") as file:
        messages = [line.strip() for line in file if line.strip()]

    for i, message in enumerate(messages, 1):
        category = classify(message)
        answer = make_answer(category, message)

        print(f"{i}. Обращение: {message}")
        print(f"   Категория: {category}")
        print(f"   Ответ: {answer}")
        print()


if __name__ == "__main__":
    main()