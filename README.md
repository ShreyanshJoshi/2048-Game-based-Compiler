# 2048-Game-based-Compiler
This repository contains my code in Python for a project that was done in partial fulfillment of the course **CS F363 - Compiler Construction at BITS Pilani** for the year 2020-21. This project fetched me 70/70 in the assignment.

The task was to design a mini-compiler (scanner, parser and an interpreter) in Python for a game programming language. Since the project has been implemented in Python, SLY library has been used (which is the standard library for writing parsers and compilers in python). SLY is a 100% python implementation of the Lex and Yacc tools commonly used to write parsers and compilers in C, C++. Parsing is based on the same LALR(1) algorithm used by many Yacc tools. SLY requires the use of python 3.6 or greater. Older versions of python are not supported.

The game is a 2048-game 'family' - all features of 2048 are there plus some additional features and operations as well. More details about this are discussed in *Assignment_specs.pdf*. Being a compiler assignment, the game was completely text based, meaning that instead of pressing arrow keys, player instead had to enter commands following a particular language. For e.g - ADD LEFT.

### Additional Improvements -
This repository here is a slightly tweaked version of what I had actually submitted. I have made some changes in the code structure, to provide a better user experience.
1. Firstly, I have **modularized** the code. This means that each functionality (scanner, parser, interpreter) has been implemented in a seperate file. This allows for easier debugging, readability and reusability of code. Moreover, in case some code has to be changed in one part of the code, other files need not be changed. That's the power modularity gives.

2. I have also tried to improve the error handling in the code. Now, the program returns much more specific errors to the user in case a grammatically incorrect sentence is typed as a command. This provides a much more realistic gaming experience to the user.

### Files uploaded in repository - 
* *functions.py* - Contains the implementation of all functions necessary to perform the required operations in this modified 2048 game.
* *scanner.py* - Contains the Lexer class - used to break input text into a collection of tokens specified by a collection of regular expression rules.
* *parser.py* - Contains the Parser class - used to parse language syntax.
* *interpreter.py* - Links the scanner and parser together. It contains the main function and is the driver for the program (calls required functions present in other files).

### How to play the game on your machine -
To run the game locally, clone the repository and download the source files. Store them in a designated directory (folder) on your local machine. To execute the program and start playing, run the following commands sequentially - `python3 functions.py`, `python3 scanner.py`, `python3 parser.py`, `python3 interpreter.py`. Upon executing the last command, the game begins. To stop the execution of the program, press Ctrl + D.
