''' The Parser class is used to parse language syntax. When writing a parser, syntax is usually specified in terms of a BNF grammar.
The semantics of what happens during parsing is often specified using a technique known as "syntax directed translation". '''

from sly import Lexer, Parser
from scanner import game_lexer
import functions

names = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]

a = [[-1 for j in range(4)] for i in range(4)]
functions.initialize_game(a)

def do_it ():
    print('2048 > Hi, I am the 2048-game Engine.\n')
    print('The start state is: ')
    functions.display_board(a)


class game_parser(Parser):

    tokens = game_lexer.tokens      # Get the token list from the lexer (required)

    def error (self, p):
        if p==None:
            print("You need to end a command with a full-stop.")

        elif p.type=="ERROR":
            print("Lexing error has occurred.")
        
        else:
            print("A parsing error has been encountered.")

        return None
    
    
    # Adding matching actions - When certain tokens are matched, you may want to trigger some kind of action that performs extra processing. 
    # One way to do this is to write your action as a method and give the associated regular expression using the @_() decorator. As an argument, the method receives a sequence of grammar symbol values in p. There are two ways to access these symbols. First, you can use symbol names - 

    ''' @_('expr PLUS term')
        def expr(self, p):
            return p.expr + p.term '''

    # Alternatively, you can also index p like an array:

    ''' @_('expr PLUS term')
        def expr(self, p):
            return p[0] + p[2] '''

    # Note: If a grammar rule includes the same symbol name more than once, you need to append a numeric suffix to disambiguate the symbol name when you’re accessing values:

    ''' @_('expr PLUS expr')
        def expr(self, p):
            return p.expr0 + p.expr1 '''



    @_('ADD LEFT FULL')
    def expr(self,p):
        return [functions.move_left(a,names,1),a,names]
 
    @_('ADD RIGHT FULL')
    def expr(self,p):
        return [functions.move_right(a,names,1),a,names]
 
    @_('ADD UP FULL')
    def expr(self,p):
        return [functions.move_up(a,names,1),a,names]
 
    @_('ADD DOWN FULL')
    def expr(self,p):
        return [functions.move_down(a,names,1),a,names]
 
    @_('SUBTRACT LEFT FULL')
    def expr(self,p):
        return [functions.move_left(a,names,2),a,names]
 
    @_('SUBTRACT RIGHT FULL')
    def expr(self,p):
        return [functions.move_right(a,names,2),a,names]
 
    @_('SUBTRACT UP FULL')
    def expr(self,p):
        return [functions.move_up(a,names,2),a,names]
 
    @_('SUBTRACT DOWN FULL')
    def expr(self,p):
        return [functions.move_down(a,names,2),a,names]
 
    @_('MULTIPLY LEFT FULL')
    def expr(self,p):
        return [functions.move_left(a,names,3),a,names]
 
    @_('MULTIPLY RIGHT FULL')
    def expr(self,p):
        return [functions.move_right(a,names,3),a,names]
 
    @_('MULTIPLY UP FULL')
    def expr(self,p):
        return [functions.move_up(a,names,3),a,names]
 
    @_('MULTIPLY DOWN FULL')
    def expr(self,p):
        return [functions.move_down(a,names,3),a,names]
 
    @_('DIVIDE LEFT FULL')
    def expr(self,p):
        return [functions.move_left(a,names,4),a,names]
 
    @_('DIVIDE RIGHT FULL')
    def expr(self,p):
        return [functions.move_right(a,names,4),a,names]
 
    @_('DIVIDE UP FULL')
    def expr(self,p):
        return [functions.move_up(a,names,4),a,names]
 
    @_('DIVIDE DOWN FULL')
    def expr(self,p):
        return [functions.move_down(a,names,4),a,names]
 
    @_('VALUE IN NUMBER COMMA NUMBER FULL')
    def expr(self,p):
        return [functions.get_value (a, int(p.NUMBER0), int(p.NUMBER1)),a,names]
 
    @_('VAR NAME IS NUMBER COMMA NUMBER FULL')
    def expr(self,p):
        return [functions.var_name (names, p.NAME, int(p.NUMBER0), int(p.NUMBER1)),a,names]
    
    @_('ASSIGN NUMBER TO NUMBER COMMA NUMBER FULL')
    def expr(self,p):
        return [functions.assign (a, names, int(p.NUMBER0), int(p.NUMBER1), int(p.NUMBER2)),a,names]

    