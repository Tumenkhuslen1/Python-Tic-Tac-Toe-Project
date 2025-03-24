import random
class TicTacToe:
    
    match_number = 0
    wins = 0
    losses = 0
    ties = 0
    if (wins + losses + ties) != 0:
        win_percentage = wins/(wins + losses + ties)

    def __init__(self):
        self.board = []
        TicTacToe.match_number += 1
        self.game = TicTacToe.match_number

    def side(self):
        if (random.randint(0,1)) == 1:
            return "X"
        else:
            return "O"
    
    def make_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)
    
    def show_board(self): #shows the board
        print("  ") #adds a space for readability
        for row in self.board: #goes by nested lists
            for item in row: #prints the items inside the nested lists
                print(item, end="  ") #adds spaces for readability of the game
            print() #prints to the next row and then the items of the nested list which constitute the tic-tac-toe board
    
    def swap_player_turn(self, player): #swaps players
        return "X" if player == "O" else "O"
    
    def game_over(self, player): #checks if the game is won or lost or tied
        win = None
        n = len(self.board)

        # rows check
        for i in range(n): # 0, 3
            win = True #Sets win to true so it can return the correct value if a player won horizontally
            #Which also consequently doesn't return none or false incorrectly when a player wins
            for j in range(n):
                if self.board[i][j] != player: #loops through 
                    win = False
                    break
                    # goes to the next row if it there is no winning tile here
            if win:
                return win

        # columns check
        for i in range(n):
            win = True #Sets win to true so it can return the correct value if a player won vertically
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
                    # goes to the next column if it there is no winning tile here
            if win:
                return win

        # diagonals check
        for i in range(n):
            win = True #Sets win to true so it can return the correct value if a player won diagonally
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        
        for i in range(n):
            win = True
            if self.board[i][-i-1] != player:
                win = False
                break
        if win:
            return win
        
        return win
    
    def set(self, player): #asks the user where they want to play their game
        valid_input = False  # Flag to check if the input is valid

        while not valid_input:
            x = input("Please enter a horizontal row to mark the board from 1, 2, or 3: ")
            y = input("Please enter a vertical column to mark the board from 1, 2, or 3: ")

            # Check if the inputs are numeric
            if not x.isdigit() or not y.isdigit():
                print("Invalid input. Please enter numeric values between 1 and 3.")
                continue

            x = int(x)
            y = int(y)

            # Check if the input is within the valid range
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Out of range. Please enter values between 1 and 3 for both row and column.")
                continue

            # Check if the selected spot is already taken
            if self.board[x - 1][y - 1] != "-":
                print("This spot is already taken. Please choose a different spot.")
                continue  # Continue to ask for input if the spot is already taken

            # If all checks pass, mark the board with the player's move
            self.board[x - 1][y - 1] = player
            valid_input = True  # Set the flag to True to break out of the loop

    def auto(self, player):
        n = len(self.board)
        store_untouched = [] #stores the indexes of values of untouched values
        for i in range(n):
            for j in range(n):
                if self.board[i][j] != "X" and self.board[i][j] != "O":
                    store = [i, j]
                    store_untouched.append(store)
        
        store_len = len(store_untouched)
        if store_len == 0:
            return False
        comp_choice = random.randint(0, store_len - 1)
        comp_area = store_untouched[comp_choice]

        x = comp_area[0]
        y = comp_area[1]
        self.board[x][y] = player

    def draw(self):
        n = len(self.board)
        for i in range(n):
            for j in range(n):
                if self.board[i] != "-":
                    return False
        return True

    def start(self):
        self.make_board()

        player = self.side()
        if player == "X":
            print(f"You are Player {player}.")
        else:
            print(f"You are Player {player}.")

        while True:
            self.show_board()
            self.set(player)
            if self.game_over(player):
                self.show_board()
                print(f"Player {player} wins the game.")
                break
            if self.draw():
                self.show_board()
                print("It's a draw. No player won the game.")
                break
            player = self.swap_player_turn(player)
            self.auto(player)
            if self.game_over(player):
                self.show_board()
                print(f"Player {player} wins the game.")
                break
            if self.draw():
                self.show_board()
                print("It's a draw. No player won the game.")
                break
            player = self.swap_player_turn(player)


game1 = TicTacToe()
game1.start()