<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Text To Word</title></head><body><p data-pm-slice="1 1 []"># Tic Tac Toe Game in Python</p>
<p>&nbsp;</p>
<p>def print_board(board):</p>
<p>for row in board:</p>
<p>print(" | ".join(row))</p>
<p>print("-" * 5)</p>
<p>&nbsp;</p>
<p>def check_winner(board, player):</p>
<p># Check rows</p>
<p>for row in board:</p>
<p>if all(s == player for s in row):</p>
<p>return True</p>
<p># Check columns</p>
<p>for col in range(3):</p>
<p>if all(board[row][col] == player for row in range(3)):</p>
<p>return True</p>
<p># Check diagonals</p>
<p>if all(board[i][i] == player for i in range(3)):</p>
<p>return True</p>
<p>if all(board[i][2-i] == player for i in range(3)):</p>
<p>return True</p>
<p>return False</p>
<p>&nbsp;</p>
<p>def is_full(board):</p>
<p>return all(all(cell != " " for cell in row) for row in board)</p>
<p>&nbsp;</p>
<p>def tic_tac_toe():</p>
<p>board = [[" " for _ in range(3)] for _ in range(3)]</p>
<p>current_player = "X"</p>
<p>&nbsp;</p>
<p>while True:</p>
<p>print_board(board)</p>
<p>print(f"Player {current_player}'s turn.")</p>
<p>&nbsp;</p>
<p>try:</p>
<p>row = int(input("Enter row (0-2): "))</p>
<p>col = int(input("Enter column (0-2): "))</p>
<p>if row not in range(3) or col not in range(3):</p>
<p>print("Invalid input! Enter numbers between 0 and 2.")</p>
<p>continue</p>
<p>if board[row][col] != " ":</p>
<p>print("Cell already taken! Try again.")</p>
<p>continue</p>
<p>except ValueError:</p>
<p>print("Invalid input! Enter numbers only.")</p>
<p>continue</p>
<p>&nbsp;</p>
<p>board[row][col] = current_player</p>
<p>&nbsp;</p>
<p>if check_winner(board, current_player):</p>
<p>print_board(board)</p>
<p>print(f"Player {current_player} wins!")</p>
<p>break</p>
<p>&nbsp;</p>
<p>if is_full(board):</p>
<p>print_board(board)</p>
<p>print("It's a tie!")</p>
<p>break</p>
<p>&nbsp;</p>
<p>current_player = "O" if current_player == "X" else "X"</p>
<p>&nbsp;</p>
<p>if __name__ == "__main__":</p>
<p>tic_tac_toe()</p></body></html>