# Color-Plosion-Project
Candy Crush backend code simulator

Color Plosion runs in the consule.
When the game runs, a 6 x 6 2d list (board) with random elements from 0 - 5 is generated.
The numbers represent different colours.
The board has at least one possible match of three same elements.
It does not have any existing match of three or more.
It prompts the user for the direction to move, either x or y.
If the direction is x, it asks the user for the row to make move in.
It then asks for the initial and final indices of adjacent elements.
If the direction is y, it asks the user for the column to make move in.
It then asks for the initial and final indices of adjacent elements.
The game then switches elements based upon the directions given by the user.
The game checks for ajacent three numbers.
If match is made, the user is awarded 50 points.
The match made is replaced by elements in the above rows.
If it is the first row, new numbers are randomly generated.
More than 50 points may be awarded if the replacing elements create a new match of three.
If no match is made, the switch is reversed.
The user is informed that the move is invalid.
The game then provides the user with a hint element to move.
The game ends when the score of the user reaches 500.
