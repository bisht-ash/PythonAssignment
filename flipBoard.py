from collections import deque 
class Solution:
    # defined the class constructor to intialize data members 
    def __init__(self,totalRow,totalCol):
        self.totalRow=totalRow
        self.totalCol=totalCol

    # defined a method to check if the index stays within bound
    def isSafe(self,board, row, col):
        if(row < 0 or row >= self.totalRow or col < 0 or col >= self.totalCol):
            return False
        else:
            return True
        
    def validateInput(self,board):
        if(board==[]):
            raise Exception("Empty Input")
        else:
            if(len(board)<self.totalRow):
                raise Exception("Number of row not satisfied")
            # if less number of rows are provided
            for row in range(self.totalRow):
                if(len(board[row])<self.totalCol):
                    raise Exception("Number of column not satisfied")
                # if less number of cols are provided
                for col in range(self.totalCol):
                    # checking if there is something else in the board
                    if(board[row][col]!='X' and board[row][col]!='O'):
                        raise Exception("Invalid Input")
                    

    # flipBoard function which does the main work 
    def flipBoard(self, board):
        '''dx and dy are directional list 
        allows us to travel in all four direction easily '''
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        # created a queue to perform Breath First Search
        bfsQueue=deque()

        '''added all the boundary elements to the queue 
        we will perform a multi source BFS'''
        for row in range(self.totalRow):
            if(board[row][0]=='O'):
                bfsQueue.append([row,0])
            if(board[row][self.totalCol-1]=='O'):
                bfsQueue.append([row,self.totalCol-1])
        # we started the loop here from 1 to totalCol -1 so that we don't add the corner element twice
        for col in range(1,self.totalCol-1):
            if(board[0][col]=='O'):
                bfsQueue.append([0,col])
            if(board[self.totalRow-1][col]=='O'):
                bfsQueue.append([self.totalRow-1,col])

        '''BFS starts here 
        we marked all the Os that are connected to some boundary O
        and then we change all the other Os to X.
        we did this by marking all the Os that can be visited if we start the BFS from any boundary O'''
        while(len(bfsQueue)):
            # poping the first element 
            x=bfsQueue.popleft()
            if(board[x[0]][x[1]]=='O'):
                '''if the current O is not visited we mark it as visited 
                check all its 4 neighbour if they are O and are not visited 
                then push them to the queue'''
                board[x[0]][x[1]]='*'
                for i in range(4):
                    # this loop is to iterate over all 4 neighbour
                    if(self.isSafe(board,x[0]+dx[i],x[1]+dy[i])==True):
                        if(board[x[0]+dx[i]][x[1]+dy[i]]=='O'):
                            bfsQueue.append([x[0]+dx[i],x[1]+dy[i]])

        # we changed all the O that can not be visited from any boundary O 
        for row in range(0,self.totalRow):
            for col in range(0,self.totalCol):
                if(board[row][col]=='O'):
                    board[row][col]='X'
                if(board[row][col]=='*'):
                    board[row][col]='O'

            
def main():
    # defined a list to store the board
    board=[]
    totalRow=int(input("Enter the number of rows"))
    totalCol=int(input("Enter the number of columns"))

    # taking input board 
    for i in range(totalRow):
        board.append(input().split(" "))
    
    # Creating the solution object
    solutionObject= Solution(totalRow,totalCol)
    try:
        solutionObject.validateInput(board)
    except Exception as e:
        print(str(e))
    else:
        solutionObject.flipBoard(board)
        print(board)



if __name__=="__main__":
    main()