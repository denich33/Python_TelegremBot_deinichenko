from colorama import init, Fore, Back, Style
init(autoreset=True)

def draw_board(board):
  # запустить двойной цикл, рисующий карту "поячеечно"
  for i in range(3):
    for j in range(3):
      # Формат вывода ноликов
      if board[j][i] == 'O':
        print(Style.BRIGHT + Back.BLUE + Fore.GREEN + str(board[j][i]), end = "")
        if j != 2:
          print('', end = " | ")
      # Формат вывода крестиков
      elif board[j][i] == 'X':
        print(Style.BRIGHT + Back.YELLOW + Fore.MAGENTA + str(board[j][i]), end = "")
        if j != 2:  
          print('', end = " | ")
      # Формат вывода пустых клеток
      elif  j != 2:
        print(Back.WHITE + str(board[j][i]), end = " | ")
      else:
        print(Back.WHITE + str(board[j][i]), end = "")       
    if i == 2:    # Убераем лишнее подчёркивание
      print('\n')    # Делаем отступ для красоты
      break
    # поставить разделители строк
    print("\n---------")

def ask_and_make_move(player, board):
  x, y = ask_move(player, board)
  # координаты x, y взять из функции ask_move(player, board)
  make_move(player, board, x, y)    # "Полу-воидная" функция

def ask_move(player, board):
  while True:
    coord_string = input(f"Игрок {player}, введите координаты столбца X и строки Y (от '0 0' до '2 2'): ").strip()
    # Отсеиваем любые некорректные данные (
    if len(coord_string) == 3 and (coord_string[0] and coord_string[2]).isnumeric() and coord_string.find(' ') == 1:
      if 0 <= int(coord_string[0]) <= 2 and 0 <= int(coord_string[2]) <= 2:
        x, y = coord_string.split()
        return int(x), int(y)
        break
      else:
        print(Style.BRIGHT + Fore.RED + 'Некорректные координаты.')
    else:
      print(Style.BRIGHT + Fore.RED + 'Некорректные координаты.')

def make_move(player, board, x, y):
  # Проверяем, свободно ли место
  if board[x][y] == " ":
    # если свободно, записать значение игрока (Х или 0) в ячейку
    board[x][y] = player
    print(Style.BRIGHT + Fore.GREEN + 'Ход выполнен.')
    print('\n')
  else:
    print(Style.BRIGHT + Fore.RED + "Ячейка занята. Повторите ход.")
    print('\n')
    ask_and_make_move(player, board)    # Повтор запроса

def check_win(player, board):
  # проверить, совпадают ли значения в строках и столбцах
  for i in range(3):
    # проверить, совпадают ли значения в строках
    if board[i] == [player, player, player]:
      return True
    # проверить, совпадают ли значения в столбцах
    if board[0][i] == player and board[1][i] == player and board[2][i] == player:
      return True
  # проверить, совпадают ли значения на диагонали из верхнего левого в нижний правый угол
  if board[0][0] == player and board[1][1] == player and board[2][2] == player:
    return True
  # проверить, совпадают ли значения на диагонали из верхнего правого в нижний левый угол
  if board[0][2] == player and board[1][1] == player and board[2][0] == player:
    return True
  return False

def check_the_tie_game(board):
  # проверить, произошла ли ничья
  tie_game = False
  for row in board:
    for cell in row:
      if cell == " ":
        tie_game = True 
  if not tie_game:
    draw_board(board)
    print(Style.BRIGHT + Back.RED + Fore.GREEN + 'Ничья!')
  return tie_game

def tic_tac_toe():
  # задать бесконечненый цикл, который проводит игры
  while True:
    board = [[" " for i in range(3)] for j in range(3)]
    player = "X"
    # задать бесконечнный цикл, который проводит конкретную игру
    while True:
      # нарисовать игровое поле
      draw_board(board)
      # запросить ход
      ask_and_make_move(player, board)
      # проверить, выиграл ли игрок
      if check_win(player, board):
        draw_board(board)
        print(Style.BRIGHT + Back.RED + Fore.GREEN + f"Игрок {player}, вы выиграли!")
        break
      # Проверка на ничью, если произошла ничья, завершить цикл
      if not check_the_tie_game(board):
        break
      # Переключение игрока
      player = "O" if player == "X" else "X"
    # спросить игроков, хотят ли они сыграть еще раз
    while True:
      restart = input("Хотите сыграть еще раз? (y/n) ")
      print('\n')
      # Отсеиваем некорректные ответы
      if restart.lower() == "n" or restart.lower() == "y":
        break
      else:
        print(Style.BRIGHT + Fore.GREEN + 'Некорректный ответ.')
    if restart.lower() == "n":
      break

tic_tac_toe()
