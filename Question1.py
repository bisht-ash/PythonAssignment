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

    # solve function which does the main work 
    def solve(self, board):
        # dx and dy are directional list 
        # allows us to travel in all four direction easily 
        dx=[1,0,-1,0]
        dy=[0,1,0,-1]
        # created a queue to perform Breath First Search
        bfsQueue=deque()

        # added all the boundary elements to the queue 
        # we will perform a multi source BFS
        for i in range(self.totalRow):
            if(board[i][0]=='O'):
                bfsQueue.append([i,0])
            if(board[i][self.totalCol-1]=='O'):
                bfsQueue.append([i,self.totalCol-1])
        # we started the loop here from 1 to totalCol -1 so that we don't add the corner element twice
        for i in range(1,self.totalCol-1):
            if(board[0][i]=='O'):
                bfsQueue.append([0,i])
            if(board[self.totalRow-1][i]=='O'):
                bfsQueue.append([self.totalRow-1,i])

        # BFS starts here 
        # we marked all the Os that are connected to some boundary O
        # and then we change all the other Os to X.
        # we did this by marking all the Os that can be visited if we start the BFS from any boundary O
        while(len(bfsQueue)):
            # poping the first element 
            x=bfsQueue.popleft()
            if(board[x[0]][x[1]]=='O'):
                # if the current O is not visited we mark it as visited 
                # check all its 4 neighbour if they are O and are not visited 
                # then push them to the queue
                board[x[0]][x[1]]='*'
                for i in range(4):
                    # this loop is to iterate over all 4 neighbour
                    if(self.isSafe(board,x[0]+dx[i],x[1]+dy[i])==True):
                        if(board[x[0]+dx[i]][x[1]+dy[i]]=='O'):
                            bfsQueue.append([x[0]+dx[i],x[1]+dy[i]])

        # we changed all the O that can not be visited from any boundary O 
        for i in range(0,self.totalRow):
            for j in range(0,self.totalCol):
                if(board[i][j]=='*'):
                    board[i][j]='X'

            
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
    solutionObject.solve(board)
    print(board)



if __name__=="__main__":
    main()