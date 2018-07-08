from random import randint 
def printBoard(boardArray): #prints the current board
	i=1
	while i < 10:
		print(gameBoard[i]+' | '+gameBoard[i+1]+' | '+gameBoard[i+2])
		i+=3
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
		print(f"{turnOrder[(turnCounter)%2+1][0]} has won! :) \n")

def compTurn(playerMarker, boardArray):

	location = str(remainingPlaces[randint(0,len(remainingPlaces))])
	gameBoard[int(location)] = playerMarker
	if checkWin(boardArray): #check if winner and declare it
		printBoard(gameBoard)
		print(f"{turnOrder[(turnCounter)%2+1][0]} has won! :) \n")

def checkWin(b): #checks if there is a winner; b = boardarray (gameBoard)
	return((b[1]==b[2]) and (b[2]==b[3]) or #top
		(b[4]==b[5]) and (b[5]==b[6]) or #mid horizontal
		(b[7]==b[8]) and (b[8]==b[9]) or #bottom
		(b[1]==b[4]) and (b[4]==b[7]) or #left
		(b[2]==b[5]) and (b[5]==b[8]) or #mid vertical
		(b[3]==b[6]) and (b[6]==b[9]) or #right
		(b[1]==b[5]) and (b[5]==b[9]) or #diagonal from upper left
		(b[3]==b[5]) and (b[5]==b[7])) #diagonal from upper right

def playerOrder(player1,player2):
	firstPlayer = randint(1,2)
	if firstPlayer == 1:
		return({2:[player1,"X"],1:[player2,"O"]})
	else:
		return({2:[player2,"X"],1:[player1,"O"]})

#main game
print("Welcome to Tic-Tac-Toe!")

playAgain = ""
keepSamePlayers = ""

while playAgain != "n": #to loop in case players want another game

	while True:
		howManyPlayers = input("Please select whether you would like to play with 1 or 2 players\n")
		if howManyPlayers not in ["1","2"]:
			print("Please select 1 or 2")
		else:
			break




	if keepSamePlayers != "y": #select new players if that option has been selected after a game
		player1 = input("Please enter the name of player 1\n")
		player2 = input("Now, please enter the name of player 2\n")

	gameBoard = list(map(str,range(0,10))) #establish gameboard as range between 0-9 (start with 0 to make indexing easier)
											#convert to str to make printing possible
	turnCounter = 1

	turnOrder = playerOrder(player1,player2)

	print(f"\n{turnOrder[(turnCounter)%2+1][0]} goes first and plays as 'X'\n")

	while checkWin(gameBoard) == False: #keep turns going until there's a winner
		printBoard(gameBoard)
		remainingPlaces = [num for num in gameBoard if num != "X" and num != "O"]
		print(f"Turn #{turnCounter}")
		turnPlay(turnOrder[(turnCounter)%2+1][1],gameBoard)
		turnCounter +=1
		if turnCounter > 9: #account for a tie
			printBoard(gameBoard)
			print("It's a tie! Game over.")
			print("")
			break

		if howManyPlayers == "1":
			compTurn(turnOrder[(turnCounter)%2+1][1],gameBoard)
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

#to do:
#add functionality for 1 or 2 players
#create a function for computer turn - first random, then with some rules
