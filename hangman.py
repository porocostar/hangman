def hangman(word):
    wrong = 0
    stages = ["",
              "________        ",
              "|      |        ",
              "|      |        ",
              "|      O        ",
              "|     /|\       ",
              "|     / \       ",
              "|               "
              ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hanged_Man!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "一文字予想して"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You Lose! Correct Answer is {}.".format(word))

hangman("dog")