import json

FILENAME = "FlashCards.json"

def load_flashcards():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except:
        return {}

def save_flashcards(cards):
    with open(FILENAME, "w") as f:
        json.dump(cards, f, indent=4)

def teacher_mode():
    cards = load_flashcards()
    print("Add flashcards (type 'exit' to stop):")
    while True:
        question = input("Phrase: ")
        if question.lower() == "exit":
            break
        answer = input("Answer: ")
        cards[question] = answer
    save_flashcards(cards)
    print("Flashcards saved!")

def student_mode():
    cards = load_flashcards()
    if not cards:
        print("No flashcards found.")
        return

    score = 0
    streak = 0

    for question in list(cards.keys())[::-1]:  # reverse as simple shuffle
        print(f"\nWhat is the answer to: '{question}'?")
        user_answer = input("Your answer: ").strip()
        correct = cards[question].strip()

        if user_answer.lower() == correct.lower():
            streak += 1
            bonus = streak if streak >= 3 else 0
            print("Correct", f"+{1 + bonus} points" if bonus else "")
            score += 1 + bonus
        else:
            print(f"Wrong the answer: {correct}")
            streak = 0

    print(f"\nYour final score: {score}")

def main():
    mode = input("Choose mode (teacher / student): ").strip().lower()
    if mode == "teacher":
        teacher_mode()
    elif mode == "student":
        student_mode()
    else:
        print("Invalid mode.")

if __name__ == "__main__":
    main()
