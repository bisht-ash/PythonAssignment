# PythonAssignment

Algorithm

1. Take input, size of the board and the board.
2. Intitialize a queue for implementing multisource Breath First Search.
3. Push all the boundary node with value 'O' to the queue.
4. Pop a element from the queue, change is to '*' . Then checks all it's 4 neighbour if their value is 'O' then push them to the queue. Repeat this until the queue is empty.
5. Then iterate over the board and change all 'O' to 'X' and then all '*' to 'O'.
6. Print the output board.
