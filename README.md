# PythonAssignment

Algorithm

1. Take input, size of the board and the board.
2. Initialize a list of list to maintain visited nodes.
3. Intitialize a queue for implementing multisource Breath First Search.
4. Push all the boundary node with value 'O' to the queue.
5. Pop a element from the queue, mark it as visited. Then checks all it's 4 neighbour if they are not visited and their value is 'O' then push them to the queue. Repeat this until the queue is empty.
6. Then iterate over the visited list of list and flip those 'O' to 'X' for which the corresponding visited value is False. 
7. Print the output board.