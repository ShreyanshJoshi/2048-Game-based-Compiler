import sys
sys.path.insert(0, '../..')
from sly import Lexer, Parser
import functions, parser
from scanner import game_lexer
from parser import game_parser


if __name__ == '__main__':

    parser.do_it()
    lexer = game_lexer()
    parser = game_parser()

    while True:
        try:
            text = input('2048 > ')

        except EOFError:
            break

        if text:
            x = parser.parse(lexer.tokenize(text))
        
            if x==None:                             # Parser or lexer error
                print(-1, file=sys.stderr)
                continue
            
            var = x[0]
            a = x[1]
            names = x[2]

            if var=="ERROR1":
                print("There is no tile like that. The tile co-ordinates must be in the range 1,2,3,4.")
                print(-1, file=sys.stderr)
                continue 
            
            elif var=="ERROR2":
                print("Cannot assign a negative value to a tile.")
                print(-1, file=sys.stderr)
                continue
                
            elif var=="ERROR3":
                print("Cannot assign a negative value to a tile and the tile co-ordinates must be in the range 1,2,3,4.")
                print(-1, file=sys.stderr)
                continue
            
            elif var=="blank":                          # No change in matrix state.
                continue

            elif var=="named":
                functions.print_stderr(a,names)
                print('')
                continue

            elif var=="assigned":
                functions.display_board(a)
                functions.print_stderr(a,names)
                print('')
                continue
                

            functions.assign_random_number(a)
            functions.display_board(a)

            functions.print_stderr(a,names)
            print('')
 