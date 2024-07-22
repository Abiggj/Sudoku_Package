# Sudoku Game Application

## Overview

The Sudoku Game Application is a graphical user interface (GUI) application built with PyQt5 for playing and solving Sudoku puzzles. The application features an intuitive interface with three main functionalities: playing the game, solving puzzles, and accessing help resources.

## Features

- **Play Sudoku**: Users can start a new Sudoku game with puzzles randomly selected from a set of predefined CSV files.
- **Solve Sudoku**: Provides a Sudoku solver that automatically solves puzzles.
- **Help Section**: Offers a help window with instructions and resources to assist users.

## Installation

To run the application, ensure you have PyQt5 installed. You can install it via pip:

```bash
pip install PyQt5
```

Make sure to place your puzzle CSV files in the same directory as the main script.

## Workflow

1. **Launch Application**: Run the main script to start the application. The main window will appear with options to play, solve, or get help.

2. **Play Sudoku**:
   - Click the "Play!!" button to start a new game.
   - A random Sudoku puzzle is loaded from one of the predefined CSV files.
   - The game window will open, displaying the puzzle for the user to solve.

3. **Solve Sudoku**:
   - Click the "Solver" button to access the Sudoku solver.
   - The solver window will open, allowing users to input a Sudoku puzzle to be solved automatically.

4. **Help Section**:
   - Click the "Help" button to access the help window.
   - The help window provides instructions and resources to assist users with the application and Sudoku gameplay.

## Components

- **Main Window**: The primary interface from which users can navigate to different functionalities.
- **Play Window**: Displays the Sudoku puzzle and allows users to interact with it.
- **Solver Window**: Provides tools and features for solving Sudoku puzzles.
- **Help Window**: Contains instructions and resources for user assistance.


## FAQ

### 1. What is the purpose of this application?

The Sudoku Game Application is designed to provide users with a platform to play and solve Sudoku puzzles. It offers an easy-to-use interface for both casual and serious Sudoku enthusiasts.

### 2. How do I install the application?

Ensure you have Python and PyQt5 installed. You can install PyQt5 using pip:
```bash
pip install PyQt5
```
Then, run the main script to start the application.

### 3. Where can I find the Sudoku puzzles?

The puzzles are stored in CSV files named `Puzzles_1.csv` to `Puzzles_11.csv` in the same directory as the main script. Each file contains multiple puzzles from which the application randomly selects one for the game.

### 4. How do I start a new game?

To start a new game, open the application and click on the "Play!!" button. A random puzzle will be loaded from the predefined CSV files, and you can begin solving it.

### 5. How do I use the Sudoku solver?

To use the solver, click on the "Solver" button. This will open the solver window where you can input a Sudoku puzzle, and the application will solve it for you automatically.

### 6. What should I do if I need help with the application?

Click on the "Help" button to access the help window. This window provides instructions and resources to assist you with using the application and solving Sudoku puzzles.

### 7. How do I exit the game or solver?

If you need to exit the game or solver window, simply close the window. If you were in the middle of a game, a prompt will appear asking if you really want to quit.

### 8. Can I contribute to this project?

Yes, contributions are welcome! Feel free to submit issues or pull requests on the project's GitHub repository.


