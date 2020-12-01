### tic-tac-toe-minimax
#### An implementation of Minimax AI Algorithm on Tic-Tac-Toe game.

#### Introduction
To solve games using AI, we will introduce the concept of a game tree followed by minimax algorithm. The different states of the game are represented by nodes in the game tree, very similar to the above planning problems. The idea is just slightly different. In the game tree, the nodes are arranged in levels that correspond to each player's turns in the game so that the “root” node of the tree (usually depicted at the top of the diagram) is the beginning position in the game. In tic-tac-toe, this would be the empty grid with no Xs or Os played yet. Under root, on the second level, there are the possible states that can result from the first player’s moves, be it X or O. We call these nodes the “children” of the root node.

Each node on the second level, would further have as its children nodes the states that can be reached from it by the opposing player's moves. This is continued, level by level, until reaching states where the game is over. In tic-tac-toe, this means that either one of the players gets a line of three and wins, or the board is full and the game ends in a tie.

#### What is Minimax?
Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.

#### How does it works?
The algorithm search, recursively, the best move that leads the Max player to win or not lose (draw). It consider the current state of the game and the available moves at that state, then for each valid move it plays (alternating min and max) until it finds a terminal state (win, draw or lose).

#### Understanding the Algorithm
The algorithm in python:

A simple Python3 program to find maximum score that maximizing player can get 
import math 
  
def minimax (curDepth, nodeIndex, 
             maxTurn, scores,  
             targetDepth): 
  
    # base case : targetDepth reached 
    if (curDepth == targetDepth):  
        return scores[nodeIndex] 
      
    if (maxTurn): 
        return max(minimax(curDepth + 1, nodeIndex * 2,  
                    False, scores, targetDepth),  
                   minimax(curDepth + 1, nodeIndex * 2 + 1,  
                    False, scores, targetDepth)) 
      
    else: 
        return min(minimax(curDepth + 1, nodeIndex * 2,  
                     True, scores, targetDepth),  
                   minimax(curDepth + 1, nodeIndex * 2 + 1,  
                     True, scores, targetDepth)) 
