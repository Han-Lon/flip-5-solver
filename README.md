# flip-5-solver
A Python3 solution for the ICPC Flip 5 challenge here -> https://www.hackerrank.com/contests/2014-icpc-north-america/challenges/flip-five/problem


This is a logic puzzle in which you have a square grid of 3×3 cells. Each cell is initially either white or black. When you click on a square it flips, or toggles, the color of that square and the colors of its four immediate north, south, east and west neighbors that exist (they don’t exist if they would be outside the grid).

The problem is to find the minimum number of cell clicks to transform a grid of all white cells into the input grid (which is always possible). You cannot rotate the grid

README.png

Input Format

The first value in the input file is an integer P (0 < P ≤ 50) on a line by itself giving the number of problems to solve.

For each of the P problems, 3 lines of 3 characters describe the input grid. The characters in the grid descriptions are ‘*’ (for black) and ‘.’ (for white).

Output Format

For each problem output a single integer giving the minimum number of clicks necessary to transform a grid of all white cells into the pattern given in the input.

Sample Input

2
*..
**.
*..
***
*..
..*

Sample Output

1
3

Explanation

Source: 2014 ICPC North America Qualifier