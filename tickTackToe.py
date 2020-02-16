import numpy as np
import random

gameBoard = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])

vicCheckRow = np.array([1, 1, 1])
vicCheckColumn = np.array([[1],
						   [1],
						   [1]])

print("Hello, welcome to my tick tack toe game. \n\nMade by Byron.C\n\n")

row = 0
column = 0

def playerVicCheck():

	#This code checks to see if the player has won.
	if np.all(gameBoard[row] == vicCheckRow) | np.all(gameBoard[column] == vicCheckColumn):
		print("You Win! \nCongraturations")
	else:
		row = row + 1
		column = column +1

gameLoop = True
while gameLoop:

	POSCheck = 0

	#This code asks the player for their position values.
	posY = int(input("Input your Y (column) position \n:"))
	posX = int(input("Input your X (row) position \n:"))

	while POSCheck != 2:
		#This loop checks if the player's Y value is too large.
		if posY >= 3:
			posY = int(input("Your value for Y is too large, choose between 0 and 2.\n:"))
		else:
			POSCheck = POSCheck + 1

		#This loop checks if the player's X value is too large.
		if posX >= 3:
			posX = int(input("Your value for X is too large, choose between 0 and 2.\n:"))
		else:
			POSCheck = POSCheck + 1

	playerVicCheck()

	gameBoard[posY, posX] = 1

	#Generate random a random position for the enemy "AI"
	enemyPOSy = random.randint(0, 2)
	enemyPOSx = random.randint(0, 2)
	gameBoard[enemyPOSy, enemyPOSx] = 2
