### UW-Madison CS540 Fall 2022 HW8 A* on the 7-tile Puzzle

#### Assginment Goal: Solve 7-tile puzzle

The goal state of the puzzle is [1, 2, 3, 4, 5, 6, 7, 0, 0], or visually:

<img width="193" alt="Screenshot 2022-12-10 at 9 11 26 PM" src="https://user-images.githubusercontent.com/90480106/206884521-c76c6c1a-30be-4564-87f5-94331f8da71d.png">

#### Assignment Summary:

This assignment is about solving a variant of the 8-tile puzzle. The 8-tile puzzle was invented and popularized by Noyes Palmer Chapman in the 1870s. The version we will consider in this homework is played on a 3x3 grid with 7 tiles labeled 1 through 7 and two empty grids. The goal is to rearrange the tiles so that they are in order and the empty places are at the bottom right.

You solve the puzzle by moving the tiles around. For each step, you can only move one (not more!) of the neighbor tiles (left, right, top, bottom but not diagonally) into an empty grid. And all tiles must stay in the 3x3 grid (so no wrap around allowed). An example is shown in the picture below. Suppose we start from the following configuration:

<img width="222" alt="Screenshot 2022-12-10 at 9 12 19 PM" src="https://user-images.githubusercontent.com/90480106/206884546-462d2ac0-c604-49c8-b86c-bde5820b3f40.png">

Then, moving one tile can result in one of the following:

<img width="627" alt="Screenshot 2022-12-10 at 9 12 34 PM" src="https://user-images.githubusercontent.com/90480106/206884552-297f189d-87b1-479b-bcb5-86a9eefa4e0c.png">

That is, in the above example, we would either move 3 or 6 down or move 7 to the right. Given these rules for the puzzle, you will generate a state space and solve this puzzle using the A* search algorithm.
