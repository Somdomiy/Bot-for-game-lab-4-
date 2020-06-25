board = list(range(1, 10))
huPlayer = "X"
aiPlayer = "O"

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)


def display_instruct():
    """Выводит на экран инструкцию для игрока."""
    print(
        """\nДобро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времён.\nЧтобы сделать ход, введи число от 1 до 9.\nЧисла однозначно соотвествуют полям доски - так, как показано ниже:"""
    )
    draw_board(board)


def ask_yes_no(question):
    """Задаёт вопрос с ответом 'Да' или 'Нет'."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def pieces():
    """Определяет принадлежность перового хода."""
    go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y, n): ")
    if go_first == "y":
        print("\nНу что ж, дают тебе фору: играй крестиками.")
        tmp = 0
    else:
        print("\nТвоя удаль тебя погубит... Буду начинать я.")
        tmp = 1
    return tmp


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")


def take_input_pc(player_token):
    tmp, a = minimax(board, aiPlayer)
    board[a] = player_token


def minimax(newBoard, player):
    global mov
    availSpots = emptyIndexies(newBoard)

    if (winning(newBoard, huPlayer)):
        return -10, 0
    else:
        if (winning(newBoard, aiPlayer)):
            return 10, 0
        else:
            if (len(availSpots) == 0):
                return 0, 0

    moves = []

    i = 0
    while (i < len(availSpots)):
        mov = 0
        tm = newBoard[availSpots[i]-1]
        newBoard[availSpots[i]-1] = player
        if (player == aiPlayer):
            result, a = minimax(newBoard, huPlayer)
            mov = result
        else:
            result, a = minimax(newBoard, aiPlayer)
            mov = result
        newBoard[availSpots[i]-1] = tm
        moves.append(result)
        i += 1

    bestMove = 0
    i = 0
    if (player == aiPlayer):
        bestScore = -10000
        while (i < len(moves)):
            if (moves[i] > bestScore):
                bestScore = moves[i]
                bestMove = i
            i += 1
    else:
        bestScore = 10000
        while (i < len(moves)):
            if (moves[i] < bestScore):
                bestScore = moves[i]
                bestMove = i
            i += 1
    return moves[bestMove], availSpots[bestMove]-1


def emptyIndexies(board):
    def fuc(s):
        if s != "O" and s != "X":
            return 1
        else:
            return 0

    return list(filter(fuc, board))


def winning(board, player):
    if (
            (board[0] == player and board[1] == player and board[2] == player) or
            (board[3] == player and board[4] == player and board[5] == player) or
            (board[6] == player and board[7] == player and board[8] == player) or
            (board[0] == player and board[3] == player and board[6] == player) or
            (board[1] == player and board[4] == player and board[7] == player) or
            (board[2] == player and board[5] == player and board[8] == player) or
            (board[0] == player and board[4] == player and board[8] == player) or
            (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False


def main(board):
    display_instruct()
    counter = pieces()
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input(huPlayer)
        else:
            take_input_pc(aiPlayer)
        counter += 1
        if counter > 4:
            if winning(board, "X"):
                print("О нет, этого не может быть! Неужели ты как-то сумел меня перехитрить белковый? \n" \
                      "Клянусь: я, компьютер, не допущу этого никогда!")
                win = True
                break
            if winning(board, "O"):
                print("Как я и предсказывал, победа в очередной раз осталась за мно!\n" \
                      "Вот ещё один довод в пользу того, что компьютеры превосходят человека решительно во всём.")
                win = True
                break
        if counter == 9:
            print("Тебе несказанно повезло, дружок: ты сумел игру вничью. \n" \
                  "Радуйся же сегодняшнему успеху. Завтра тебе уже не суждено его повторить.")
            break
    draw_board(board)


main(board)
