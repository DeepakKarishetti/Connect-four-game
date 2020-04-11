## Connect-four game


**Name and CSM ID of the student**

	Name: Deepak Rajasekhar Karishetti
	CWID: 


**What programming language and what version of the compiler are used**

	Programming language used: Python
	Interpreter: Linux terminal
	Operating system: Linux - Ubuntu 16.04 LTS


**How the code is structured**

	-Code for the structure of the game derived from the sample code provided in the project description.

	-The project consists of two python files which consists the basic structure of the game and the other performing
	the required action like one-move mode or interactive mode in the game.

	-connect4game.py contains all the game functions all defined under a class and main.py contains code to execute
	the game in the desired modes.

	-The game is implemented with:
		-Plain minimax algorithm.
		-Alpha-beta pruning in search.
		-Depth-limited version of minimax.
		-Alpha-beta pruning with successor node prioritization.

	The evaluation function is derived from the resource pdf provided in the project description.


**How to run the code**

	>>Terminal opened at the file path.

	-Interactive mode:
	$ python main.py interactive input2.txt computer-next/human-next depth
		
		This interactive mode is played between human and the computer, where the computer will predict its move based on the algorithms implemented and gives us the result of the score and winner of the game.


	-One-move mode:
	$ python main.py one-move input2.txt computer-next/human-next depth

		This one-move mode will predicts and plays according to the depth given and gives the board state of the next move based on the current game state given as input.

	
	-Code structured in jupyter notebook and then edited using vimand run on Linux terminal.

To run on WINDOWS:

	>> Open a terminal and navigate to the folder path containing all the files enclosed along.

	-Interactive mode:
	main.py interactive input2.txt computer-next/human-next depth

	-One-move mode:
	main.py one-move input2.txt computer-next/human-next depth



	>> arg[1] = choosing the game mode, one-move mode or interactive mode.
	>> arg[2] = choosing the input file containing the gameboard state, from the current folder.
	>> arg[3] = choosing the next player from the current state, either the computer or human player.
	>> arg[4] = choosing the depth at which you want the search to be done by the computer.

	->>Example implementaion:

	>main.py one-move input2.txt computer-next 7
