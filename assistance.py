message1 = "=" * 40 + "\n  Welcome to the word memorization game\n" + "=" * 40

option = "<<<< Press 'n' if you do not know the word ,'skip' to skip the word and press 'q' to quit the game >>>>"


def score_calc(number):
    if number == 1:
        print(f"Correct, you have memorized {number} word")
    else:
        print(f"Correct, you have memorized {number} words")


def correct_answers(current_line):
    total = ""
    with open("SavedWords.txt", "a", encoding="utf-8") as SavedWords:
        SavedWords.write(current_line + "\n")

    with open("2500 English Words.txt", "r", encoding="utf-8") as all_words:
        all_en_words = all_words.read().splitlines()
        for word in all_en_words:
            if word != current_line:
                total += word + "\n"

    with open("2500 English Words.txt", "w", encoding="utf-8") as Not_Saved_Words:
        Not_Saved_Words.write(total)


def rate(rank):
    if rank >= 7:
        print(f"You did will,  you have memorized {rank} words, Great jop.")
    elif 4 <= rank < 7:
        print(f"Not bad, you have memorized just {rank} words, Try to be better next time.")
    elif rank == 1:
        print(f"you have memorized just {rank} word, Be serious man ")
    elif rank == 0:
        exit()
    else:
        print(f"I guess it's not your lucky day. you have memorized just {rank} words ")
