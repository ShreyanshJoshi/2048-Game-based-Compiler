import random
import sys

def var_name (names, var, x, y):            # Assigns variables to a particular cell
    x-=1
    y-=1

    if x<0 or y<0 or x>3 or y>3:
        return "ERROR1"

    names[x][y].append(var)
    return "named"


def assign (a, names, value, x, y):         # Assigns a value to a particular cell
    x-=1
    y-=1

    if (x<0 or y<0 or x>3 or y>3) and value<0:
        return "ERROR3"

    if x<0 or y<0 or x>3 or y>3:
        return "ERROR1"
    
    if value<0:
        return "ERROR2"

    if value==0:
        names[x][y].clear()
        a[x][y] = -1
        return "assigned"

    a[x][y] = value
    return "assigned"


def get_value (a, x, y):                    # Retrieves value from a particular cell
    x-=1
    y-=1

    if x<0 or y<0 or x>3 or y>3:
        return "ERROR1"

    if a[x][y]==-1:
        print("The value stored at corresponding position is ",0, "\n")
    
    else:
        print("The value stored at corresponding position is ", a[x][y], "\n")

    return "blank"


def get_loc (a):                        # Helper function that returns an empty location in the matrix
    v = []
    for i in range(4):
        for j in range(4):
            if a[i][j]==-1:
                v.append(4*i+j)
    
    if len(v)==0:
        return [-1,-1]
    
    temp = random.randint(0,1000)
    temp = temp % len(v)
    row = int(v[temp]/4)
    col = v[temp] % 4

    return [row,col]


def assign_random_number (a):           # Assigns one of 2 or 4 to an empty cell
    random1 = random.randint(0,1000)
    [row, col] = get_loc(a)

    if row==-1 and col==-1:					
        return False

    if(random1 % 2 ==0): 						
        a[row][col] = 2
    
    else: 								 	
        a[row][col] = 4

    return True


def initialize_game (a):                # Initialize the board with 2 cells - either 2 or 4.
    assign_random_number(a)
    assign_random_number(a)
    return True


def move_up (a, names, operation):      # Move up (performing one of add, subtract, multiply or divide based on operation)
    for j in range(4):
        i=0
        while i<3:
            if a[i][j]==-1:
                i+=1
                continue
            
            k = i+1
            while k<=2 and a[k][j]==-1:
                k+=1
            
            if(a[k][j]==a[i][j]):
                if(operation==1): 
                    a[i][j] = 2*a[k][j]
                    a[k][j] = -1
            
                elif(operation==2): 
                    a[i][j] = -1
                    a[k][j] = -1
                
                elif(operation==3): 
                    a[i][j] = a[k][j]*a[k][j]
                    a[k][j] = -1
                
                elif(operation==4): 
                    a[i][j] = 1
                    a[k][j] = -1
                
                for z in range(len(names[k][j])):
                    names[i][j].append(names[k][j][z])
                
                names[k][j].clear()

                i = k+1
            
            else:
                i = k
        
        for v in range(4):                  # ADDED NOW
            for w in range(4):
                if a[v][w]==-1:
                    names[v][w].clear()

        for m in range(4):
            if(a[m][j]==-1):
                continue
            
            k = m-1
            while(k>=0 and a[k][j]==-1): 
                k-=1
            
            if(k!=m-1):                               
                a[k+1][j] = a[m][j]
                a[m][j] = -1

                for z in range(len(names[m][j])):
                    names[k+1][j].append(names[m][j][z])
                
                names[m][j].clear()
    
    for i in range(4):
        for j in range(4):
            if a[i][j]==-1:
                names[i][j].clear()

    return True


def move_left (a, names, operation):        # Move left (performing one of add, subtract, multiply or divide based on operation)
    for i in range(4):
        j=0
        while j<3:
            if a[i][j]==-1:
                j+=1
                continue
        
            k=j+1
            while(k<=2 and a[i][k]==-1):
                k+=1
            
            if(a[i][k]==a[i][j]): 
                if(operation==1): 
                    a[i][j] = 2*a[i][k]
                    a[i][k] = -1
                
                elif(operation==2): 
                    a[i][j] = -1
                    a[i][k]= -1
                
                elif(operation==3): 
                    a[i][j] = a[i][k]*a[i][k]
                    a[i][k]= -1
                
                elif(operation==4): 
                    a[i][j] = 1
                    a[i][k] = -1
                
                for z in range(len(names[i][k])):
                    names[i][j].append(names[i][k][z])
                
                names[i][k].clear()

                j = k+1
            
            else:
                j = k

        for v in range(4):                  # ADDED NOW
            for w in range(4):
                if a[v][w]==-1:
                    names[v][w].clear()

        for m in range(4):
            if(a[i][m]==-1):
                continue

            k = m-1
            while(k>=0 and a[i][k]==-1):
                k-=1

            if(k!=m-1):                            
                a[i][k+1] = a[i][m]
                a[i][m] = -1
                
                for z in range(len(names[i][m])):
                    names[i][k+1].append(names[i][m][z])
                
                names[i][m].clear()
        
    for i in range(4):
        for j in range(4):
            if a[i][j]==-1:
                names[i][j].clear()

    return True


def move_down (a, names, operation):            # Move down (performing one of add, subtract, multiply or divide based on operation)
    for j in range(4):
        i = 3
        while i>=1:
            if(a[i][j]==-1): 
                i-=1
                continue
            
            k = i-1
            while(k>=1 and a[k][j]==-1):
                k-=1

            if(a[k][j]==a[i][j]): 
                if(operation==1): 
                    a[i][j] = 2*a[k][j]
                    a[k][j] = -1
                
                elif(operation==2): 
                    a[i][j] = -1
                    a[k][j] = -1
                
                elif(operation==3): 
                    a[i][j] = a[k][j]*a[k][j]
                    a[k][j] = -1
                
                elif(operation==4): 
                    a[i][j] = 1
                    a[k][j] = -1
                
                for z in range(len(names[k][j])):
                    names[i][j].append(names[k][j][z])
                
                names[k][j].clear()

                i = k-1
            
            else:
                i = k
        
        for v in range(4):                  # ADDED NOW
            for w in range(4):
                if a[v][w]==-1:
                    names[v][w].clear()

        m = 2
        while m>=0:
            if(a[m][j]==-1):
                m-=1
                continue

            k = m+1
            while(k<4 and a[k][j]==-1): 
                k+=1
            
            if(k!=m+1):								 
                a[k-1][j] = a[m][j]
                a[m][j] = -1
                
                for z in range(len(names[m][j])):
                    names[k-1][j].append(names[m][j][z])
                
                names[m][j].clear()
            
            m-=1
    
    for i in range(4):
        for j in range(4):
            if a[i][j]==-1:
                names[i][j].clear()

    return True


def move_right (a, names, operation):           # Move right (performing one of add, subtract, multiply or divide based on operation)
    for i in range(4):
        j = 3
        while(j>=1): 								
            if(a[i][j]==-1): 
                j-=1
                continue
            
            k = j-1
            while(k>=1 and a[i][k]==-1): 
                k-=1
            
            if(a[i][k]==a[i][j]): 
                if(operation==1): 
                    a[i][j] = 2*a[i][k]
                    a[i][k] = -1
                
                elif(operation==2): 
                    a[i][j] = -1
                    a[i][k] = -1
                
                elif(operation==3): 
                    a[i][j] = a[i][k]*a[i][k]
                    a[i][k] = -1
                
                elif(operation==4): 
                    a[i][j] = 1
                    a[i][k] = -1
                
                for z in range(len(names[i][k])):
                    names[i][j].append(names[i][k][z])
                
                names[i][k].clear()

                j = k-1
            
            else:
                j = k

        for v in range(4):                  # ADDED NOW
            for w in range(4):
                if a[v][w]==-1:
                    names[v][w].clear()

        m = 2
        while m>=0:
            if(a[i][m]==-1):
                m-=1
                continue

            k = m+1
            while(k<4 and a[i][k]==-1):
                k+=1

            if(k!=m+1): 								
                a[i][k-1] = a[i][m]
                a[i][m] = -1

                for z in range(len(names[i][m])):
                    names[i][k-1].append(names[i][m][z])
                
                names[i][m].clear()
            
            m-=1
    
    for i in range(4):
        for j in range(4):
            if a[i][j]==-1:
                names[i][j].clear()

    return True


def display_board (a):                  # Displays the 4x4 board to the player on the screen
    for i in range(4):
        for j in range(4):
            if a[i][j]!=-1:
                if a[i][j]<10:
                    print("000", end="")
                    print(a[i][j], "    ", end="")
                
                elif a[i][j]<100:
                    print("00", end="")
                    print(a[i][j], "    ", end="")

                elif a[i][j]<1000:
                    print("0", end="")
                    print(a[i][j], "    ", end="")

                else:
                    print(a[i][j], end=" ")
                    print("    ", end="")

            else:
                print("****     ", end="")

        print('')
    print('')


def number_of_names (names):            # Helper function that returns number of cells having a variable assigned
    count = 0

    for i in range(4):
        for j in range(4):
            if len(names[i][j])>0:
                count+=1
    
    return count


def print_stderr (a, names):            # Prints on stderr - as required by the assignment

    for i in range(4):
        for j in range(4):
            if a[i][j]==-1:
                print(0, end=" ", file=sys.stderr)
            else:
                print(a[i][j], end=" ", file=sys.stderr)
    
    xxx = number_of_names(names)
    if xxx==0:
        print('', file=sys.stderr)
    
    count = 0
    
    for i in range(4):
        for j in range(4):
            if len(names[i][j])>0:
                
                count+=1
                print(i+1,end='',file=sys.stderr)
                print(",",end='',file=sys.stderr)
                print(j+1,end='',file=sys.stderr)

                for k in range(len(names[i][j])):

                    if k!=len(names[i][j])-1:
                        print(names[i][j][k],end='',file=sys.stderr)
                        print(",",end='',file=sys.stderr)
                    
                    else:
                        if count==xxx:
                            print(names[i][j][k], file=sys.stderr)
                        
                        else:
                            print(names[i][j][k], end=" ", file=sys.stderr)
    
                