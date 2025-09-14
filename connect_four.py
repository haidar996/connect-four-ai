"""
Tic Tac Toe Player
created by Haidar Saad
"""

import math

X = "X"
O = "O"
EMPTY = None
index_l=[]
index_l=[4,4,4,4,4,4]
copy_index=[4,4,4,4,4,4]
def initial_state():
    
    return [[EMPTY, EMPTY, EMPTY,EMPTY,EMPTY],
            [EMPTY, EMPTY, EMPTY,EMPTY,EMPTY],
            [EMPTY, EMPTY, EMPTY,EMPTY,EMPTY],[EMPTY, EMPTY, EMPTY,EMPTY,EMPTY],[EMPTY, EMPTY, EMPTY,EMPTY,EMPTY],[EMPTY, EMPTY, EMPTY,EMPTY,EMPTY]]


def is_start(board):
    empty=True
    for i in range(6):
        for j in range(5):
            if board[i][j]!=None:
                empty=False
            if empty==False:
                break  
        if empty==False:
                break 
    return empty         

def count_forx(board):
    count=0
    for i in range(6):
        for j in range(5):
            if board[i][j]==X :
                count=count+1
    return count     
def count_foro(board):
    count=0
    for i in range(6):
        for j in range(5):
            if board[i][j]==O :
                count=count+1
    return count        






def player(board):
    empty=is_start(board)
    end=terminal(board)
    if empty==True:
        return X
    elif end==True:
       return 'the game is already over'
    else:
        num_x=count_forx(board)
        num_o=count_foro(board)
        if num_x>num_o:
            return O
        else:
            return X
        

    


  
    raise NotImplementedError


def actions(index_l):
    possible_actions = []
    for i in range(6):
        index = index_l[i]
        if index >= 0:
            action = (i, index)
            possible_actions.append(action)
    return possible_actions
              

    
    raise NotImplementedError


def result(board, action, index_l):
    new_board = [row[:] for row in board]
    new_index_l = index_l[:]  

    player_turn = player(board)
    new_board[action[0]][action[1]] = player_turn
    new_index_l[action[0]] -= 1  
    return new_board, new_index_l

    
    raise NotImplementedError

def check_4(board,A):
    three=False
    for i in range(6):
        for j in range(2):
            if board[i][j]==A and board[i][j+1]==A and board[i][j+2]==A and board[i][j+3]==A:
                three=True
            if three==True:
              return three
    for i in range(3):
        for j in range(5):
            if board[i][j]==A and board[i+1][j]==A and board[i+2][j]==A and board[i+3][j]==A:
                three=True
            if three==True:
              return three 
    for i in range(3):
        for j in range(2): 
            if board[i][j]==A and board[i+1][j+1]==A and board[i+2][j+2]==A and board[i+3][j+3]==A:
               three=True
            if three==True:
              return three 
    for i in range(3):
        for j in range(4,-1,2): 
          
            
            if board[i][j]==A and board[i+1][j-1]==A and board[i+2][j-2]==A and board[i+3][j-3]==A:
               three=True
            if three==True:
              return three  
    for i in range(5,2,-1):
        for j in range(2): 
            
            
            if board[i][j]==A and board[i-1][j+1]==A and board[i-2][j+2]==A and board[i-3][j+3]==A:
               three=True
            if three==True:
              return three        
    for i in range(5,2,-1):
        for j in range(4,-1,2): 
            
            
            if board[i][j]==A and board[i-1][j-1]==A and board[i-2][j-2]==A and board[i-3][j-3]==A:
               three=True
            if three==True:
              return three               
                   
def winner(board):
    end=terminal(board)
    if end==False:
        return None
    else:
        win=check_4(board,X)
        if win==True:
            return X
        else:
            win=check_4(board,O)
            if win==True:
               return O
            else:
                return None

            
            
            

            
    
    

    raise NotImplementedError


def terminal(board):
    numx=count_forx(board)
    numo=count_foro(board)

    if check_4(board,X) or check_4(board,O) or numo+numx==30 :
        return True
    else :
        return False
    raise NotImplementedError


def utility(board):
    w=winner(board)
    if w==X:
        return 1000
    elif w==O:
        return -1000
    else:
        return 0
    raise NotImplementedError

def evaluate(board,A):
    
    three=False
    numm=0
    for i in range(6):
        for j in range(2):
            if board[i][j]==A and board[i][j+1]==A and board[i][j+2]==A and board[i][j+3]==None  :
                numm=numm+1
    for i in range(3):
        for j in range(5):
            if board[i][j]==A and board[i+1][j]==A and board[i+2][j]==A and board[i+3][j]==None:
                numm=numm+1 
    for i in range(3):
        for j in range(2): 
            if board[i][j]==A and board[i+1][j+1]==A and board[i+2][j+2]==A and board[i+3][j+3]==None:
                numm=numm+1 
    for i in range(3):
        for j in range(4,-1,2): 
        
            
            if board[i][j]==A and board[i+1][j-1]==A and board[i+2][j-2]==A and board[i+3][j-3]==A  :
                numm=numm+1  
    for i in range(5,2,-1):
        for j in range(2): 
            
            
            if board[i][j]==A and board[i-1][j+1]==A and board[i-2][j+2]==A  and board[i-3][j+3]==A:
                numm=numm+1        
    for i in range(5,2,-1):
        for j in range(4,-1,2): 
            
            
            if board[i][j]==A and board[i-1][j-1]==A and board[i-2][j-2]==A and board[i-3][j-3]==A :
                numm=numm+1
    if numm==0:
        for i in range(6):
            for j in range(2):
                if board[i][j]==A and board[i][j+1]==A and board[i][j+2]==None :
                    numm=numm+1
        for i in range(3):
            for j in range(5):
                if board[i][j]==A and board[i+1][j]==A and board[i+2][j]==None :
                    numm=numm+1 
        for i in range(3):
            for j in range(2): 
                if board[i][j]==A and board[i+1][j+1]==A and board[i+2][j+2]==None :
                    numm=numm+1 
        for i in range(3):
            for j in range(4,-1,2): 
            
                
                if board[i][j]==A and board[i+1][j-1]==A and board[i+2][j-2]==None:
                    numm=numm+1  
        for i in range(5,2,-1):
            for j in range(2): 
                
                
                if board[i][j]==A and board[i-1][j+1]==A and board[i-2][j+2]==None  :
                    numm=numm+1        
        for i in range(5,2,-1):
            for j in range(4,-1,2): 
                
                
                if board[i][j]==A and board[i-1][j-1]==A and board[i-2][j-2]==A  :
                    numm=numm+1
    if A=='O':

       return -numm
    else :
        return numm               

                    


     



def maxx(board, index_l,alpha,beta, depth):
    if terminal(board) :
        return utility(board), None
    if depth == 4:
       return  evaluate(board,X),None
    v = -math.inf
    best = None
    for action in actions(index_l):
        new_board, new_index = result(board, action, index_l)
        score, _ = minn(new_board, new_index,alpha,beta, depth + 1)
        if score > v:
            v = score
            best = action
        alpha = max(alpha, v)
        if beta <= alpha:
            break    
    return v, best

def minn(board, index_l,alpha,beta, depth):
    if terminal(board) :
        return utility(board), None
    if depth == 4:
        return  evaluate(board,O),None

    v = math.inf
    best = None
    for action in actions(index_l):
        new_board, new_index = result(board, action, index_l)
        score, _ = maxx(new_board, new_index,alpha,beta, depth + 1)
        if score < v:
            v = score
            best = action
        beta=min(beta,v)
        if beta<= alpha:
            break    
    return v, best



def minimax(board):
    depth = 0
    play = player(board)
    current_index_l = index_l[:]  

    if play == X:
        _, move = maxx(board, current_index_l,-math.inf,math.inf, depth)
    elif play == O:
        _, move = minn(board, current_index_l,-math.inf,math.inf, depth)
    else:
        return None

    
    index_l[move[0]] = move[1] - 1
    return move

bb=[[None, None, None, O, O], [None, None, None, None,None ], [None, None, None, None, None], [None, None, None, None, None], 
[None, None, X, X, X], [None, None, None, None, None]]
index_l=[2,4,4,4,1,4]
print(minimax(bb))


    
