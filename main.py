def classify(message: str) -> str:
    """
    Определяет категорию обращения:
    - справка
    - жалоба
    - другое
    """

    text = message.lower()

    # Жалоба — пользователь сообщает о проблеме
    complaint_words = [
        "пропал",
        "холодная",
        "холодный",
        "очередь",
        "не работает",
        "сломался",
        "проблема",
    ]

    if any(word in text for word in complaint_words):
        return "жалоба"

    # Справка — запрос именно на получение справки
    if "справк" in text:
        return "справка"

    # Всё остальное
    return "другое"


def generate_answer(category: str, message: str) -> str:
    """
    Создаёт простой черновик ответа
    в зависимости от категории обращения.
    """

    if category == "справка":
        return (
            "Здравствуйте! Для получения справки о месте учёбы "
            "обратитесь в учебный отдел."
        )

    if category == "жалоба":
        return (
            "Спасибо, что сообщили о проблеме. "
            "Мы зафиксировали обращение и передадим информацию "
            "ответственному сотруднику."
        )

    return (
        "Здравствуйте! Спасибо за обращение. "
        "Мы зарегистрировали ваш запрос и передадим его "
        "ответственному сотруднику."
    )


def main():
    try:
        with open("messages.txt", "r", encoding="utf-8") as file:
            messages = [
                line.strip()
                for line in file
                if line.strip()
            ]
    except FileNotFoundError:
        print("Ошибка: файл messages.txt не найден.")
        return

    for number, message in enumerate(messages, start=1):
        category = classify(message)
        answer = generate_answer(category, message)

        print(f"{number}) {message}")
        print(f"   Категория: {category}")
        print(f"   Черновик ответа: {answer}")
        print()


if __name__ == "__main__":
    main()