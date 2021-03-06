COMP 3981 Abalone Project

Group 1: Haejoon Choi, Tommy Chien, Grace Bu, Geoffrey Browning


----- Abalone Game GUI -----
	- About: Displays the game itself. Includes the game board, starting page and configurations page. The main page also includes the display of players' stats, suggested next move generated by AI, and next move input for human player.

	- To Run: Run main.py, on the game menu, click [Config] for changing configuration of the game. Click [Start] button to have the game board and marbles generated.
	- For Computer vs. Computer game, the direction buttons are changed to "switch agent" button. You can run each agent by clicking the button repeatedly.
	- For Computer vs. Human game, the agent will generate the next best move and show it on the "Suggested Move" text box. You can still play it by yourself, or click the "Apply" button to apply the suggested move to the game. 


----- State Space Generator -----
	- About: This generator intakes a given state of the board (Test<#>.input) and the which players' turn to move and uses that data to generate all the possible legal moves on the board for that player and their resulting board state.

	- To Run: Run the main() inside the StateSpaceGenerator (state_space_generator.py) and you will be prompted to
	enter the Test<#>.input file name in console without the extension. The moves taken and their resulting board state
	will be outputted into Test<#>.move and Test<#>.board.


----- Game-Playing Agent -----
    - About: This game-playing agent intakes an input list that contains which player's it is (either 'b' or 'w') and the current board state. It uses the current board state to generate a tree of all possible resulting board states. From those board states the agent further extends the tree by generating the opponent's responses. The current tree searches a depth of 2. The heuristic evaluation function is then applied to these board states to assign a score. We use minimax by max of opponent's scores and then by min of those to select the agent's next best move. A quiescent search is applied when there's a move that pushes the opponent's marbles off the board and searches for the next nonquiescent position and its score.

    - To Run the Game-Playing Agent on it's own: Run the main() inside the GamePlayingAgent class (game_playing_agent.py) and the agent will play against another agent. Each player's responses will be outputted as move notations.
    - To Run the Game-Playing Agent in the Abalone GUI: when Black Player is selected as the Computer the agent will start the game by playing a random legal move.


----- Evaluation Function -----
    - There are four evaluation functions written by each team member. 
    - You can run the main function of each file to see what value it gives for example board setup.


To Be Implemented:
    - Adding a feature of choosing different evaluation function / agent for the game.
    - Adding some graphical representation of "just changed" marble positions.
    - Adding sound effect for marble move, score, win / loss of the game. 
