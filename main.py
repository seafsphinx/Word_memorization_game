from assistance import *
file = open('2500 English Words.txt', "r", encoding="utf-8")
print(message1)
print(option)
words = file.read().splitlines()
answer = ""
score = 0
for n in range(10):
    word = words[n].split()
    en_word = word[0]
    ar_word = word[1]
    while answer != ar_word:
        answer = input(f"What is the meaning of ({en_word}) in Arabic : ")
        if answer == ar_word:
            score += 1
            score_calc(score)
            correct_answers(words[n])
            print("-"*50)
        elif answer == "skip":
            print("The word has been skipped successfully")
            print("-"*50)
            break
        elif answer == "n":
            print(f"The meaning of ({en_word}) is : ({ar_word})")
            print("-" * 50)
            break

        # here is the problem , if the User Type Review it should ask him about the words in SavedWords.txt
        elif answer == "review":
            with open("SavedWords.txt", "r", encoding="utf-8") as SavedWords:
                Saved = SavedWords.read().splitlines()
                for w in range(len(Saved)):
                    word = Saved[w].split()
                    en = word[0]    # It is said that the index is out of the range
                    ar = word[1]
                    while answer != ar:
                        print("-"*50)
                        answer = input(f"What is the meaning of ({en}) in Arabic : ")
                print("done, lets continue")

        elif answer == "q":
            print("Finish")
            rate(score)
            exit()
        else:
            print("Wrong, Try again")





