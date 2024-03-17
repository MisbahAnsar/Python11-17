#11th Practical
def create_stack(): 
  stack = [] 
  return stack 
def check_empty(stack): 
  return len(stack) == 0 
def push(stack,item): 
  stack.append(item) 
  print("pushed item:" + item) 
def pop(stack): 
  if (check_empty(stack)): 
     return "stack is empty" 
  return stack.pop() 
stack = create_stack() 
push(stack, str(1)) 
push(stack, str(2)) 
push(stack, str(3)) 
push(stack, str(4)) 
push(stack, str(5)) 
print("popped item:" + pop(stack)) 
print("stack after popping an element:" + str(stack))





#12th practical
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            return None
        else:
            poppednode = self.head
            self.head = self.head.next
            poppednode.next = None
            return poppednode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        iternode = self.head
        if self.isempty():
            print("Stack underflow")
        else:
            while(iternode != None):
                print(iternode.data, " -> ", end=" ")
                iternode = iternode.next
            return

MyStack = Stack()
MyStack.push(4)
MyStack.push(3)
MyStack.push(2)
MyStack.push(1)
MyStack.display()
print("\nTop element is ", MyStack.peek())
MyStack.pop()
MyStack.pop()
print("Stack after popping two times")
MyStack.display()
print("\nTop Element is ", MyStack.peek())






#13th Practical Nqueen
global N
N=4
def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j]==1:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()

def isSafe(board,row,col):
    for i in range(col):
        if board[row][i]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,N,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True
def solveNQUti(board,col):
    if col>=N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col]=1
        if solveNQUti(board, col+1)==True:
            return True
        board[i][col]
    return False
def solveNQ():
    board=[[0,0,0,0],
           [0,0,0,0],
           [0,0,0,0],
           [0,0,0,0]]
    if solveNQUti(board, 0)==False:
        print("Solution does not exist")
        return False
    printSolution(board)
    return True
if __name__=='__main__':
    solveNQ()
    
    
    
    
    
#17th Practical
def partition(arr, l, r): 	
  x = arr[r] 
  i = l 
  for j in range(l, r): 	
   if arr[j] <= x: 
      arr[i], arr[j] = arr[j], arr[i] 
      i += 1			
  arr[i], arr[r] = arr[r], arr[i] 
  return i 
def kthSmallest(arr, l, r, k): 
  if (k > 0 and k <= r - l + 1): 
   index = partition(arr, l, r) 
  if (index - l == k - 1): 
   return arr[index] 
  if (index - l > k - 1): 
   return kthSmallest(arr, l, index - 1, k) 
  return kthSmallest(arr, index + 1, r, 
   k - index + l - 1) 
  print("Index out of bound") 
arr = [ 10, 4, 5, 8, 6, 11, 26 ] 
n = len(arr) 
k = 3
print("K-th smallest element is ", end = "") 
print(kthSmallest(arr, 0, n - 1, k))
