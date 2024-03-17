# 7. Python program to find the factorial of a number provided by the user.
num = 8
factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

# 8. Program to display the Fibonacci sequence up to n-th term (Tested).
nterms = int(input("How many teams?"))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibanocci sequence upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

# 9. Recursive Python function to solve the tower of Hanoi (Tested).
def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)

n = 3
TowerOfHanoi(n, 'A', 'B', 'C')

# 10. Selection Sort.
def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [-2, 25, 0, 21, -7, 17]
size = len(data)
selectionSort(data, size)
print("Sorted Array in Ascending Order:")
print(data)

# 11. Stack implementation in Python (Tested).
def create_stack():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print("pushed item: " + item)

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
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))

# 12. Stack implementation using Linked list in Python.
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
            print("Stack Underflow")
        else:
            while (iternode != None):
                print(iternode.data, "->", end=" ")
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
print("Stack after popping 2 times")
MyStack.display()
print("\nTop element is ", MyStack.peek())

# 13. Write a Python program to solve N Queen using backtracking.
global N
N = 4

def printSolution(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solveNQUti(board, col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            if solveNQUti(board, col + 1) == True:
                return True
            board[i][col] = 0
    return False

def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if solveNQUti(board, 0) == False:
        print("Solution does not exist")
        return False
    printSolution(board)
    return True

if __name__ == '__main__':
    solveNQ()

# 14. Implementation - Longest Common Subsequence.
def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))

if __name__ == '__main__':
    S1 = "AGGTAB"
    S2 = "GXTXAYB"
    print("Length of LCS is", lcs(S1, S2, len(S1), len(S2)))

# 15. Recursion applications (Factorial of a Number).
def factorial_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 4
factorial = factorial_loop(number)
print("Factorial of", number, "is", factorial)

# 16. Python program for Fibonacci Series (Iterative version).
n = 8
num1 = 0
num2 = 1
next_number = num2
count = 1
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()

# 17. Python Program for Quick select (QuickSort).
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
        return kthSmallest(arr, index + 1, r, k - index + l - 1)
    print("Index out of bound")

arr = [10, 4, 5, 8, 6, 11, 26]
n = len(arr)
k = 3
print("K-th smallest element is ", end="")
print(kthSmallest(arr, 0, n - 1, k))
