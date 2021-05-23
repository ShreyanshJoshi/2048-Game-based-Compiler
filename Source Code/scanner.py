'''SLY is library for writing parsers and compilers. It is loosely based on the traditional compiler construction tools lex and yacc and 
implements the same LALR(1) parsing algorithm. Most of the features available in lex and yacc are also available in SLY.  

SLY provides two separate classes Lexer and Parser. The Lexer class is used to break input text into a collection of tokens specified 
by a collection of regular expression rules. '''

import sys
sys.path.insert(0, '../..')
 
from sly import Lexer

 
class game_lexer (Lexer):

    # Lexers must specify a tokens set that defines all of the possible token type names that can be produced by the lexer. This is always 
    # required and is used to perform a variety of validation checks. Token names should be specified using all-caps.

    tokens={LEFT, RIGHT, UP, DOWN, ADD, SUBTRACT, MULTIPLY, DIVIDE,  ASSIGN, VAR, 
            NAME, IS, TO, IN, VALUE, FULL, COMMA, NUMBER}
 
    ignore=' \t'
 
    # Tokens are specified by writing a regular expression rule compatible with the re module. The name of each rule must match one of the names of the tokens provided in the tokens set. Tokens are matched in the same order that patterns are listed in the Lexer class.

    FULL=r'\.'
    COMMA=r'\,'

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    NAME["ADD"] = ADD
    NAME["SUBTRACT"] = SUBTRACT
    NAME["MULTIPLY"] = MULTIPLY
    NAME["DIVIDE"] = DIVIDE

    NAME["LEFT"] = LEFT
    NAME["RIGHT"] = RIGHT
    NAME["UP"] = UP
    NAME["DOWN"] = DOWN

    NAME["ASSIGN"] = ASSIGN
    NAME["TO"] = TO
    NAME["IS"] = IS
    NAME["IN"] = IN
    NAME["VAR"] = VAR
    NAME["ASSIGN"] = ASSIGN
    NAME["VALUE"] = VALUE

    NUMBER=r'[+-]?[0-9]+'
    
    # Error handling - If a bad character is encountered while lexing, tokenizing will stop. However, you can add an error() method to handle lexing errors that occur when illegal characters are detected. If the error() method also returns the passed token, it will show up as an ERROR token in the resulting token stream. This might be useful if the parser wants to see error tokens for some reason–perhaps for the purposes of improved error messages or some other kind of error handling.
    # This is precisely what I have done.

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1
        return t        
 
 
 


