import sys

class Stack:
    def __init__(self) -> None:
        self.s_list = []
        self.top = 0
        self.max = 100
    
    def push(self, item) -> None:
        if self.pop == self.max:
            exit(1)
        self.s_list.append(item)
        self.top += 1

    def pop(self) -> int:
        if self.top == 0:
            exit(1)
        self.top -= 1
        return self.s_list.pop()

    def isempty(self) -> bool:
        return self.top == 0
    
    def isfull(self) -> bool:
        return self.top == self.max


def check_value(value, n):
    return 0 <= value and value < n


def dfs(pan, n) -> None:
    stack = Stack()
    visited = [[False for _ in range(n)] for _ in range(n)]

    stack.push([0, 0, pan[0][0]]) # [(x, y), value]
    while not stack.isempty():
        vtx = stack.pop()
        x, y, value = vtx[0], vtx[1], vtx[2]
        if vtx[2] == -1:
            print("HaruHaru")
            return

        if visited[x][y]:
            continue
        else:
            visited[x][y] = True
        
        for i in range(2): # 0: right, 1: down
            if i == 0 and check_value(x + value, n):
                if not visited[x+value][y] :
                    stack.push([x+value, y, pan[x+value][y]])
            elif i == 1 and check_value(y + value, n):
                if not visited[x][y+value]:
                    stack.push([x, y+value, pan[x][y+value]])
    
    print("Hing")


n = int(sys.stdin.readline())
pan = list()
for _ in range(n):
    pan.append(list(map(int, sys.stdin.readline().split())))
dfs(pan, n)
