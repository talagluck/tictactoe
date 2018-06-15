

def printBoard(boardArray): #prints the current board
	print(gameBoard[1]+' | '+gameBoard[2]+' | '+gameBoard[3])
	print(gameBoard[4]+' | '+gameBoard[5]+' | '+gameBoard[6])
	print(gameBoard[7]+' | '+gameBoard[8]+' | '+gameBoard[9])
	print("")

def turnPlay(playerMarker,boardArray): #represents one turn
	while True: #use a loop here to insure continuous prompting until proper input
		location = input(f"Please select your location, {turnOrder[(turnCounter)%2+1][0]} \n")
		if location == "0": #array goes from 0 to 10, inclusive, board goes from 1-9, so 0 will get lost without this
			print("Please select a valid location using the numbers 1-9.")
			print("")
		elif location in gameBoard: #if the location is still in the gameboard array
			location = int(location)
			break
		else:
			print("Please select a valid location using the numbers 1-9.")
			print("")

	gameBoard[location] = playerMarker #set location equal to the X or O
	print("")
	if checkWin(boardArray): #check if winner and declare it
		printBoard(gameBoard)
		print(f"{turnOrder[(turnCounter)%2+1][0]} has won!\n")

def checkWin(b): #checks if there is a winner; b = boardarray (gameBoard) 
	return((b[1]==b[2]) and (b[2]==b[3]) or #top
		(b[4]==b[5]) and (b[5]==b[6]) or #mid horizontal
		(b[7]==b[8]) and (b[8]==b[9]) or #bottom
		(b[1]==b[4]) and (b[4]==b[7]) or #left
		(b[2]==b[5]) and (b[5]==b[8]) or #mid vertical
		(b[3]==b[6]) and (b[6]==b[9]) or #right
		(b[1]==b[5]) and (b[5]==b[9]) or #diagonal from upper left
		(b[3]==b[5]) and (b[5]==b[7])) #diagonal from upper right

#main game
print("Welcome to Tic-Tac-Toe!")
player1 = str(input("Please enter the name of player 1 (marked by 'X')"))
player2 = str(input("Now, please enter the name of player 2 (marked by 'O')"))

playAgain = ""
keepSamePlayers = ""

while playAgain != "n": #to loop in case players want another game
	gameBoard = list(map(str,range(0,10))) #establish gameboard as range between 0-9 (start with 0 to make indexing easier)
											#convert to str to make printing possible
	turnCounter = 1
	
	if keepSamePlayers == "n": #select new players if that option has been selected after a game
		player1 = str(input("Please enter the name of player 1 (marked by 'X')"))
		player2 = str(input("Now, please enter the name of player 2 (marked by 'O')"))
	
	turnOrder = {2:[player1,"X"],1:[player2,"O"]}

	while checkWin(gameBoard) == False: #keep turns going until there's a winner 
		printBoard(gameBoard)
		print(f"Turn #{turnCounter}")	
		turnPlay(turnOrder[(turnCounter)%2+1][1],gameBoard)
		turnCounter +=1
		if turnCounter > 9: #account for a tie
			printBoard(gameBoard)
			print("It's a tie! Game over.")
			print("")
			break

	while True: #use a loop here to insure continuous prompting until proper input
		playAgain = input("Play again? y/n \n")
		if playAgain not in ["y","n"]:
			print("Please enter 'y' if you would like to play again, or 'n' if you would like to exit\n")
		elif playAgain == "n":
			break	
		else:
			while True: #use a loop here to insure continuous prompting until proper input
				keepSamePlayers = input("Keep same players? y/n\n")
				if keepSamePlayers not in ["y","n"]:
					print("Please enter 'y' if you would like to keep the same players,\nor 'n' if you would like to select new players or a new order\n")
				else:
					break
			break


#maybe select turn order?
#keep same players?
#add in AI - or figure out where it goes