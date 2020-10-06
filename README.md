# Sudoku Solver

## What is Sudoku?

Sudoku is a logic-based number-placement puzzle game, where a player must fill a grid with the digits 1-9 in various patterns. In a well-formed game, the puzzle should only have one viable solution. This solution will always result in a <a href="https://en.wikipedia.org/wiki/Latin_square">Latin Square</a>.

### Sudoku Board

A sudoku board is typically a 9x9 grid that is broken up into 9 smaller grids subgrids, which can be called **sub-boards** (or **board** for short), **boxes**, or **regions**.

- Each row of the grid must contain each digit 1-9 *exactly* one time (that is, no numbers in each row can repeat, however numbers can repeat in successive rows)

- Each column of the grid must also contain each digit 1-9 *exactly* one time (that is, no numbers in each column can repeat)

- Each 3x3 square of the grid must contain each digit 1-9 *exactly* one time (that is, no numbers can repeat inside each 3x3 square of the grid)

Some digits on the board must be provided at the start of the puzzle (at least 17 of the 81 required to solve).

### Representing the Board

A standard sudoku board will feature 9 different regions, which can be referred to in the following way:

```
|----------------------------------|
|           |           |          |
|     1     |     2     |     3    |
|           |           |          |
|----------------------------------|
|           |           |          |
|     4     |     5     |     6    |
|           |           |          |
|----------------------------------|
|           |           |          |
|     7     |     8     |     9    |
|           |           |          |
|----------------------------------|
```

Each of these regions can then be broken down into a 3x3 board, which may look something like this:

```
 -------------
 | 1 | 2 | 3 |
 -------------
 | 4 | 5 | 6 |
 -------------
 | 7 | 8 | 9 |
 -------------
```

This representation allows for a pythonic representation of the board as a list of lists:

```
board = [
    [row 1],
    [row 2],
    [row 3],
    [row 4],
    [row 5],
    [row 6],
    [row 7],
    [row 8],
    [row 9],
]
```

Each row's list will contain the digits 1-9 when a digit has been placed, and a 0 for a digit that is still yet to be determined.

## Purpose of This Repository

This repository will serve as a way to centralize different solving algorithms. As a new algorithm is developed, they it will be explained, tested, and compared below.

## Requirements

The following packages will be required to run this repository:

## Author

This repository is created by <a href="https://github.com/rossdrucker">Ross Drucker</a>. If you have any questions, feel free to reach out <a href="mailto:ross.a.drucker@gmail.com">via email</a>.