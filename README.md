# Tic-Tac-Toe Versus AI
This project contains the files for a Tic-Tac-Toe game I made that allows the user to play against the computer.
I completed this project for fun in my free time as a way for me to learn something new by applying my skills 
in a way that I had not done previously and for me to take a first step of sorts into the realm of AI.

![tictactoe_screenshot](https://github.com/shane-monaghan/TicTacToe-AI/assets/135287482/99de8bd8-e0f8-4d17-aafe-6693bcb6459e)
![tictactoe_end_screenshot](https://github.com/shane-monaghan/TicTacToe-AI/assets/135287482/c641c406-d058-4910-897a-48d757537091)

## How It's Made:

**Tech used:** Python, Pygame

For me, seeing as it was the reason I decided to make this project in the first place, the highlight of this project was implementing a minimax algorithm to find the best move for the opponent AI to play. I found implementing this algorithm to be a really fun challenge because all I really knew about it before I began coding was what it was supposed to do and that the algorithm involved a minimize function, a maximize function, and a function to evaluate the board.  
 
 Other than that, this project includes just about what you would expect of a Tic-Tac-Toe game (e.g., a function to check for three in a row, see if a move is allowed to be played, etc). The user interface for this game was made using Pygame, and I also used Pygame to detect user input which could come in the form of clicking where they want to place an 'X' or pressing 'R' to restart the game. 

 One thing I would add is that originally, I was not planning on making a UI for this project because my primary goal was just to make the opponent AI. I only decided to make the UI after I had already made the game work in the console. However, with some minor adjustments here and there, I was able to use almost all of the code that I already had from making the game in the console.

## What I Learned
Overall, I found that I learned a good deal from this project despite the fact that it may have been relatively simple. First, 
I had only ever worked with binary tree structures before for the most part, so having the opportunity to see and use a general tree 
structure was nice. 

To complete this project, specifically implementing the minimax algorithm, I also had to do some research into game theory 
and AI. I found learning about those things to be extremely interesting. 

Finally, this project taught me a lot about adapting and the importance of planning. 
As I mentioned earlier, my original plan for this project was to simply make a tic-tac-toe game against an AI that the user could play in the console, so that
was exactly what I did. After showing the project to a friend, however, they suggested that I create a user interface. Seeing as this
was not something that I was originally planning to do, there was some code that needed to be adjusted to fit this new addition.
This proved to be a valuable learning experience and allowed me to work on my adaptability. Despite this being a valuable experience, I probably could have completed this project in a more efficient manner if I had known what I wanted the final version of it to look like from the very beginning as opposed to deciding last minute to add new features; this is definitely something that will stick with me for future projects. In the end, though, I'm very glad that I did end up adding a user interface element to the project because it provided me with an opportunity to learn more about how to adjust existing code and to practice using Pygame which was something I had already been wanting to do more with.

## What's Next?
For future projects, I think it would be really cool to start looking into a game like chess which is significantly more complicated than tic-tac-toe. Based on what I've read, this would require the use of alpha-beta pruning which, from what I can tell, is an improved version of the minimax algorithm I implemented in this project making a chess project a logical next step.  

Another thing I think would be interesting is to redo this project but in a way that would scale. Currently, my version of the game is on a 9x9 board, and the code is not designed to work with anything else. But what if I let the user pick a board size? What if I allowed multiple players or AIs? I think that this would be a really fun way to take what I learned from this project and use it to make an improved version of it.  





